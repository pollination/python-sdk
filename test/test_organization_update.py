# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.12.4
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.organization_update import OrganizationUpdate  # noqa: E501
from pollination_sdk.rest import ApiException

class TestOrganizationUpdate(unittest.TestCase):
    """OrganizationUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrganizationUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.organization_update.OrganizationUpdate()  # noqa: E501
        if include_optional :
            return OrganizationUpdate(
                contact_email = 'info@ladybug.tools', 
                description = 'Making environmental design knowledge and tools freely accessible to every person, project and design process', 
                name = 'Ladybug Tools', 
                picture_url = 'https://avatars1.githubusercontent.com/u/38131342'
            )
        else :
            return OrganizationUpdate(
        )

    def testOrganizationUpdate(self):
        """Test OrganizationUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
