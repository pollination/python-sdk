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
from pollination_sdk.models.dag_task_loop import DAGTaskLoop  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDAGTaskLoop(unittest.TestCase):
    """DAGTaskLoop unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DAGTaskLoop
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.dag_task_loop.DAGTaskLoop()  # noqa: E501
        if include_optional :
            return DAGTaskLoop(
                annotations = {
                    'key' : '0'
                    }, 
                _from = null, 
                type = 'DAGTaskLoop'
            )
        else :
            return DAGTaskLoop(
        )

    def testDAGTaskLoop(self):
        """Test DAGTaskLoop"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
