# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.16.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.meta_data import MetaData  # noqa: E501
from pollination_sdk.rest import ApiException

class TestMetaData(unittest.TestCase):
    """MetaData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetaData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.meta_data.MetaData()  # noqa: E501
        if include_optional :
            return MetaData(
                annotations = {
                    'key' : '0'
                    }, 
                app_version = '0', 
                deprecated = True, 
                description = '0', 
                home = '0', 
                icon = '0', 
                keywords = [
                    '0'
                    ], 
                license = null, 
                maintainers = [
                    pollination_sdk.models.maintainer.Maintainer(
                        annotations = {
                            'key' : '0'
                            }, 
                        email = '0', 
                        name = '0', 
                        type = 'Maintainer', )
                    ], 
                name = '0', 
                sources = [
                    '0'
                    ], 
                tag = '0', 
                type = 'MetaData'
            )
        else :
            return MetaData(
                name = '0',
                tag = '0',
        )

    def testMetaData(self):
        """Test MetaData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
