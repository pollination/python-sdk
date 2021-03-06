# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.19
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.accounts_api import AccountsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_account(self):
        """Test case for get_account

        Get an account by name  # noqa: E501
        """
        pass

    def test_list_accounts(self):
        """Test case for list_accounts

        List Accounts on the Pollination platform  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
