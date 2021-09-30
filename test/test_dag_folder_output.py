# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: v0.17.0-staging
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.dag_folder_output import DAGFolderOutput  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDAGFolderOutput(unittest.TestCase):
    """DAGFolderOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DAGFolderOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.dag_folder_output.DAGFolderOutput()  # noqa: E501
        if include_optional :
            return DAGFolderOutput(
                alias = [
                    null
                    ], 
                annotations = {
                    'key' : '0'
                    }, 
                description = '0', 
                _from = null, 
                name = '0', 
                required = True, 
                type = 'DAGFolderOutput'
            )
        else :
            return DAGFolderOutput(
                _from = null,
                name = '0',
        )

    def testDAGFolderOutput(self):
        """Test DAGFolderOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
