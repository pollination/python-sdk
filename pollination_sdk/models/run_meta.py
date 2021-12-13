# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: v0.20.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class RunMeta(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'progress': 'RunProgress',
        'resources_duration': 'ResourcesDuration'
    }

    attribute_map = {
        'progress': 'progress',
        'resources_duration': 'resources_duration'
    }

    def __init__(self, progress=None, resources_duration=None, local_vars_configuration=None):  # noqa: E501
        """RunMeta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._progress = None
        self._resources_duration = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if resources_duration is not None:
            self.resources_duration = resources_duration

    @property
    def progress(self):
        """Gets the progress of this RunMeta.  # noqa: E501

        progress of the run  # noqa: E501

        :return: The progress of this RunMeta.  # noqa: E501
        :rtype: RunProgress
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this RunMeta.

        progress of the run  # noqa: E501

        :param progress: The progress of this RunMeta.  # noqa: E501
        :type progress: RunProgress
        """

        self._progress = progress

    @property
    def resources_duration(self):
        """Gets the resources_duration of this RunMeta.  # noqa: E501

        resource usage  # noqa: E501

        :return: The resources_duration of this RunMeta.  # noqa: E501
        :rtype: ResourcesDuration
        """
        return self._resources_duration

    @resources_duration.setter
    def resources_duration(self, resources_duration):
        """Sets the resources_duration of this RunMeta.

        resource usage  # noqa: E501

        :param resources_duration: The resources_duration of this RunMeta.  # noqa: E501
        :type resources_duration: ResourcesDuration
        """

        self._resources_duration = resources_duration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RunMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunMeta):
            return True

        return self.to_dict() != other.to_dict()
