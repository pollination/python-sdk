# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.26.3
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.license_pool_list import LicensePoolList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestLicensePoolList(unittest.TestCase):
    """LicensePoolList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LicensePoolList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.license_pool_list.LicensePoolList()  # noqa: E501
        if include_optional :
            return LicensePoolList(
                resources = [
                    pollination_sdk.models.license_pool_public.LicensePoolPublic(
                        accessors = [
                            pollination_sdk.models.accessor.Accessor(
                                permission = 'admin', 
                                subject = null, )
                            ], 
                        allowed_activations = 56, 
                        description = '0', 
                        id = '0', 
                        license_id = '0', 
                        owner = null, 
                        permissions = pollination_sdk.models.user_permission.UserPermission(
                            admin = False, 
                            read = True, 
                            write = False, ), 
                        product = '0', 
                        total_activations = 56, )
                    ]
            )
        else :
            return LicensePoolList(
                resources = [
                    pollination_sdk.models.license_pool_public.LicensePoolPublic(
                        accessors = [
                            pollination_sdk.models.accessor.Accessor(
                                permission = 'admin', 
                                subject = null, )
                            ], 
                        allowed_activations = 56, 
                        description = '0', 
                        id = '0', 
                        license_id = '0', 
                        owner = null, 
                        permissions = pollination_sdk.models.user_permission.UserPermission(
                            admin = False, 
                            read = True, 
                            write = False, ), 
                        product = '0', 
                        total_activations = 56, )
                    ],
        )

    def testLicensePoolList(self):
        """Test LicensePoolList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
