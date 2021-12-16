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
from pollination_sdk.models.coupon_duration import CouponDuration  # noqa: E501
from pollination_sdk.rest import ApiException

class TestCouponDuration(unittest.TestCase):
    """CouponDuration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CouponDuration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.coupon_duration.CouponDuration()  # noqa: E501
        if include_optional :
            return CouponDuration(
            )
        else :
            return CouponDuration(
        )

    def testCouponDuration(self):
        """Test CouponDuration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()