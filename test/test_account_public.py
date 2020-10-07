# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.9.2
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.account_public import AccountPublic  # noqa: E501
from pollination_sdk.rest import ApiException

class TestAccountPublic(unittest.TestCase):
    """AccountPublic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountPublic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.account_public.AccountPublic()  # noqa: E501
        if include_optional :
            return AccountPublic(
                id = 0ad77f99-8043-46e4-8220-7221487c3ee5, 
                name = LadybugBot, 
                type = user
            )
        else :
            return AccountPublic(
                id = 0ad77f99-8043-46e4-8220-7221487c3ee5,
                name = LadybugBot,
                type = user,
        )

    def testAccountPublic(self):
        """Test AccountPublic"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
