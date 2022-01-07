# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.23.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pollination_sdk
from pollination_sdk.models.subject_type import SubjectType  # noqa: E501
from pollination_sdk.rest import ApiException

class TestSubjectType(unittest.TestCase):
    """SubjectType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubjectType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pollination_sdk.models.subject_type.SubjectType()  # noqa: E501
        if include_optional :
            return SubjectType(
            )
        else :
            return SubjectType(
        )

    def testSubjectType(self):
        """Test SubjectType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
