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
from pollination_sdk.models.queenbee_operator_metadata_meta_data import QueenbeeOperatorMetadataMetaData  # noqa: E501
from pollination_sdk.rest import ApiException

class TestQueenbeeOperatorMetadataMetaData(unittest.TestCase):
    """QueenbeeOperatorMetadataMetaData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test QueenbeeOperatorMetadataMetaData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.queenbee_operator_metadata_meta_data.QueenbeeOperatorMetadataMetaData()  # noqa: E501
        if include_optional :
            return QueenbeeOperatorMetadataMetaData(
                app_version = '0', 
                deprecated = True, 
                description = '0', 
                home = '0', 
                icon = '0', 
                keywords = [
                    '0'
                    ], 
                maintainers = [
                    pollination_sdk.models.maintainer.Maintainer(
                        email = '0', 
                        name = '0', )
                    ], 
                name = '0', 
                sources = [
                    '0'
                    ], 
                tag = '0'
            )
        else :
            return QueenbeeOperatorMetadataMetaData(
                name = '0',
                tag = '0',
        )

    def testQueenbeeOperatorMetadataMetaData(self):
        """Test QueenbeeOperatorMetadataMetaData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
