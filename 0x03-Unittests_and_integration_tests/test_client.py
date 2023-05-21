#!/usr/bin/env python3
"""
Test for client file
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import utils

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
