# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.40.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.task_path_reference import TaskPathReference  # noqa: E501
from pollination_sdk.rest import ApiException

class TestTaskPathReference(unittest.TestCase):
    """TaskPathReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskPathReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.task_path_reference.TaskPathReference()  # noqa: E501
        if include_optional :
            return TaskPathReference(
                annotations = {
                    'key' : '0'
                    }, 
                name = '0', 
                type = 'TaskPathReference', 
                variable = '0'
            )
        else :
            return TaskPathReference(
                name = '0',
                variable = '0',
        )

    def testTaskPathReference(self):
        """Test TaskPathReference"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
