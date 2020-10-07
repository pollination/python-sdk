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
from pollination_sdk.models.team_list import TeamList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestTeamList(unittest.TestCase):
    """TeamList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TeamList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.team_list.TeamList()  # noqa: E501
        if include_optional :
            return TeamList(
                next_page = null, 
                page = null, 
                page_count = null, 
                per_page = null, 
                resources = null, 
                total_count = null
            )
        else :
            return TeamList(
                page = null,
                page_count = null,
                per_page = null,
                resources = null,
                total_count = null,
        )

    def testTeamList(self):
        """Test TeamList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
