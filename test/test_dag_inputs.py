# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.dag_inputs import DAGInputs  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDAGInputs(unittest.TestCase):
    """DAGInputs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DAGInputs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.dag_inputs.DAGInputs()  # noqa: E501
        if include_optional :
            return DAGInputs(
                artifacts = [
                    pollination_sdk.models.dag_input_artifact.DAGInputArtifact(
                        annotations = {
                            'key' : '0'
                            }, 
                        default = null, 
                        description = '0', 
                        name = '0', 
                        required = True, )
                    ], 
                parameters = [
                    pollination_sdk.models.dag_input_parameter.DAGInputParameter(
                        annotations = {
                            'key' : '0'
                            }, 
                        default = '0', 
                        description = '0', 
                        name = '0', 
                        required = True, )
                    ]
            )
        else :
            return DAGInputs(
        )

    def testDAGInputs(self):
        """Test DAGInputs"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
