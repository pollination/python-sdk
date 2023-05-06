# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.39.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.runs_api import RunsApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestRunsApi(unittest.TestCase):
    """RunsApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.runs_api.RunsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_run(self):
        """Test case for cancel_run

        Cancel a run  # noqa: E501
        """
        pass

    def test_download_run_artifact(self):
        """Test case for download_run_artifact

        Download an artifact from the run folder  # noqa: E501
        """
        pass

    def test_get_all_run_steps(self):
        """Test case for get_all_run_steps

        Query the steps of a run  # noqa: E501
        """
        pass

    def test_get_run(self):
        """Test case for get_run

        Get a Run  # noqa: E501
        """
        pass

    def test_get_run_output(self):
        """Test case for get_run_output

        Get run output by name  # noqa: E501
        """
        pass

    def test_get_run_step_logs(self):
        """Test case for get_run_step_logs

        Get the logs of a specific step of the run  # noqa: E501
        """
        pass

    def test_get_run_steps(self):
        """Test case for get_run_steps

        Query the steps of a run  # noqa: E501
        """
        pass

    def test_list_run_artifacts(self):
        """Test case for list_run_artifacts

        List artifacts in a run folder  # noqa: E501
        """
        pass

    def test_list_runs(self):
        """Test case for list_runs

        List runs  # noqa: E501
        """
        pass

    def test_query_results(self):
        """Test case for query_results

        Query run results  # noqa: E501
        """
        pass

    def test_retry_run(self):
        """Test case for retry_run

        Retry a run  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
