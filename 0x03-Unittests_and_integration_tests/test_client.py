#!/usr/bin/env python3
"""
Test for client file
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import utils
import client

from client import GithubOrgClient


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
