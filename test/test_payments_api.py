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

import pollination_sdk
from pollination_sdk.api.payments_api import PaymentsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestPaymentsApi(unittest.TestCase):
    """PaymentsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.payments_api.PaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_subscription(self):
        """Test case for cancel_subscription

        Cancel Subscription  # noqa: E501
        """
        pass

    def test_create_payment_method(self):
        """Test case for create_payment_method

        Add Payment Method  # noqa: E501
        """
        pass

    def test_create_subscription(self):
        """Test case for create_subscription

        Create Subscription  # noqa: E501
        """
        pass

    def test_get_default_payment_method(self):
        """Test case for get_default_payment_method

        Get Default Payment Method  # noqa: E501
        """
        pass

    def test_get_failed_payment(self):
        """Test case for get_failed_payment

        Get Failed Payment  # noqa: E501
        """
        pass

    def test_get_inventory(self):
        """Test case for get_inventory

        Get Inventory  # noqa: E501
        """
        pass

    def test_get_invoice_list(self):
        """Test case for get_invoice_list

        Get Invoice List  # noqa: E501
        """
        pass

    def test_get_next_invoice(self):
        """Test case for get_next_invoice

        Get Next Invoice  # noqa: E501
        """
        pass

    def test_get_status(self):
        """Test case for get_status

        Get Status  # noqa: E501
        """
        pass

    def test_get_subscription(self):
        """Test case for get_subscription

        Get Subscription  # noqa: E501
        """
        pass

    def test_get_unfiltered_inventory(self):
        """Test case for get_unfiltered_inventory

        Get Unfiltered Inventory  # noqa: E501
        """
        pass

    def test_list_payment_methods(self):
        """Test case for list_payment_methods

        Get Payment Methods  # noqa: E501
        """
        pass

    def test_preview_update_subscription(self):
        """Test case for preview_update_subscription

        Preview Update Subscription  # noqa: E501
        """
        pass

    def test_subscribe(self):
        """Test case for subscribe

        Subscribe  # noqa: E501
        """
        pass

    def test_update_subscription(self):
        """Test case for update_subscription

        Update Subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
