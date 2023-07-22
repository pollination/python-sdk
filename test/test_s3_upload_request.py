# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.42.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.s3_upload_request import S3UploadRequest  # noqa: E501
from pollination_sdk.rest import ApiException

class TestS3UploadRequest(unittest.TestCase):
    """S3UploadRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test S3UploadRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.s3_upload_request.S3UploadRequest()  # noqa: E501
        if include_optional :
            return S3UploadRequest(
                fields = {
                    'key' : '0'
                    }, 
                url = '0'
            )
        else :
            return S3UploadRequest(
                fields = {
                    'key' : '0'
                    },
                url = '0',
        )

    def testS3UploadRequest(self):
        """Test S3UploadRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
