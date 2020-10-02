# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: v0.9.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.operator import Operator  # noqa: E501
from pollination_sdk.rest import ApiException

class TestOperator(unittest.TestCase):
    """Operator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Operator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.operator.Operator()  # noqa: E501
        if include_optional :
            return Operator(
                config = null, 
                functions = [
                    pollination_sdk.models.function.Function(
                        command = '0', 
                        description = '0', 
                        inputs = null, 
                        name = '0', 
                        outputs = null, )
                    ], 
                metadata = null
            )
        else :
            return Operator(
                config = null,
                functions = [
                    pollination_sdk.models.function.Function(
                        command = '0', 
                        description = '0', 
                        inputs = null, 
                        name = '0', 
                        outputs = null, )
                    ],
                metadata = null,
        )

    def testOperator(self):
        """Test Operator"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
