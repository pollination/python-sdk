# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.28.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.repository_index import RepositoryIndex  # noqa: E501
from pollination_sdk.rest import ApiException

class TestRepositoryIndex(unittest.TestCase):
    """RepositoryIndex unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RepositoryIndex
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.repository_index.RepositoryIndex()  # noqa: E501
        if include_optional :
            return RepositoryIndex(
                annotations = {
                    'key' : '0'
                    }, 
                api_version = 'v1beta1', 
                generated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                metadata = null, 
                plugin = {
                    'key' : [
                        pollination_sdk.models.package_version.PackageVersion(
                            annotations = {
                                'key' : '0'
                                }, 
                            app_version = '0', 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deprecated = True, 
                            description = '0', 
                            digest = '0', 
                            home = '0', 
                            icon = '0', 
                            keywords = [
                                '0'
                                ], 
                            kind = '0', 
                            license = null, 
                            maintainers = [
                                pollination_sdk.models.maintainer.Maintainer(
                                    annotations = {
                                        'key' : '0'
                                        }, 
                                    email = '0', 
                                    name = '0', 
                                    type = 'Maintainer', )
                                ], 
                            manifest = null, 
                            name = '0', 
                            readme = '0', 
                            slug = '0', 
                            sources = [
                                '0'
                                ], 
                            tag = '0', 
                            type = 'PackageVersion', 
                            url = '0', )
                        ]
                    }, 
                recipe = {
                    'key' : [
                        pollination_sdk.models.package_version.PackageVersion(
                            annotations = {
                                'key' : '0'
                                }, 
                            app_version = '0', 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deprecated = True, 
                            description = '0', 
                            digest = '0', 
                            home = '0', 
                            icon = '0', 
                            keywords = [
                                '0'
                                ], 
                            kind = '0', 
                            license = null, 
                            maintainers = [
                                pollination_sdk.models.maintainer.Maintainer(
                                    annotations = {
                                        'key' : '0'
                                        }, 
                                    email = '0', 
                                    name = '0', 
                                    type = 'Maintainer', )
                                ], 
                            manifest = null, 
                            name = '0', 
                            readme = '0', 
                            slug = '0', 
                            sources = [
                                '0'
                                ], 
                            tag = '0', 
                            type = 'PackageVersion', 
                            url = '0', )
                        ]
                    }, 
                type = 'RepositoryIndex'
            )
        else :
            return RepositoryIndex(
        )

    def testRepositoryIndex(self):
        """Test RepositoryIndex"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
