# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.31.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.step_list import StepList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestStepList(unittest.TestCase):
    """StepList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StepList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.step_list.StepList()  # noqa: E501
        if include_optional :
            return StepList(
                next_page = 56, 
                page = 56, 
                page_count = 56, 
                per_page = 56, 
                resources = [
                    pollination_sdk.models.step_status.StepStatus(
                        annotations = {
                            'key' : '0'
                            }, 
                        boundary_id = '0', 
                        children_ids = [
                            '0'
                            ], 
                        command = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '0', 
                        inputs = [
                            null
                            ], 
                        message = '0', 
                        name = '0', 
                        outbound_steps = [
                            '0'
                            ], 
                        outputs = [
                            null
                            ], 
                        source = '0', 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = null, 
                        status_type = null, 
                        template_ref = '0', 
                        type = 'StepStatus', )
                    ], 
                total_count = 56
            )
        else :
            return StepList(
                page = 56,
                page_count = 56,
                per_page = 56,
                resources = [
                    pollination_sdk.models.step_status.StepStatus(
                        annotations = {
                            'key' : '0'
                            }, 
                        boundary_id = '0', 
                        children_ids = [
                            '0'
                            ], 
                        command = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '0', 
                        inputs = [
                            null
                            ], 
                        message = '0', 
                        name = '0', 
                        outbound_steps = [
                            '0'
                            ], 
                        outputs = [
                            null
                            ], 
                        source = '0', 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = null, 
                        status_type = null, 
                        template_ref = '0', 
                        type = 'StepStatus', )
                    ],
                total_count = 56,
        )

    def testStepList(self):
        """Test StepList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
