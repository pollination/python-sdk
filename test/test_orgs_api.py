# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.22.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.orgs_api import OrgsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestOrgsApi(unittest.TestCase):
    """OrgsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.orgs_api.OrgsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_org(self):
        """Test case for create_org

        Create an Org  # noqa: E501
        """
        pass

    def test_delete_org(self):
        """Test case for delete_org

        Delete an Org  # noqa: E501
        """
        pass

    def test_delete_org_member(self):
        """Test case for delete_org_member

        Remove an Org member  # noqa: E501
        """
        pass

    def test_get_org(self):
        """Test case for get_org

        Get an Org  # noqa: E501
        """
        pass

    def test_get_org_members(self):
        """Test case for get_org_members

        List organization members  # noqa: E501
        """
        pass

    def test_list_orgs(self):
        """Test case for list_orgs

        List Orgs  # noqa: E501
        """
        pass

    def test_update_org(self):
        """Test case for update_org

        Update an Org  # noqa: E501
        """
        pass

    def test_upsert_org_member(self):
        """Test case for upsert_org_member

        Add or update the role of an Org Member  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
