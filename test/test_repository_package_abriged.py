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
from pollination_sdk.models.repository_package_abriged import RepositoryPackageAbriged  # noqa: E501
from pollination_sdk.rest import ApiException

class TestRepositoryPackageAbriged(unittest.TestCase):
    """RepositoryPackageAbriged unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RepositoryPackageAbriged
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.repository_package_abriged.RepositoryPackageAbriged()  # noqa: E501
        if include_optional :
            return RepositoryPackageAbriged(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                description = '0', 
                digest = '0', 
                icon = '0', 
                keywords = [
                    '0'
                    ], 
                tag = '0'
            )
        else :
            return RepositoryPackageAbriged(
                digest = '0',
                tag = '0',
        )

    def testRepositoryPackageAbriged(self):
        """Test RepositoryPackageAbriged"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
