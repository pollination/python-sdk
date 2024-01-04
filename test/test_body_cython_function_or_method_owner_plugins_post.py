# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.body_cython_function_or_method_owner_plugins_post import BodyCythonFunctionOrMethodOwnerPluginsPost  # noqa: E501
from pollination_sdk.rest import ApiException

class TestBodyCythonFunctionOrMethodOwnerPluginsPost(unittest.TestCase):
    """BodyCythonFunctionOrMethodOwnerPluginsPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BodyCythonFunctionOrMethodOwnerPluginsPost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.body_cython_function_or_method_owner_plugins_post.BodyCythonFunctionOrMethodOwnerPluginsPost()  # noqa: E501
        if include_optional :
            return BodyCythonFunctionOrMethodOwnerPluginsPost(
                package = bytes(b'blah')
            )
        else :
            return BodyCythonFunctionOrMethodOwnerPluginsPost(
                package = bytes(b'blah'),
        )

    def testBodyCythonFunctionOrMethodOwnerPluginsPost(self):
        """Test BodyCythonFunctionOrMethodOwnerPluginsPost"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
