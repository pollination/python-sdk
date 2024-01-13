# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.dag_string_output import DAGStringOutput  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDAGStringOutput(unittest.TestCase):
    """DAGStringOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DAGStringOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.dag_string_output.DAGStringOutput()  # noqa: E501
        if include_optional :
            return DAGStringOutput(
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
                type = 'DAGStringOutput'
            )
        else :
            return DAGStringOutput(
                _from = null,
                name = '0',
        )

    def testDAGStringOutput(self):
        """Test DAGStringOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
