# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.billing_option import BillingOption  # noqa: E501
from pollination_sdk.rest import ApiException

class TestBillingOption(unittest.TestCase):
    """BillingOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BillingOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.billing_option.BillingOption()  # noqa: E501
        if include_optional :
            return BillingOption(
                billing_period = 56, 
                billing_type = '0', 
                id = 56, 
                name = '0', 
                recurring_price = {
                    'key' : 1.337
                    }
            )
        else :
            return BillingOption(
                billing_period = 56,
                billing_type = '0',
                id = 56,
                name = '0',
                recurring_price = {
                    'key' : 1.337
                    },
        )

    def testBillingOption(self):
        """Test BillingOption"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
