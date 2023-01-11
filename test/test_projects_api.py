# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.36.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.projects_api import ProjectsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.projects_api.ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a Project  # noqa: E501
        """
        pass

    def test_create_project_recipe_filter(self):
        """Test case for create_project_recipe_filter

        Upsert a recipe filter to a project  # noqa: E501
        """
        pass

    def test_delete_project(self):
        """Test case for delete_project

        Delete a Project  # noqa: E501
        """
        pass

    def test_delete_project_org_permission(self):
        """Test case for delete_project_org_permission

        Remove a Project permissions  # noqa: E501
        """
        pass

    def test_delete_project_recipe_filter(self):
        """Test case for delete_project_recipe_filter

        Remove a Project recipe filter  # noqa: E501
        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Get a project  # noqa: E501
        """
        pass

    def test_get_project_access_permissions(self):
        """Test case for get_project_access_permissions

        Get project access permissions  # noqa: E501
        """
        pass

    def test_get_project_recipe_filters(self):
        """Test case for get_project_recipe_filters

        Get project recipe filters  # noqa: E501
        """
        pass

    def test_get_project_recipes(self):
        """Test case for get_project_recipes

        Get project recipes  # noqa: E501
        """
        pass

    def test_list_projects(self):
        """Test case for list_projects

        List Projects  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update a Project  # noqa: E501
        """
        pass

    def test_upsert_project_permission(self):
        """Test case for upsert_project_permission

        Upsert a new permission to a project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
