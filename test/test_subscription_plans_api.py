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

import pollination_sdk
from pollination_sdk.api.subscription_plans_api import SubscriptionPlansApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestSubscriptionPlansApi(unittest.TestCase):
    """SubscriptionPlansApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.subscription_plans_api.SubscriptionPlansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_subscription_plans(self):
        """Test case for list_subscription_plans

        List Subscription Plans  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
