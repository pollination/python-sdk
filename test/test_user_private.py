# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.user_private import UserPrivate  # noqa: E501
from pollination_sdk.rest import ApiException

class TestUserPrivate(unittest.TestCase):
    """UserPrivate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserPrivate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.user_private.UserPrivate()  # noqa: E501
        if include_optional :
            return UserPrivate(
                description = 'Beep Boop!', 
                email = 'ladybugbot@ladybug.tools', 
                id = '96c12d05-f1a2-4491-b0cc-c2ed473301b5', 
                name = 'Ladybug Bot', 
                picture = 'https://avatars1.githubusercontent.com/u/38131342', 
                username = 'ladybugbot'
            )
        else :
            return UserPrivate(
                email = 'ladybugbot@ladybug.tools',
                id = '96c12d05-f1a2-4491-b0cc-c2ed473301b5',
                username = 'ladybugbot',
        )

    def testUserPrivate(self):
        """Test UserPrivate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
