# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.45.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Usage(object):
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
        'daily_usage': 'list[DailyUsage]',
        'end': 'datetime',
        'failed': 'int',
        'memory': 'float',
        'start': 'datetime',
        'succeeded': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'daily_usage': 'daily_usage',
        'end': 'end',
        'failed': 'failed',
        'memory': 'memory',
        'start': 'start',
        'succeeded': 'succeeded'
    }

    def __init__(self, cpu=0, daily_usage=[], end=None, failed=0, memory=0, start=None, succeeded=0, local_vars_configuration=None):  # noqa: E501
        """Usage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu = None
        self._daily_usage = None
        self._end = None
        self._failed = None
        self._memory = None
        self._start = None
        self._succeeded = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if daily_usage is not None:
            self.daily_usage = daily_usage
        self.end = end
        if failed is not None:
            self.failed = failed
        if memory is not None:
            self.memory = memory
        self.start = start
        if succeeded is not None:
            self.succeeded = succeeded

    @property
    def cpu(self):
        """Gets the cpu of this Usage.  # noqa: E501

        cpu usage  # noqa: E501

        :return: The cpu of this Usage.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this Usage.

        cpu usage  # noqa: E501

        :param cpu: The cpu of this Usage.  # noqa: E501
        :type cpu: float
        """

        self._cpu = cpu

    @property
    def daily_usage(self):
        """Gets the daily_usage of this Usage.  # noqa: E501

        daily breakdown of usage  # noqa: E501

        :return: The daily_usage of this Usage.  # noqa: E501
        :rtype: list[DailyUsage]
        """
        return self._daily_usage

    @daily_usage.setter
    def daily_usage(self, daily_usage):
        """Sets the daily_usage of this Usage.

        daily breakdown of usage  # noqa: E501

        :param daily_usage: The daily_usage of this Usage.  # noqa: E501
        :type daily_usage: list[DailyUsage]
        """

        self._daily_usage = daily_usage

    @property
    def end(self):
        """Gets the end of this Usage.  # noqa: E501

        The end date for this usage aggregation  # noqa: E501

        :return: The end of this Usage.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this Usage.

        The end date for this usage aggregation  # noqa: E501

        :param end: The end of this Usage.  # noqa: E501
        :type end: datetime
        """
        if self.local_vars_configuration.client_side_validation and end is None:  # noqa: E501
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

    @property
    def failed(self):
        """Gets the failed of this Usage.  # noqa: E501

        failed usage  # noqa: E501

        :return: The failed of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this Usage.

        failed usage  # noqa: E501

        :param failed: The failed of this Usage.  # noqa: E501
        :type failed: int
        """

        self._failed = failed

    @property
    def memory(self):
        """Gets the memory of this Usage.  # noqa: E501

        memory usage  # noqa: E501

        :return: The memory of this Usage.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this Usage.

        memory usage  # noqa: E501

        :param memory: The memory of this Usage.  # noqa: E501
        :type memory: float
        """

        self._memory = memory

    @property
    def start(self):
        """Gets the start of this Usage.  # noqa: E501

        The start date for this usage aggregation  # noqa: E501

        :return: The start of this Usage.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Usage.

        The start date for this usage aggregation  # noqa: E501

        :param start: The start of this Usage.  # noqa: E501
        :type start: datetime
        """
        if self.local_vars_configuration.client_side_validation and start is None:  # noqa: E501
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def succeeded(self):
        """Gets the succeeded of this Usage.  # noqa: E501

        succeeded usage  # noqa: E501

        :return: The succeeded of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this Usage.

        succeeded usage  # noqa: E501

        :param succeeded: The succeeded of this Usage.  # noqa: E501
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
        if not isinstance(other, Usage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Usage):
            return True

        return self.to_dict() != other.to_dict()
