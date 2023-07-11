# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.41.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.user_api import UserApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Register a new user  # noqa: E501
        """
        pass

    def test_get_me(self):
        """Test case for get_me

        Get authenticated user profile.  # noqa: E501
        """
        pass

    def test_get_roles(self):
        """Test case for get_roles

        Get the authenticated user roles  # noqa: E501
        """
        pass

    def test_update_user_profile(self):
        """Test case for update_user_profile

        Update the authenticated user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
