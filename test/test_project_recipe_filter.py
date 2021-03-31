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
from pollination_sdk.models.project_recipe_filter import ProjectRecipeFilter  # noqa: E501
from pollination_sdk.rest import ApiException

class TestProjectRecipeFilter(unittest.TestCase):
    """ProjectRecipeFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectRecipeFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.project_recipe_filter.ProjectRecipeFilter()  # noqa: E501
        if include_optional :
            return ProjectRecipeFilter(
                name = 'daylight-factor', 
                owner = 'ladybug-tools', 
                tag = '0.2.1'
            )
        else :
            return ProjectRecipeFilter(
                name = 'daylight-factor',
                owner = 'ladybug-tools',
        )

    def testProjectRecipeFilter(self):
        """Test ProjectRecipeFilter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
