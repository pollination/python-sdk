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
from pollination_sdk.models.license import License  # noqa: E501
from pollination_sdk.rest import ApiException

class TestLicense(unittest.TestCase):
    """License unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test License
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.license.License()  # noqa: E501
        if include_optional :
            return License(
                annotations = {
                    'key' : '0'
                    }, 
                name = '0', 
                type = 'License', 
                url = '0'
            )
        else :
            return License(
                name = '0',
        )

    def testLicense(self):
        """Test License"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
