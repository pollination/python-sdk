# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.31.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.application_version_list import ApplicationVersionList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestApplicationVersionList(unittest.TestCase):
    """ApplicationVersionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationVersionList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.application_version_list.ApplicationVersionList()  # noqa: E501
        if include_optional :
            return ApplicationVersionList(
                next_page = 56, 
                page = 56, 
                page_count = 56, 
                per_page = 56, 
                resources = [
                    pollination_sdk.models.application_version.ApplicationVersion(
                        author = null, 
                        build_status = null, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '0', 
                        release_notes = '0', 
                        tag = '0', )
                    ], 
                total_count = 56
            )
        else :
            return ApplicationVersionList(
                page = 56,
                page_count = 56,
                per_page = 56,
                resources = [
                    pollination_sdk.models.application_version.ApplicationVersion(
                        author = null, 
                        build_status = null, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '0', 
                        release_notes = '0', 
                        tag = '0', )
                    ],
                total_count = 56,
        )

    def testApplicationVersionList(self):
        """Test ApplicationVersionList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
