#!/usr/bin/env python3
"""
Test for client file
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
import utils
import client

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests methods in GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
        ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Tests org client methods
        """
        ghc = GithubOrgClient(org_name)
        ghc.org()
        mock_get_json.assert_called_once_with(ghc.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """
        Test _public_repos_url from client;
        Uses patch as a context manager to patch org() and make it return
        a known payload
        """
        with patch(
                "client.GithubOrgClient.org", new_callable=PropertyMock
                ) as mock_org:
            test_payload = {"repos_url": "a repo url"}
            mock_org.return_value = test_payload
            ghc = GithubOrgClient('org')
            self.assertEqual(ghc._public_repos_url, test_payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test public_repos from client;
        uses patch as both a decorator and a context manager
        """
        payload = [
                {"id": 328910, "name": "JavaWorks"},
                {"id": "340103", "name": "ClibSync"}
                ]
        mock_get_json.return_value = payload
        with patch(
                "client.GithubOrgClient._public_repos_url"
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "A repo url"

            ghc = GithubOrgClient('org')
            result = [load["name"] for load in payload]
            self.assertEqual(ghc.public_repos(), result)
            mock_get_json.assert_called_once()
            mock_public_repos_url.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the has_license method from GithubOrgClient.client
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
        )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration testing with fixtures
    """
    @classmethod
    def setupClass(cls):
        """
        Setupclass which mocks requests.get
        """
        cls.fixt_payloads = [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
                ]
        config = {'return_value.json.side_effect': cls.fixt_payload}
        cls.get_patcher = patch('requests.get', **config)
        # cls.mock_get.return_value = fixt_payloads
        # cls.mock_get.return_value.json.side_effect = cls.fixt_payloads
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Stops the patcher
        """
        cls.get_patcher.stop()
