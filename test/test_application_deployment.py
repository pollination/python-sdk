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
from pollination_sdk.models.application_deployment import ApplicationDeployment  # noqa: E501
from pollination_sdk.rest import ApiException

class TestApplicationDeployment(unittest.TestCase):
    """ApplicationDeployment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationDeployment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.application_deployment.ApplicationDeployment()  # noqa: E501
        if include_optional :
            return ApplicationDeployment(
                author = null, 
                ready = True, 
                url = '0', 
                version = null
            )
        else :
            return ApplicationDeployment(
                author = null,
                ready = True,
                url = '0',
                version = null,
        )

    def testApplicationDeployment(self):
        """Test ApplicationDeployment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
