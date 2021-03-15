# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.12.3
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.registries_api import RegistriesApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestRegistriesApi(unittest.TestCase):
    """RegistriesApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.registries_api.RegistriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_package(self):
        """Test case for get_package

        Get Package  # noqa: E501
        """
        pass

    def test_get_package_json(self):
        """Test case for get_package_json

        Get Package in JSON format  # noqa: E501
        """
        pass

    def test_get_registry_index(self):
        """Test case for get_registry_index

        Get Registry Index  # noqa: E501
        """
        pass

    def test_post_plugin(self):
        """Test case for post_plugin

        Push a plugin to the registry  # noqa: E501
        """
        pass

    def test_post_recipe(self):
        """Test case for post_recipe

        Push an Recipe to the registry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
