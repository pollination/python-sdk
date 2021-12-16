# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.21.2
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.new_subscription_item import NewSubscriptionItem  # noqa: E501
from pollination_sdk.rest import ApiException

class TestNewSubscriptionItem(unittest.TestCase):
    """NewSubscriptionItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewSubscriptionItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.new_subscription_item.NewSubscriptionItem()  # noqa: E501
        if include_optional :
            return NewSubscriptionItem(
                price = pollination_sdk.models.price.Price(
                    active = True, 
                    currency = '0', 
                    id = '0', 
                    metadata = pollination_sdk.models.metadata.Metadata(), 
                    nickname = '0', 
                    product = '0', 
                    recurring = pollination_sdk.models.price_recurrence.PriceRecurrence(
                        interval = '0', 
                        interval_count = 56, 
                        usage_type = '0', ), 
                    tiers = [
                        pollination_sdk.models.price_tier.PriceTier(
                            flat_amount = 56, 
                            flat_amount_decimal = '0', 
                            unit_amount = 56, 
                            unit_amount_decimal = '0', 
                            up_to = 56, )
                        ], 
                    type = 'recurring', 
                    unit_amount = 56, ), 
                quantity = 56
            )
        else :
            return NewSubscriptionItem(
                price = pollination_sdk.models.price.Price(
                    active = True, 
                    currency = '0', 
                    id = '0', 
                    metadata = pollination_sdk.models.metadata.Metadata(), 
                    nickname = '0', 
                    product = '0', 
                    recurring = pollination_sdk.models.price_recurrence.PriceRecurrence(
                        interval = '0', 
                        interval_count = 56, 
                        usage_type = '0', ), 
                    tiers = [
                        pollination_sdk.models.price_tier.PriceTier(
                            flat_amount = 56, 
                            flat_amount_decimal = '0', 
                            unit_amount = 56, 
                            unit_amount_decimal = '0', 
                            up_to = 56, )
                        ], 
                    type = 'recurring', 
                    unit_amount = 56, ),
                quantity = 56,
        )

    def testNewSubscriptionItem(self):
        """Test NewSubscriptionItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
