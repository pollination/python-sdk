# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.18
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.job import Job  # noqa: E501
from pollination_sdk.rest import ApiException

class TestJob(unittest.TestCase):
    """Job unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Job
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.job.Job()  # noqa: E501
        if include_optional :
            return Job(
                annotations = {
                    'key' : '0'
                    }, 
                api_version = 'v1beta1', 
                arguments = [
                    null
                    ], 
                description = '0', 
                labels = {
                    'key' : '0'
                    }, 
                name = '0', 
                source = '0', 
                type = 'Job'
            )
        else :
            return Job(
                source = '0',
        )

    def testJob(self):
        """Test Job"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
