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
from pollination_sdk.models.card import Card  # noqa: E501
from pollination_sdk.rest import ApiException

class TestCard(unittest.TestCase):
    """Card unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Card
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.card.Card()  # noqa: E501
        if include_optional :
            return Card(
                brand = '0', 
                country = '0', 
                exp_month = 56, 
                exp_year = 56, 
                last4 = '0', 
                networks = pollination_sdk.models.networks.Networks()
            )
        else :
            return Card(
                brand = '0',
                country = '0',
                exp_month = 56,
                exp_year = 56,
                last4 = '0',
                networks = pollination_sdk.models.networks.Networks(),
        )

    def testCard(self):
        """Test Card"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
