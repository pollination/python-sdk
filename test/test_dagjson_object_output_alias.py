# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.39.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.dagjson_object_output_alias import DAGJSONObjectOutputAlias  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDAGJSONObjectOutputAlias(unittest.TestCase):
    """DAGJSONObjectOutputAlias unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DAGJSONObjectOutputAlias
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.dagjson_object_output_alias.DAGJSONObjectOutputAlias()  # noqa: E501
        if include_optional :
            return DAGJSONObjectOutputAlias(
                annotations = {
                    'key' : '0'
                    }, 
                description = '0', 
                _from = null, 
                handler = [
                    pollination_sdk.models.io_alias_handler.IOAliasHandler(
                        annotations = {
                            'key' : '0'
                            }, 
                        function = '0', 
                        index = 56, 
                        language = '0', 
                        module = 'honeybee_rhino.handlers', 
                        type = 'IOAliasHandler', )
                    ], 
                name = '0', 
                platform = [
                    '0'
                    ], 
                required = True, 
                type = 'DAGJSONObjectOutputAlias'
            )
        else :
            return DAGJSONObjectOutputAlias(
                _from = null,
                handler = [
                    pollination_sdk.models.io_alias_handler.IOAliasHandler(
                        annotations = {
                            'key' : '0'
                            }, 
                        function = '0', 
                        index = 56, 
                        language = '0', 
                        module = 'honeybee_rhino.handlers', 
                        type = 'IOAliasHandler', )
                    ],
                name = '0',
                platform = [
                    '0'
                    ],
        )

    def testDAGJSONObjectOutputAlias(self):
        """Test DAGJSONObjectOutputAlias"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
