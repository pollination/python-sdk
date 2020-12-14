# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.11
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.function_json_object_input import FunctionJSONObjectInput  # noqa: E501
from pollination_sdk.rest import ApiException

class TestFunctionJSONObjectInput(unittest.TestCase):
    """FunctionJSONObjectInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FunctionJSONObjectInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.function_json_object_input.FunctionJSONObjectInput()  # noqa: E501
        if include_optional :
            return FunctionJSONObjectInput(
                alias = [
                    null
                    ], 
                annotations = {
                    'key' : '0'
                    }, 
                default = pollination_sdk.models.default.Default(), 
                description = '0', 
                name = '0', 
                required = True, 
                spec = pollination_sdk.models.spec.Spec(), 
                type = 'FunctionJSONObjectInput'
            )
        else :
            return FunctionJSONObjectInput(
                name = '0',
        )

    def testFunctionJSONObjectInput(self):
        """Test FunctionJSONObjectInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
