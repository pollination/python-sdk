# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.11.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.public_account_list import PublicAccountList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestPublicAccountList(unittest.TestCase):
    """PublicAccountList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PublicAccountList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.public_account_list.PublicAccountList()  # noqa: E501
        if include_optional :
            return PublicAccountList(
                next_page = 56, 
                page = 56, 
                page_count = 56, 
                per_page = 56, 
                resources = [
                    pollination_sdk.models.account_public.AccountPublic(
                        account_type = 'user', 
                        description = 'Beep Boop!', 
                        display_name = 'Ladybug Bot', 
                        id = '0ad77f99-8043-46e4-8220-7221487c3ee5', 
                        name = 'ladybugbot', 
                        picture_url = '0', )
                    ], 
                total_count = 56
            )
        else :
            return PublicAccountList(
                page = 56,
                page_count = 56,
                per_page = 56,
                resources = [
                    pollination_sdk.models.account_public.AccountPublic(
                        account_type = 'user', 
                        description = 'Beep Boop!', 
                        display_name = 'Ladybug Bot', 
                        id = '0ad77f99-8043-46e4-8220-7221487c3ee5', 
                        name = 'ladybugbot', 
                        picture_url = '0', )
                    ],
                total_count = 56,
        )

    def testPublicAccountList(self):
        """Test PublicAccountList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
