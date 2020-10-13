# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.operators_api import OperatorsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestOperatorsApi(unittest.TestCase):
    """OperatorsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.operators_api.OperatorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_operator(self):
        """Test case for create_operator

        Create an Operator  # noqa: E501
        """
        pass

    def test_create_operator_package(self):
        """Test case for create_operator_package

        Create a new Operator package  # noqa: E501
        """
        pass

    def test_delete_operator(self):
        """Test case for delete_operator

        Delete an Operator  # noqa: E501
        """
        pass

    def test_delete_operator_org_permission(self):
        """Test case for delete_operator_org_permission

        Remove a Repository permissions  # noqa: E501
        """
        pass

    def test_get_operator(self):
        """Test case for get_operator

        Get an operator  # noqa: E501
        """
        pass

    def test_get_operator_access_permissions(self):
        """Test case for get_operator_access_permissions

        Get operator access permissions  # noqa: E501
        """
        pass

    def test_get_operator_by_tag(self):
        """Test case for get_operator_by_tag

        Get an operator tag  # noqa: E501
        """
        pass

    def test_list_operator_tags(self):
        """Test case for list_operator_tags

        Get an operator tags  # noqa: E501
        """
        pass

    def test_list_operators(self):
        """Test case for list_operators

        List operators  # noqa: E501
        """
        pass

    def test_update_operator(self):
        """Test case for update_operator

        Update an Operator  # noqa: E501
        """
        pass

    def test_upsert_operator_permission(self):
        """Test case for upsert_operator_permission

        Upsert a new permission to a operator  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
