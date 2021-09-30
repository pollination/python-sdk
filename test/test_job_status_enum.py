# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: v0.17.0-staging
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.job_status_enum import JobStatusEnum  # noqa: E501
from pollination_sdk.rest import ApiException

class TestJobStatusEnum(unittest.TestCase):
    """JobStatusEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobStatusEnum
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.job_status_enum.JobStatusEnum()  # noqa: E501
        if include_optional :
            return JobStatusEnum(
            )
        else :
            return JobStatusEnum(
        )

    def testJobStatusEnum(self):
        """Test JobStatusEnum"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
