# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.37.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class BuildStatus(object):
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
        'created_at': 'datetime',
        'finished_at': 'datetime',
        'started_at': 'datetime',
        'status': 'BuildStatusEnum'
    }

    attribute_map = {
        'created_at': 'created_at',
        'finished_at': 'finished_at',
        'started_at': 'started_at',
        'status': 'status'
    }

    def __init__(self, created_at=None, finished_at=None, started_at=None, status=None, local_vars_configuration=None):  # noqa: E501
        """BuildStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._finished_at = None
        self._started_at = None
        self._status = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if finished_at is not None:
            self.finished_at = finished_at
        if started_at is not None:
            self.started_at = started_at
        self.status = status

    @property
    def created_at(self):
        """Gets the created_at of this BuildStatus.  # noqa: E501

        The date and time the build was created  # noqa: E501

        :return: The created_at of this BuildStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BuildStatus.

        The date and time the build was created  # noqa: E501

        :param created_at: The created_at of this BuildStatus.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def finished_at(self):
        """Gets the finished_at of this BuildStatus.  # noqa: E501

        The date and time the build finished  # noqa: E501

        :return: The finished_at of this BuildStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this BuildStatus.

        The date and time the build finished  # noqa: E501

        :param finished_at: The finished_at of this BuildStatus.  # noqa: E501
        :type finished_at: datetime
        """

        self._finished_at = finished_at

    @property
    def started_at(self):
        """Gets the started_at of this BuildStatus.  # noqa: E501

        The date and time the build started  # noqa: E501

        :return: The started_at of this BuildStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this BuildStatus.

        The date and time the build started  # noqa: E501

        :param started_at: The started_at of this BuildStatus.  # noqa: E501
        :type started_at: datetime
        """

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this BuildStatus.  # noqa: E501

        The status of the build  # noqa: E501

        :return: The status of this BuildStatus.  # noqa: E501
        :rtype: BuildStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BuildStatus.

        The status of the build  # noqa: E501

        :param status: The status of this BuildStatus.  # noqa: E501
        :type status: BuildStatusEnum
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, BuildStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BuildStatus):
            return True

        return self.to_dict() != other.to_dict()
