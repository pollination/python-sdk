# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.12.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.s3 import S3  # noqa: E501
from pollination_sdk.rest import ApiException

class TestS3(unittest.TestCase):
    """S3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test S3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.s3.S3()  # noqa: E501
        if include_optional :
            return S3(
                annotations = {
                    'key' : '0'
                    }, 
                bucket = '0', 
                credentials_path = '0', 
                endpoint = '0', 
                key = '0', 
                type = 'S3'
            )
        else :
            return S3(
                bucket = '0',
                endpoint = '0',
                key = '0',
        )

    def testS3(self):
        """Test S3"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
