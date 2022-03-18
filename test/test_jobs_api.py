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
from pollination_sdk.api.jobs_api import JobsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.jobs_api.JobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_job(self):
        """Test case for cancel_job

        Cancel a Job  # noqa: E501
        """
        pass

    def test_create_job(self):
        """Test case for create_job

        Schedule a job  # noqa: E501
        """
        pass

    def test_delete_job(self):
        """Test case for delete_job

        Delete a Job  # noqa: E501
        """
        pass

    def test_download_job_artifact(self):
        """Test case for download_job_artifact

        Download an artifact from the job folder  # noqa: E501
        """
        pass

    def test_get_job(self):
        """Test case for get_job

        Get a Job  # noqa: E501
        """
        pass

    def test_list_jobs(self):
        """Test case for list_jobs

        List Jobs  # noqa: E501
        """
        pass

    def test_search_job_folder(self):
        """Test case for search_job_folder

        List files/folders in a job folder  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
