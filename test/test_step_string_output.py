# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.33.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.step_string_output import StepStringOutput  # noqa: E501
from pollination_sdk.rest import ApiException

class TestStepStringOutput(unittest.TestCase):
    """StepStringOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StepStringOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.step_string_output.StepStringOutput()  # noqa: E501
        if include_optional :
            return StepStringOutput(
                annotations = {
                    'key' : '0'
                    }, 
                description = '0', 
                name = '0', 
                path = '0', 
                required = True, 
                type = 'StepStringOutput', 
                value = '0'
            )
        else :
            return StepStringOutput(
                name = '0',
                path = '0',
                value = '0',
        )

    def testStepStringOutput(self):
        """Test StepStringOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
