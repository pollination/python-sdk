# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.34.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.step_integer_input import StepIntegerInput  # noqa: E501
from pollination_sdk.rest import ApiException

class TestStepIntegerInput(unittest.TestCase):
    """StepIntegerInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StepIntegerInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.step_integer_input.StepIntegerInput()  # noqa: E501
        if include_optional :
            return StepIntegerInput(
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
                type = 'StepIntegerInput', 
                value = 56
            )
        else :
            return StepIntegerInput(
                name = '0',
                value = 56,
        )

    def testStepIntegerInput(self):
        """Test StepIntegerInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
