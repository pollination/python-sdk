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
from pollination_sdk.models.tax_amount import TaxAmount  # noqa: E501
from pollination_sdk.rest import ApiException

class TestTaxAmount(unittest.TestCase):
    """TaxAmount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaxAmount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.tax_amount.TaxAmount()  # noqa: E501
        if include_optional :
            return TaxAmount(
                amount = 56, 
                inclusive = True, 
                tax_rate = '0'
            )
        else :
            return TaxAmount(
                amount = 56,
                inclusive = True,
                tax_rate = '0',
        )

    def testTaxAmount(self):
        """Test TaxAmount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
