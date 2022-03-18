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

import pollination_sdk
from pollination_sdk.api.artifacts_api import ArtifactsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestArtifactsApi(unittest.TestCase):
    """ArtifactsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.artifacts_api.ArtifactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_artifact(self):
        """Test case for create_artifact

        Get an Artifact upload link.  # noqa: E501
        """
        pass

    def test_delete_artifact(self):
        """Test case for delete_artifact

        Delete one or many artifacts by key/prefix  # noqa: E501
        """
        pass

    def test_download_artifact(self):
        """Test case for download_artifact

        Download an artifact from the project folder  # noqa: E501
        """
        pass

    def test_list_artifacts(self):
        """Test case for list_artifacts

        List artifacts in a project folder  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
