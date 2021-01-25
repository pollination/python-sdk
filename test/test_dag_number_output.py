# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.17
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.dag_number_output import DAGNumberOutput  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDAGNumberOutput(unittest.TestCase):
    """DAGNumberOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DAGNumberOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.dag_number_output.DAGNumberOutput()  # noqa: E501
        if include_optional :
            return DAGNumberOutput(
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
                type = 'DAGNumberOutput'
            )
        else :
            return DAGNumberOutput(
                _from = null,
                name = '0',
        )

    def testDAGNumberOutput(self):
        """Test DAGNumberOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
