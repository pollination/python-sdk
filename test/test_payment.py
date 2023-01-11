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
from pollination_sdk.models.payment import Payment  # noqa: E501
from pollination_sdk.rest import ApiException

class TestPayment(unittest.TestCase):
    """Payment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Payment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.payment.Payment()  # noqa: E501
        if include_optional :
            return Payment(
                amount = 56, 
                currency = '0', 
                id = 56, 
                is_one_off_charge = True, 
                is_paid = True, 
                payout_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                receipt_url = '0', 
                subscription_id = 56
            )
        else :
            return Payment(
                amount = 56,
                currency = '0',
                id = 56,
                is_one_off_charge = True,
                is_paid = True,
                payout_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                subscription_id = 56,
        )

    def testPayment(self):
        """Test Payment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
