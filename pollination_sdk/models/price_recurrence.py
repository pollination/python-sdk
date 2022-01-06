# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.22.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class PriceRecurrence(object):
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
        'interval': 'str',
        'interval_count': 'int',
        'usage_type': 'str'
    }

    attribute_map = {
        'interval': 'interval',
        'interval_count': 'interval_count',
        'usage_type': 'usage_type'
    }

    def __init__(self, interval=None, interval_count=None, usage_type=None, local_vars_configuration=None):  # noqa: E501
        """PriceRecurrence - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._interval = None
        self._interval_count = None
        self._usage_type = None
        self.discriminator = None

        self.interval = interval
        self.interval_count = interval_count
        self.usage_type = usage_type

    @property
    def interval(self):
        """Gets the interval of this PriceRecurrence.  # noqa: E501


        :return: The interval of this PriceRecurrence.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this PriceRecurrence.


        :param interval: The interval of this PriceRecurrence.  # noqa: E501
        :type interval: str
        """
        if self.local_vars_configuration.client_side_validation and interval is None:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def interval_count(self):
        """Gets the interval_count of this PriceRecurrence.  # noqa: E501


        :return: The interval_count of this PriceRecurrence.  # noqa: E501
        :rtype: int
        """
        return self._interval_count

    @interval_count.setter
    def interval_count(self, interval_count):
        """Sets the interval_count of this PriceRecurrence.


        :param interval_count: The interval_count of this PriceRecurrence.  # noqa: E501
        :type interval_count: int
        """
        if self.local_vars_configuration.client_side_validation and interval_count is None:  # noqa: E501
            raise ValueError("Invalid value for `interval_count`, must not be `None`")  # noqa: E501

        self._interval_count = interval_count

    @property
    def usage_type(self):
        """Gets the usage_type of this PriceRecurrence.  # noqa: E501


        :return: The usage_type of this PriceRecurrence.  # noqa: E501
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this PriceRecurrence.


        :param usage_type: The usage_type of this PriceRecurrence.  # noqa: E501
        :type usage_type: str
        """
        if self.local_vars_configuration.client_side_validation and usage_type is None:  # noqa: E501
            raise ValueError("Invalid value for `usage_type`, must not be `None`")  # noqa: E501

        self._usage_type = usage_type

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
        if not isinstance(other, PriceRecurrence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PriceRecurrence):
            return True

        return self.to_dict() != other.to_dict()
