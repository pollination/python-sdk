# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.27.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.quota_list import QuotaList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestQuotaList(unittest.TestCase):
    """QuotaList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test QuotaList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.quota_list.QuotaList()  # noqa: E501
        if include_optional :
            return QuotaList(
                next_page = 56, 
                page = 56, 
                page_count = 56, 
                per_page = 56, 
                resources = [
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
                    ], 
                total_count = 56
            )
        else :
            return QuotaList(
                page = 56,
                page_count = 56,
                per_page = 56,
                resources = [
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
                    ],
                total_count = 56,
        )

    def testQuotaList(self):
        """Test QuotaList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
