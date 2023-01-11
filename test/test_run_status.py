# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.36.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.run_status import RunStatus  # noqa: E501
from pollination_sdk.rest import ApiException

class TestRunStatus(unittest.TestCase):
    """RunStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RunStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.run_status.RunStatus()  # noqa: E501
        if include_optional :
            return RunStatus(
                annotations = {
                    'key' : '0'
                    }, 
                api_version = 'v1beta1', 
                entrypoint = '0', 
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '0', 
                inputs = [
                    null
                    ], 
                job_id = '0', 
                message = '0', 
                outputs = [
                    null
                    ], 
                source = '0', 
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = null, 
                steps = {
                    'key' : pollination_sdk.models.step_status.StepStatus(
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
                    }, 
                type = 'RunStatus'
            )
        else :
            return RunStatus(
                id = '0',
                inputs = [
                    null
                    ],
                job_id = '0',
                outputs = [
                    null
                    ],
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testRunStatus(self):
        """Test RunStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
