# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.function import Function  # noqa: E501
from pollination_sdk.rest import ApiException

class TestFunction(unittest.TestCase):
    """Function unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Function
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.function.Function()  # noqa: E501
        if include_optional :
            return Function(
                annotations = {
                    'key' : '0'
                    }, 
                command = '0', 
                description = '0', 
                inputs = [
                    null
                    ], 
                language = null, 
                name = '0', 
                outputs = [
                    null
                    ], 
                source = '0', 
                type = 'Function'
            )
        else :
            return Function(
                name = '0',
        )

    def testFunction(self):
        """Test Function"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
