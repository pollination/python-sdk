# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.37.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.subscription_payment import SubscriptionPayment  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSubscriptionPayment(unittest.TestCase):
    """SubscriptionPayment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionPayment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.subscription_payment.SubscriptionPayment()  # noqa: E501
        if include_optional :
            return SubscriptionPayment(
                amount = 1.337, 
                currency = '0', 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else :
            return SubscriptionPayment(
                amount = 1.337,
                currency = '0',
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )

    def testSubscriptionPayment(self):
        """Test SubscriptionPayment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
