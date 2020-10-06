# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: v0.9.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.submit_simulation import SubmitSimulation  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSubmitSimulation(unittest.TestCase):
    """SubmitSimulation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubmitSimulation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.submit_simulation.SubmitSimulation()  # noqa: E501
        if include_optional :
            return SubmitSimulation(
                inputs = {"artifacts":[{"name":"model","source":{"path":"path/to/model.hbjson","type":"project-folder"}}],"parameters":[{"name":"bounces","value":5}]}, 
                recipe = null
            )
        else :
            return SubmitSimulation(
                recipe = null,
        )

    def testSubmitSimulation(self):
        """Test SubmitSimulation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
