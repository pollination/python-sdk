# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.18
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.team_update import TeamUpdate  # noqa: E501
from pollination_sdk.rest import ApiException

class TestTeamUpdate(unittest.TestCase):
    """TeamUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TeamUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.team_update.TeamUpdate()  # noqa: E501
        if include_optional :
            return TeamUpdate(
                description = 'The Honeybee team works on all things energy modelling', 
                name = 'Honeybee Contributors'
            )
        else :
            return TeamUpdate(
                name = 'Honeybee Contributors',
        )

    def testTeamUpdate(self):
        """Test TeamUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
