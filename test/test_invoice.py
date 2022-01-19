# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.25.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.invoice import Invoice  # noqa: E501
from pollination_sdk.rest import ApiException

class TestInvoice(unittest.TestCase):
    """Invoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Invoice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.invoice.Invoice()  # noqa: E501
        if include_optional :
            return Invoice(
                auto_advance = True, 
                collection_method = '0', 
                currency = '0', 
                customer = '0', 
                description = '0', 
                discount = pollination_sdk.models.discount.Discount(
                    coupon = pollination_sdk.models.coupon.Coupon(
                        amount_off = 1.337, 
                        duration = 'forever', 
                        duration_in_months = 56, 
                        id = '0', 
                        metadata = pollination_sdk.models.metadata.Metadata(), 
                        name = '0', 
                        percent_off = 1.337, 
                        valid = True, ), 
                    end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '0', 
                    metadata = pollination_sdk.models.metadata.Metadata(), 
                    promotion_code = '0', 
                    start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                hosted_invoice_url = '0', 
                id = '0', 
                lines = pollination_sdk.models.line_item_list.LineItemList(
                    data = [
                        pollination_sdk.models.line_item.LineItem(
                            amount = 56, 
                            currency = '0', 
                            description = '0', 
                            id = '0', 
                            metadata = pollination_sdk.models.metadata.Metadata(), 
                            period = pollination_sdk.models.period.Period(
                                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
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
                            proration = True, 
                            quantity = 56, 
                            type = '0', )
                        ], 
                    has_more = True, ), 
                metadata = pollination_sdk.models.metadata.Metadata(), 
                period_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                period_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = 'draft', 
                status_transitions = pollination_sdk.models.invoice_status_transitions.InvoiceStatusTransitions(
                    finalized_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    marked_uncollectible_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    paid_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    voided_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                subscription = '0', 
                subtotal = 56, 
                tax = 56, 
                total = 56, 
                total_discount_amounts = [
                    pollination_sdk.models.discount_amount.DiscountAmount(
                        amount = 56, 
                        discount = '0', )
                    ], 
                total_tax_amounts = [
                    pollination_sdk.models.tax_amount.TaxAmount(
                        amount = 56, 
                        inclusive = True, 
                        tax_rate = '0', )
                    ]
            )
        else :
            return Invoice(
                collection_method = '0',
                currency = '0',
                customer = '0',
                id = '0',
                lines = pollination_sdk.models.line_item_list.LineItemList(
                    data = [
                        pollination_sdk.models.line_item.LineItem(
                            amount = 56, 
                            currency = '0', 
                            description = '0', 
                            id = '0', 
                            metadata = pollination_sdk.models.metadata.Metadata(), 
                            period = pollination_sdk.models.period.Period(
                                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
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
                            proration = True, 
                            quantity = 56, 
                            type = '0', )
                        ], 
                    has_more = True, ),
                period_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                period_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'draft',
                status_transitions = pollination_sdk.models.invoice_status_transitions.InvoiceStatusTransitions(
                    finalized_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    marked_uncollectible_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    paid_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    voided_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                subtotal = 56,
                total = 56,
        )

    def testInvoice(self):
        """Test Invoice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
