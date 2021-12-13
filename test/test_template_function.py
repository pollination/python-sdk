# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.20.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.template_function import TemplateFunction  # noqa: E501
from pollination_sdk.rest import ApiException

class TestTemplateFunction(unittest.TestCase):
    """TemplateFunction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TemplateFunction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.template_function.TemplateFunction()  # noqa: E501
        if include_optional :
            return TemplateFunction(
                annotations = {
                    'key' : '0'
                    }, 
                command = '0', 
                config = null, 
                description = '0', 
                inputs = [
                    null
                    ], 
                name = '0', 
                outputs = [
                    null
                    ], 
                type = 'TemplateFunction'
            )
        else :
            return TemplateFunction(
                command = '0',
                config = null,
                name = '0',
        )

    def testTemplateFunction(self):
        """Test TemplateFunction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
