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
from pollination_sdk.models.subscription_update_dry_run import SubscriptionUpdateDryRun  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSubscriptionUpdateDryRun(unittest.TestCase):
    """SubscriptionUpdateDryRun unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionUpdateDryRun
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.subscription_update_dry_run.SubscriptionUpdateDryRun()  # noqa: E501
        if include_optional :
            return SubscriptionUpdateDryRun(
                exceeded_quotas = [
                    pollination_sdk.models.quota.Quota(
                        description = '0', 
                        display_name = '0', 
                        enforced = True, 
                        exceeded = True, 
                        id = '0', 
                        limit = 1.337, 
                        owner = null, 
                        period_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        resets = True, 
                        type = null, 
                        unit = '0', 
                        usage = 0.0, )
                    ]
            )
        else :
            return SubscriptionUpdateDryRun(
        )

    def testSubscriptionUpdateDryRun(self):
        """Test SubscriptionUpdateDryRun"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
