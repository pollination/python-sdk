# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.25.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.recipe import Recipe  # noqa: E501
from pollination_sdk.rest import ApiException

class TestRecipe(unittest.TestCase):
    """Recipe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Recipe
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.recipe.Recipe()  # noqa: E501
        if include_optional :
            return Recipe(
                annotations = {
                    'key' : '0'
                    }, 
                api_version = 'v1beta1', 
                dependencies = [
                    pollination_sdk.models.dependency.Dependency(
                        alias = '0', 
                        annotations = {
                            'key' : '0'
                            }, 
                        hash = '0', 
                        kind = null, 
                        name = '0', 
                        source = '0', 
                        tag = '0', 
                        type = 'Dependency', )
                    ], 
                flow = [
                    pollination_sdk.models.dag.DAG(
                        annotations = {
                            'key' : '0'
                            }, 
                        fail_fast = True, 
                        inputs = [
                            null
                            ], 
                        name = '0', 
                        outputs = [
                            null
                            ], 
                        tasks = [
                            pollination_sdk.models.dag_task.DAGTask(
                                annotations = {
                                    'key' : '0'
                                    }, 
                                arguments = [
                                    null
                                    ], 
                                loop = null, 
                                name = '0', 
                                needs = [
                                    '0'
                                    ], 
                                returns = [
                                    null
                                    ], 
                                sub_folder = '0', 
                                template = '0', 
                                type = 'DAGTask', )
                            ], 
                        type = 'DAG', )
                    ], 
                metadata = null, 
                type = 'Recipe'
            )
        else :
            return Recipe(
                flow = [
                    pollination_sdk.models.dag.DAG(
                        annotations = {
                            'key' : '0'
                            }, 
                        fail_fast = True, 
                        inputs = [
                            null
                            ], 
                        name = '0', 
                        outputs = [
                            null
                            ], 
                        tasks = [
                            pollination_sdk.models.dag_task.DAGTask(
                                annotations = {
                                    'key' : '0'
                                    }, 
                                arguments = [
                                    null
                                    ], 
                                loop = null, 
                                name = '0', 
                                needs = [
                                    '0'
                                    ], 
                                returns = [
                                    null
                                    ], 
                                sub_folder = '0', 
                                template = '0', 
                                type = 'DAGTask', )
                            ], 
                        type = 'DAG', )
                    ],
        )

    def testRecipe(self):
        """Test Recipe"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
