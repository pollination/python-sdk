# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.12.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.body_post_plugin_registries_owner_plugins_post import BodyPostPluginRegistriesOwnerPluginsPost  # noqa: E501
from pollination_sdk.rest import ApiException

class TestBodyPostPluginRegistriesOwnerPluginsPost(unittest.TestCase):
    """BodyPostPluginRegistriesOwnerPluginsPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BodyPostPluginRegistriesOwnerPluginsPost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.body_post_plugin_registries_owner_plugins_post.BodyPostPluginRegistriesOwnerPluginsPost()  # noqa: E501
        if include_optional :
            return BodyPostPluginRegistriesOwnerPluginsPost(
                package = bytes(b'blah')
            )
        else :
            return BodyPostPluginRegistriesOwnerPluginsPost(
                package = bytes(b'blah'),
        )

    def testBodyPostPluginRegistriesOwnerPluginsPost(self):
        """Test BodyPostPluginRegistriesOwnerPluginsPost"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
