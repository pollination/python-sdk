# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.19
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.function_integer_input import FunctionIntegerInput  # noqa: E501
from pollination_sdk.rest import ApiException

class TestFunctionIntegerInput(unittest.TestCase):
    """FunctionIntegerInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FunctionIntegerInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.function_integer_input.FunctionIntegerInput()  # noqa: E501
        if include_optional :
            return FunctionIntegerInput(
                alias = [
                    null
                    ], 
                annotations = {
                    'key' : '0'
                    }, 
                default = 56, 
                description = '0', 
                name = '0', 
                required = True, 
                spec = pollination_sdk.models.spec.Spec(), 
                type = 'FunctionIntegerInput'
            )
        else :
            return FunctionIntegerInput(
                name = '0',
        )

    def testFunctionIntegerInput(self):
        """Test FunctionIntegerInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
