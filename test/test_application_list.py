# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.43.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.application_list import ApplicationList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestApplicationList(unittest.TestCase):
    """ApplicationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.application_list.ApplicationList()  # noqa: E501
        if include_optional :
            return ApplicationList(
                next_page = 56, 
                page = 56, 
                page_count = 56, 
                per_page = 56, 
                resources = [
                    pollination_sdk.models.application.Application(
                        deployment_config = null, 
                        description = '0', 
                        id = '50bb7fe0-8f19-499e-972e-1ebec8af2c71', 
                        image = 'https://picsum.photos/400', 
                        is_paid = True, 
                        keywords = ["falcon","api"], 
                        license = '0', 
                        name = 'Application Falcon', 
                        owner = null, 
                        permissions = pollination_sdk.models.user_permission.UserPermission(
                            admin = False, 
                            read = True, 
                            write = False, ), 
                        public = True, 
                        sdk = null, 
                        slug = 'application-falcon', 
                        source = '0', )
                    ], 
                total_count = 56
            )
        else :
            return ApplicationList(
                page = 56,
                page_count = 56,
                per_page = 56,
                resources = [
                    pollination_sdk.models.application.Application(
                        deployment_config = null, 
                        description = '0', 
                        id = '50bb7fe0-8f19-499e-972e-1ebec8af2c71', 
                        image = 'https://picsum.photos/400', 
                        is_paid = True, 
                        keywords = ["falcon","api"], 
                        license = '0', 
                        name = 'Application Falcon', 
                        owner = null, 
                        permissions = pollination_sdk.models.user_permission.UserPermission(
                            admin = False, 
                            read = True, 
                            write = False, ), 
                        public = True, 
                        sdk = null, 
                        slug = 'application-falcon', 
                        source = '0', )
                    ],
                total_count = 56,
        )

    def testApplicationList(self):
        """Test ApplicationList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
