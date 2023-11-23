# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.45.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.plugin import Plugin  # noqa: E501
from pollination_sdk.rest import ApiException

class TestPlugin(unittest.TestCase):
    """Plugin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Plugin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.plugin.Plugin()  # noqa: E501
        if include_optional :
            return Plugin(
                annotations = {
                    'key' : '0'
                    }, 
                api_version = 'v1beta1', 
                config = null, 
                functions = [
                    pollination_sdk.models.function.Function(
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
                        type = 'Function', )
                    ], 
                metadata = null, 
                type = 'Plugin'
            )
        else :
            return Plugin(
                config = null,
                functions = [
                    pollination_sdk.models.function.Function(
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
                        type = 'Function', )
                    ],
                metadata = null,
        )

    def testPlugin(self):
        """Test Plugin"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
