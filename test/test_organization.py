# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: v0.17.0-staging
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.organization import Organization  # noqa: E501
from pollination_sdk.rest import ApiException

class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Organization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.organization.Organization()  # noqa: E501
        if include_optional :
            return Organization(
                account_name = 'ladybug-tools', 
                contact_email = 'info@ladybug.tools', 
                description = 'Making environmental design knowledge and tools freely accessible to every person, project and design process', 
                id = '1eb8e60d-771d-4a30-8078-fe553eb2f0bc', 
                member_count = 10, 
                name = 'Ladybug Tools', 
                owner = {"id":"e4d0d922-2031-4b39-94d2-aa6d584d6bb2","name":"ladybug-tools","type":"org"}, 
                picture_url = 'https://avatars1.githubusercontent.com/u/38131342', 
                role = member, 
                team_count = 3
            )
        else :
            return Organization(
                id = '1eb8e60d-771d-4a30-8078-fe553eb2f0bc',
                owner = {"id":"e4d0d922-2031-4b39-94d2-aa6d584d6bb2","name":"ladybug-tools","type":"org"},
        )

    def testOrganization(self):
        """Test Organization"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
