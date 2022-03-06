# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.27.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class DailyUsage(object):
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
        'cpu': 'float',
        'date': 'datetime',
        'failed': 'int',
        'memory': 'float',
        'succeeded': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'date': 'date',
        'failed': 'failed',
        'memory': 'memory',
        'succeeded': 'succeeded'
    }

    def __init__(self, cpu=0, date=None, failed=0, memory=0, succeeded=0, local_vars_configuration=None):  # noqa: E501
        """DailyUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu = None
        self._date = None
        self._failed = None
        self._memory = None
        self._succeeded = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        self.date = date
        if failed is not None:
            self.failed = failed
        if memory is not None:
            self.memory = memory
        if succeeded is not None:
            self.succeeded = succeeded

    @property
    def cpu(self):
        """Gets the cpu of this DailyUsage.  # noqa: E501

        cpu usage  # noqa: E501

        :return: The cpu of this DailyUsage.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this DailyUsage.

        cpu usage  # noqa: E501

        :param cpu: The cpu of this DailyUsage.  # noqa: E501
        :type cpu: float
        """

        self._cpu = cpu

    @property
    def date(self):
        """Gets the date of this DailyUsage.  # noqa: E501

        The day this usage was aggregated for  # noqa: E501

        :return: The date of this DailyUsage.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DailyUsage.

        The day this usage was aggregated for  # noqa: E501

        :param date: The date of this DailyUsage.  # noqa: E501
        :type date: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def failed(self):
        """Gets the failed of this DailyUsage.  # noqa: E501

        failed usage  # noqa: E501

        :return: The failed of this DailyUsage.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this DailyUsage.

        failed usage  # noqa: E501

        :param failed: The failed of this DailyUsage.  # noqa: E501
        :type failed: int
        """

        self._failed = failed

    @property
    def memory(self):
        """Gets the memory of this DailyUsage.  # noqa: E501

        memory usage  # noqa: E501

        :return: The memory of this DailyUsage.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this DailyUsage.

        memory usage  # noqa: E501

        :param memory: The memory of this DailyUsage.  # noqa: E501
        :type memory: float
        """

        self._memory = memory

    @property
    def succeeded(self):
        """Gets the succeeded of this DailyUsage.  # noqa: E501

        succeeded usage  # noqa: E501

        :return: The succeeded of this DailyUsage.  # noqa: E501
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this DailyUsage.

        succeeded usage  # noqa: E501

        :param succeeded: The succeeded of this DailyUsage.  # noqa: E501
        :type succeeded: int
        """

        self._succeeded = succeeded

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
        if not isinstance(other, DailyUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DailyUsage):
            return True

        return self.to_dict() != other.to_dict()
