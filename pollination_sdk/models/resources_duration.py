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


class ResourcesDuration(object):
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
        'cpu': 'int',
        'memory': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory'
    }

    def __init__(self, cpu=0, memory=0, local_vars_configuration=None):  # noqa: E501
        """ResourcesDuration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu = None
        self._memory = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this ResourcesDuration.  # noqa: E501


        :return: The cpu of this ResourcesDuration.  # noqa: E501
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ResourcesDuration.


        :param cpu: The cpu of this ResourcesDuration.  # noqa: E501
        :type cpu: int
        """

        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this ResourcesDuration.  # noqa: E501


        :return: The memory of this ResourcesDuration.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ResourcesDuration.


        :param memory: The memory of this ResourcesDuration.  # noqa: E501
        :type memory: int
        """

        self._memory = memory

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
        if not isinstance(other, ResourcesDuration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourcesDuration):
            return True

        return self.to_dict() != other.to_dict()