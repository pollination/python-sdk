# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.23.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.recipes_api import RecipesApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestRecipesApi(unittest.TestCase):
    """RecipesApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.recipes_api.RecipesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_recipe(self):
        """Test case for create_recipe

        Create a Recipe  # noqa: E501
        """
        pass

    def test_create_recipe_package(self):
        """Test case for create_recipe_package

        Create a new Recipe package  # noqa: E501
        """
        pass

    def test_delete_recipe(self):
        """Test case for delete_recipe

        Delete a Recipe  # noqa: E501
        """
        pass

    def test_delete_recipe_org_permission(self):
        """Test case for delete_recipe_org_permission

        Remove a Repository permissions  # noqa: E501
        """
        pass

    def test_get_recipe(self):
        """Test case for get_recipe

        Get a recipe  # noqa: E501
        """
        pass

    def test_get_recipe_access_permissions(self):
        """Test case for get_recipe_access_permissions

        Get recipe access permissions  # noqa: E501
        """
        pass

    def test_get_recipe_by_tag(self):
        """Test case for get_recipe_by_tag

        Get a recipe tag  # noqa: E501
        """
        pass

    def test_list_recipe_tags(self):
        """Test case for list_recipe_tags

        Get a recipe tags  # noqa: E501
        """
        pass

    def test_list_recipes(self):
        """Test case for list_recipes

        List recipes  # noqa: E501
        """
        pass

    def test_update_recipe(self):
        """Test case for update_recipe

        Update a Recipe  # noqa: E501
        """
        pass

    def test_upsert_recipe_permission(self):
        """Test case for upsert_recipe_permission

        Upsert a new permission to a recipe  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
