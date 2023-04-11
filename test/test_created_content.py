# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.37.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.created_content import CreatedContent  # noqa: E501
from pollination_sdk.rest import ApiException

class TestCreatedContent(unittest.TestCase):
    """CreatedContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreatedContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.created_content.CreatedContent()  # noqa: E501
        if include_optional :
            return CreatedContent(
                id = '3fa85f64-5717-4562-b3fc-2c963f66afa6', 
                message = 'Use Location in headers to access the new object.'
            )
        else :
            return CreatedContent(
                id = '3fa85f64-5717-4562-b3fc-2c963f66afa6',
        )

    def testCreatedContent(self):
        """Test CreatedContent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
