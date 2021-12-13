# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: v0.20.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.daily_usage import DailyUsage  # noqa: E501
from pollination_sdk.rest import ApiException

class TestDailyUsage(unittest.TestCase):
    """DailyUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DailyUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.daily_usage.DailyUsage()  # noqa: E501
        if include_optional :
            return DailyUsage(
                cpu = 1.337, 
                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                failed = 56, 
                memory = 1.337, 
                succeeded = 56
            )
        else :
            return DailyUsage(
                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testDailyUsage(self):
        """Test DailyUsage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()