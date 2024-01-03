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
from pollination_sdk.models.subscription_plan import SubscriptionPlan  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSubscriptionPlan(unittest.TestCase):
    """SubscriptionPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionPlan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.subscription_plan.SubscriptionPlan()  # noqa: E501
        if include_optional :
            return SubscriptionPlan(
                account_types = [
                    'org'
                    ], 
                billing_options = [
                    pollination_sdk.models.billing_option.BillingOption(
                        billing_period = 56, 
                        billing_type = '0', 
                        id = 56, 
                        name = '0', 
                        recurring_price = {
                            'key' : 1.337
                            }, )
                    ], 
                name = '0', 
                quotas = [
                    pollination_sdk.models.quota_plan.QuotaPlan(
                        description = '0', 
                        display_name = '0', 
                        enforced = True, 
                        limit = 1.337, 
                        max_limit = 1.337, 
                        resets = True, 
                        type = null, 
                        unit = '0', )
                    ], 
                slug = '0', 
                type = null
            )
        else :
            return SubscriptionPlan(
                account_types = [
                    'org'
                    ],
                name = '0',
                slug = '0',
                type = null,
        )

    def testSubscriptionPlan(self):
        """Test SubscriptionPlan"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
