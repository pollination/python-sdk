# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: v0.9.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.repository_list import RepositoryList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestRepositoryList(unittest.TestCase):
    """RepositoryList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RepositoryList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.repository_list.RepositoryList()  # noqa: E501
        if include_optional :
            return RepositoryList(
                next_page = 56, 
                page = 56, 
                page_count = 56, 
                per_page = 56, 
                resources = [
                    pollination_sdk.models.repository.Repository(
                        description = '0', 
                        icon = '0', 
                        id = '0', 
                        keywords = [
                            '0'
                            ], 
                        latest_tag = '0', 
                        name = '0', 
                        owner = null, 
                        permissions = null, 
                        public = True, 
                        slug = '0', )
                    ], 
                total_count = 56
            )
        else :
            return RepositoryList(
                page = 56,
                page_count = 56,
                per_page = 56,
                resources = [
                    pollination_sdk.models.repository.Repository(
                        description = '0', 
                        icon = '0', 
                        id = '0', 
                        keywords = [
                            '0'
                            ], 
                        latest_tag = '0', 
                        name = '0', 
                        owner = null, 
                        permissions = null, 
                        public = True, 
                        slug = '0', )
                    ],
                total_count = 56,
        )

    def testRepositoryList(self):
        """Test RepositoryList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
