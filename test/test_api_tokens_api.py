# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.12.4
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.api_tokens_api import APITokensApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestAPITokensApi(unittest.TestCase):
    """APITokensApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.api_tokens_api.APITokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_token(self):
        """Test case for create_token

        Create a new API token  # noqa: E501
        """
        pass

    def test_delete_token(self):
        """Test case for delete_token

        Delete an API Token  # noqa: E501
        """
        pass

    def test_list_tokens(self):
        """Test case for list_tokens

        List user API tokens  # noqa: E501
        """
        pass

    def test_regenerate_token(self):
        """Test case for regenerate_token

        Regenerate an API token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
