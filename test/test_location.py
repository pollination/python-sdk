# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.42.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.location import Location  # noqa: E501
from pollination_sdk.rest import ApiException

class TestLocation(unittest.TestCase):
    """Location unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Location
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.location.Location()  # noqa: E501
        if include_optional :
            return Location(
                city = '0', 
                country_code = '0', 
                country_name = '0', 
                ip_address = '0', 
                latitude = 1.337, 
                longitude = 1.337
            )
        else :
            return Location(
        )

    def testLocation(self):
        """Test Location"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
