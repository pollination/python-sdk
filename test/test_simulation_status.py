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
from pollination_sdk.models.simulation_status import SimulationStatus  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSimulationStatus(unittest.TestCase):
    """SimulationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SimulationStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.simulation_status.SimulationStatus()  # noqa: E501
        if include_optional :
            return SimulationStatus(
                account_id = null, 
                entrypoint = null, 
                finished_at = null, 
                id = null, 
                message = null, 
                parallelism = null, 
                project_id = null, 
                recipe_account_id = null, 
                recipe_id = null, 
                recipe_package_id = null, 
                started_at = null, 
                status = null, 
                tasks = null
            )
        else :
            return SimulationStatus(
                account_id = null,
                id = null,
                project_id = null,
                recipe_account_id = null,
                recipe_id = null,
                recipe_package_id = null,
                started_at = null,
                status = null,
        )

    def testSimulationStatus(self):
        """Test SimulationStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
