#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access_nested_map utils methods
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        expected_exception = "KeyError('{}')".format(expected)
        self.assertEqual(repr(err.exception), expected_exception)


class TestGetJson(unittest.TestCase):
    """
    Test get_json utils methods
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        mock = Mock()
        mock.json.return_value = test_payload
        mock_get.return_value = mock
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once()
