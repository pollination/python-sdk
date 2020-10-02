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
from pollination_sdk.models.dag_task_parameter_argument import DAGTaskParameterArgument  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDAGTaskParameterArgument(unittest.TestCase):
    """DAGTaskParameterArgument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DAGTaskParameterArgument
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.dag_task_parameter_argument.DAGTaskParameterArgument()  # noqa: E501
        if include_optional :
            return DAGTaskParameterArgument(
                _from = null, 
                name = '0', 
                value = '0'
            )
        else :
            return DAGTaskParameterArgument(
                name = '0',
        )

    def testDAGTaskParameterArgument(self):
        """Test DAGTaskParameterArgument"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
