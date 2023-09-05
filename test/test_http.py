# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.43.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.http import HTTP  # noqa: E501
from pollination_sdk.rest import ApiException

class TestHTTP(unittest.TestCase):
    """HTTP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HTTP
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.http.HTTP()  # noqa: E501
        if include_optional :
            return HTTP(
                annotations = {
                    'key' : '0'
                    }, 
                type = 'HTTP', 
                url = '0'
            )
        else :
            return HTTP(
                url = '0',
        )

    def testHTTP(self):
        """Test HTTP"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
