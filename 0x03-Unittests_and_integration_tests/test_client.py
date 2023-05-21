#!/usr/bin/env python3
"""
Test for client file
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
import utils

# from client import GithugOrgClient
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
