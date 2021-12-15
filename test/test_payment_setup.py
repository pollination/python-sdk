# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.21.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.payment_setup import PaymentSetup  # noqa: E501
from pollination_sdk.rest import ApiException

class TestPaymentSetup(unittest.TestCase):
    """PaymentSetup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentSetup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.payment_setup.PaymentSetup()  # noqa: E501
        if include_optional :
            return PaymentSetup(
                client_secret = '0'
            )
        else :
            return PaymentSetup(
                client_secret = '0',
        )

    def testPaymentSetup(self):
        """Test PaymentSetup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
