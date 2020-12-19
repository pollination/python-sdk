# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.14
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.repository import Repository  # noqa: E501
from pollination_sdk.rest import ApiException

class TestRepository(unittest.TestCase):
    """Repository unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Repository
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.repository.Repository()  # noqa: E501
        if include_optional :
            return Repository(
                description = 'Run daylight simulations the easy way!', 
                icon = 'https://avatars1.githubusercontent.com/u/38131342', 
                id = '5d5e7103-2c1e-413f-9332-f8ec4a9aace7', 
                keywords = ["daylight","radiance"], 
                latest_tag = '0.2.1', 
                name = 'daylight-factor', 
                owner = null, 
                permissions = null, 
                public = True, 
                slug = 'ladybug-tools/daylight-factor'
            )
        else :
            return Repository(
                id = '5d5e7103-2c1e-413f-9332-f8ec4a9aace7',
                latest_tag = '0.2.1',
                name = 'daylight-factor',
                owner = null,
        )

    def testRepository(self):
        """Test Repository"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
