# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.38.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.subscriptions_api import SubscriptionsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestSubscriptionsApi(unittest.TestCase):
    """SubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.subscriptions_api.SubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_subscription(self):
        """Test case for cancel_subscription

        Cancel a subscription  # noqa: E501
        """
        pass

    def test_create_subscription(self):
        """Test case for create_subscription

        Subscribe account to subscritpion plan  # noqa: E501
        """
        pass

    def test_get_subscription(self):
        """Test case for get_subscription

        Retrieve a subscription by ID  # noqa: E501
        """
        pass

    def test_list_pollination_subscriptions(self):
        """Test case for list_pollination_subscriptions

        List Subscriptions  # noqa: E501
        """
        pass

    def test_list_subscription_payments(self):
        """Test case for list_subscription_payments

        List Payment for a Subscription  # noqa: E501
        """
        pass

    def test_list_subscription_quotas(self):
        """Test case for list_subscription_quotas

        List the quotas for a given subscription  # noqa: E501
        """
        pass

    def test_update_subscription(self):
        """Test case for update_subscription

        Update a subscription  # noqa: E501
        """
        pass

    def test_update_subscription_preivew(self):
        """Test case for update_subscription_preivew

        Preview the effect of a subscription update  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
