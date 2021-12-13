# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.20.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.price_tier import PriceTier  # noqa: E501
from pollination_sdk.rest import ApiException

class TestPriceTier(unittest.TestCase):
    """PriceTier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PriceTier
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.price_tier.PriceTier()  # noqa: E501
        if include_optional :
            return PriceTier(
                flat_amount = 56, 
                flat_amount_decimal = '0', 
                unit_amount = 56, 
                unit_amount_decimal = '0', 
                up_to = 56
            )
        else :
            return PriceTier(
                unit_amount = 56,
                unit_amount_decimal = '0',
        )

    def testPriceTier(self):
        """Test PriceTier"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
