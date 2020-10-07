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
from pollination_sdk.models.project_update import ProjectUpdate  # noqa: E501
from pollination_sdk.rest import ApiException

class TestProjectUpdate(unittest.TestCase):
    """ProjectUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.project_update.ProjectUpdate()  # noqa: E501
        if include_optional :
            return ProjectUpdate(
                description = I always wanted to have a project called project Falcon, 
                name = Project Falcon, 
                public = null
            )
        else :
            return ProjectUpdate(
                name = Project Falcon,
        )

    def testProjectUpdate(self):
        """Test ProjectUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
