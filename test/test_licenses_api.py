# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.30.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.licenses_api import LicensesApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestLicensesApi(unittest.TestCase):
    """LicensesApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.licenses_api.LicensesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_activation(self):
        """Test case for delete_activation

        Delete Activation  # noqa: E501
        """
        pass

    def test_get_available_pools(self):
        """Test case for get_available_pools

        Cython Function Or Method  # noqa: E501
        """
        pass

    def test_get_license_activations(self):
        """Test case for get_license_activations

        Get Activations  # noqa: E501
        """
        pass

    def test_get_pool_license(self):
        """Test case for get_pool_license

        Get Pool License  # noqa: E501
        """
        pass

    def test_grant_access_to_pool(self):
        """Test case for grant_access_to_pool

        Cython Function Or Method  # noqa: E501
        """
        pass

    def test_regenerate_license_pool(self):
        """Test case for regenerate_license_pool

        Cython Function Or Method  # noqa: E501
        """
        pass

    def test_revoke_access_to_pool(self):
        """Test case for revoke_access_to_pool

        Cython Function Or Method  # noqa: E501
        """
        pass

    def test_update_license_pool(self):
        """Test case for update_license_pool

        Cython Function Or Method  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
