# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.new_repository_dto import NewRepositoryDto  # noqa: E501
from pollination_sdk.rest import ApiException

class TestNewRepositoryDto(unittest.TestCase):
    """NewRepositoryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewRepositoryDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.new_repository_dto.NewRepositoryDto()  # noqa: E501
        if include_optional :
            return NewRepositoryDto(
                description = '0', 
                icon = '0', 
                keywords = [
                    '0'
                    ], 
                name = '0', 
                public = True
            )
        else :
            return NewRepositoryDto(
                name = '0',
        )

    def testNewRepositoryDto(self):
        """Test NewRepositoryDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
