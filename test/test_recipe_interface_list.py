# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.39.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.recipe_interface_list import RecipeInterfaceList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestRecipeInterfaceList(unittest.TestCase):
    """RecipeInterfaceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RecipeInterfaceList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.recipe_interface_list.RecipeInterfaceList()  # noqa: E501
        if include_optional :
            return RecipeInterfaceList(
                next_page = 56, 
                page = 56, 
                page_count = 56, 
                per_page = 56, 
                resources = [
                    pollination_sdk.models.recipe_interface.RecipeInterface(
                        annotations = {
                            'key' : '0'
                            }, 
                        api_version = 'v1beta1', 
                        inputs = [
                            null
                            ], 
                        metadata = null, 
                        outputs = [
                            null
                            ], 
                        source = '0', 
                        type = 'RecipeInterface', )
                    ], 
                total_count = 56
            )
        else :
            return RecipeInterfaceList(
                page = 56,
                page_count = 56,
                per_page = 56,
                resources = [
                    pollination_sdk.models.recipe_interface.RecipeInterface(
                        annotations = {
                            'key' : '0'
                            }, 
                        api_version = 'v1beta1', 
                        inputs = [
                            null
                            ], 
                        metadata = null, 
                        outputs = [
                            null
                            ], 
                        source = '0', 
                        type = 'RecipeInterface', )
                    ],
                total_count = 56,
        )

    def testRecipeInterfaceList(self):
        """Test RecipeInterfaceList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
