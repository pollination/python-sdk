# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: v0.9.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.simulation_output_source import SimulationOutputSource  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSimulationOutputSource(unittest.TestCase):
    """SimulationOutputSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SimulationOutputSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.simulation_output_source.SimulationOutputSource()  # noqa: E501
        if include_optional :
            return SimulationOutputSource(
                output = '0', 
                path = '0', 
                simulation = '0', 
                type = 'simulation'
            )
        else :
            return SimulationOutputSource(
                simulation = '0',
        )

    def testSimulationOutputSource(self):
        """Test SimulationOutputSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
