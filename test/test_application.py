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
from pollination_sdk.models.application import Application  # noqa: E501
from pollination_sdk.rest import ApiException

class TestApplication(unittest.TestCase):
    """Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Application
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.application.Application()  # noqa: E501
        if include_optional :
            return Application(
                description = '0', 
                id = '50bb7fe0-8f19-499e-972e-1ebec8af2c71', 
                name = 'Application Falcon', 
                owner = null, 
                permissions = pollination_sdk.models.user_permission.UserPermission(
                    admin = False, 
                    read = True, 
                    write = False, ), 
                public = True, 
                slug = 'application-falcon'
            )
        else :
            return Application(
                id = '50bb7fe0-8f19-499e-972e-1ebec8af2c71',
                name = 'Application Falcon',
                owner = null,
                permissions = pollination_sdk.models.user_permission.UserPermission(
                    admin = False, 
                    read = True, 
                    write = False, ),
                slug = 'application-falcon',
        )

    def testApplication(self):
        """Test Application"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
