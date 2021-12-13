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
from pollination_sdk.models.subscription_update import SubscriptionUpdate  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSubscriptionUpdate(unittest.TestCase):
    """SubscriptionUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.subscription_update.SubscriptionUpdate()  # noqa: E501
        if include_optional :
            return SubscriptionUpdate(
                to_add = [
                    pollination_sdk.models.new_subscription_item.NewSubscriptionItem(
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
                        quantity = 56, )
                    ], 
                to_delete = [
                    pollination_sdk.models.subscription_item.SubscriptionItem(
                        id = '0', 
                        metadata = pollination_sdk.models.metadata.Metadata(), 
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
                        quantity = 56, )
                    ], 
                to_subscribe = null, 
                to_update = [
                    pollination_sdk.models.subscription_item.SubscriptionItem(
                        id = '0', 
                        metadata = pollination_sdk.models.metadata.Metadata(), 
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
                        quantity = 56, )
                    ]
            )
        else :
            return SubscriptionUpdate(
        )

    def testSubscriptionUpdate(self):
        """Test SubscriptionUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()