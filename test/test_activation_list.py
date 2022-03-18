# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.28.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.activation_list import ActivationList  # noqa: E501
from pollination_sdk.rest import ApiException

class TestActivationList(unittest.TestCase):
    """ActivationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ActivationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.activation_list.ActivationList()  # noqa: E501
        if include_optional :
            return ActivationList(
                resources = [
                    pollination_sdk.models.activation.Activation(
                        app_version = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        hostname = '0', 
                        id = '0', 
                        last_synced_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        lease_expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        license_id = '0', 
                        location = pollination_sdk.models.location.Location(
                            city = '0', 
                            country_code = '0', 
                            country_name = '0', 
                            ip_address = '0', 
                            latitude = 1.337, 
                            longitude = 1.337, ), 
                        metadata = [
                            pollination_sdk.models.metadata.Metadata(
                                id = '0', 
                                key = '0', 
                                value = '0', 
                                visible = True, )
                            ], 
                        offline = True, 
                        os = '0', 
                        os_version = '0', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user = null, )
                    ]
            )
        else :
            return ActivationList(
                resources = [
                    pollination_sdk.models.activation.Activation(
                        app_version = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        hostname = '0', 
                        id = '0', 
                        last_synced_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        lease_expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        license_id = '0', 
                        location = pollination_sdk.models.location.Location(
                            city = '0', 
                            country_code = '0', 
                            country_name = '0', 
                            ip_address = '0', 
                            latitude = 1.337, 
                            longitude = 1.337, ), 
                        metadata = [
                            pollination_sdk.models.metadata.Metadata(
                                id = '0', 
                                key = '0', 
                                value = '0', 
                                visible = True, )
                            ], 
                        offline = True, 
                        os = '0', 
                        os_version = '0', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user = null, )
                    ],
        )

    def testActivationList(self):
        """Test ActivationList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
