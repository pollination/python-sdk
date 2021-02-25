# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.teams_api import TeamsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.teams_api.TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_team(self):
        """Test case for create_team

        Create a Team  # noqa: E501
        """
        pass

    def test_delete_org_team_member(self):
        """Test case for delete_org_team_member

        Remove a team member  # noqa: E501
        """
        pass

    def test_delete_team(self):
        """Test case for delete_team

        Delete a Team  # noqa: E501
        """
        pass

    def test_get_org_team_members(self):
        """Test case for get_org_team_members

        List team members  # noqa: E501
        """
        pass

    def test_get_team(self):
        """Test case for get_team

        Get a Team  # noqa: E501
        """
        pass

    def test_list_org_teams(self):
        """Test case for list_org_teams

        List Teams  # noqa: E501
        """
        pass

    def test_update_team(self):
        """Test case for update_team

        Update a Team  # noqa: E501
        """
        pass

    def test_upsert_org_team_member(self):
        """Test case for upsert_org_team_member

        Add or update the role of an Team Member  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
