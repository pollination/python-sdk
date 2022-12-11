# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.33.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.task_path_return import TaskPathReturn  # noqa: E501
from pollination_sdk.rest import ApiException

class TestTaskPathReturn(unittest.TestCase):
    """TaskPathReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskPathReturn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.task_path_return.TaskPathReturn()  # noqa: E501
        if include_optional :
            return TaskPathReturn(
                annotations = {
                    'key' : '0'
                    }, 
                description = '0', 
                name = '0', 
                path = '0', 
                required = True, 
                type = 'TaskPathReturn'
            )
        else :
            return TaskPathReturn(
                name = '0',
                path = '0',
        )

    def testTaskPathReturn(self):
        """Test TaskPathReturn"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
