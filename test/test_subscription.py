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
from pollination_sdk.models.subscription import Subscription  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSubscription(unittest.TestCase):
    """Subscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Subscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.subscription.Subscription()  # noqa: E501
        if include_optional :
            return Subscription(
                billing_info = null, 
                external_id = '0', 
                id = '0', 
                owner = null, 
                period_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                period_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                plan_multiplier = 56, 
                plan_slug = '0', 
                type = null
            )
        else :
            return Subscription(
                id = '0',
                owner = null,
                period_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                period_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                plan_slug = '0',
                type = null,
        )

    def testSubscription(self):
        """Test Subscription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
