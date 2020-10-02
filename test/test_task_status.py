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
from pollination_sdk.models.task_status import TaskStatus  # noqa: E501
from pollination_sdk.rest import ApiException

class TestTaskStatus(unittest.TestCase):
    """TaskStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.task_status.TaskStatus()  # noqa: E501
        if include_optional :
            return TaskStatus(
                boundary_id = '0', 
                children = [
                    '0'
                    ], 
                command = '0', 
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '0', 
                inputs = null, 
                message = '0', 
                name = '0', 
                outbound_tasks = [
                    '0'
                    ], 
                outputs = null, 
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = '0', 
                template_ref = '0', 
                type = 'function'
            )
        else :
            return TaskStatus(
                children = [
                    '0'
                    ],
                id = '0',
                inputs = null,
                name = '0',
                outbound_tasks = [
                    '0'
                    ],
                outputs = null,
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = '0',
                template_ref = '0',
                type = 'function',
        )

    def testTaskStatus(self):
        """Test TaskStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
