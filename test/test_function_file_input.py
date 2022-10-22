# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.31.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.function_file_input import FunctionFileInput  # noqa: E501
from pollination_sdk.rest import ApiException

class TestFunctionFileInput(unittest.TestCase):
    """FunctionFileInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FunctionFileInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.function_file_input.FunctionFileInput()  # noqa: E501
        if include_optional :
            return FunctionFileInput(
                alias = [
                    null
                    ], 
                annotations = {
                    'key' : '0'
                    }, 
                default = null, 
                description = '0', 
                extensions = [
                    '0'
                    ], 
                name = '0', 
                path = '0', 
                required = True, 
                spec = pollination_sdk.models.spec.Spec(), 
                type = 'FunctionFileInput'
            )
        else :
            return FunctionFileInput(
                name = '0',
                path = '0',
        )

    def testFunctionFileInput(self):
        """Test FunctionFileInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
