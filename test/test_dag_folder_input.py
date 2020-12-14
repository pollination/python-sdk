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
from pollination_sdk.models.dag_folder_input import DAGFolderInput  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDAGFolderInput(unittest.TestCase):
    """DAGFolderInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DAGFolderInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.dag_folder_input.DAGFolderInput()  # noqa: E501
        if include_optional :
            return DAGFolderInput(
                alias = [
                    null
                    ], 
                annotations = {
                    'key' : '0'
                    }, 
                default = null, 
                description = '0', 
                name = '0', 
                required = True, 
                spec = pollination_sdk.models.spec.Spec(), 
                type = 'DAGFolderInput'
            )
        else :
            return DAGFolderInput(
                name = '0',
        )

    def testDAGFolderInput(self):
        """Test DAGFolderInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()