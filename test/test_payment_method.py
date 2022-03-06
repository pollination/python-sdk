# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.27.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.payment_method import PaymentMethod  # noqa: E501
from pollination_sdk.rest import ApiException

class TestPaymentMethod(unittest.TestCase):
    """PaymentMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.payment_method.PaymentMethod()  # noqa: E501
        if include_optional :
            return PaymentMethod(
                card_type = 'master', 
                expiry_date = '0', 
                last_four_digits = '0', 
                payment_method = 'card'
            )
        else :
            return PaymentMethod(
                card_type = 'master',
                expiry_date = '0',
                last_four_digits = '0',
                payment_method = 'card',
        )

    def testPaymentMethod(self):
        """Test PaymentMethod"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()