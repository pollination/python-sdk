# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.users_api import UsersApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_username(self):
        """Test case for check_username

        Check if a username is already taken  # noqa: E501
        """
        pass

    def test_get_one_user(self):
        """Test case for get_one_user

        Get a specific user profile  # noqa: E501
        """
        pass

    def test_list_users(self):
        """Test case for list_users

        List Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
