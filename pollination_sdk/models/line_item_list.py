# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.21.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class LineItemList(object):
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
        'data': 'list[LineItem]',
        'has_more': 'bool'
    }

    attribute_map = {
        'data': 'data',
        'has_more': 'has_more'
    }

    def __init__(self, data=None, has_more=None, local_vars_configuration=None):  # noqa: E501
        """LineItemList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._has_more = None
        self.discriminator = None

        self.data = data
        self.has_more = has_more

    @property
    def data(self):
        """Gets the data of this LineItemList.  # noqa: E501


        :return: The data of this LineItemList.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this LineItemList.


        :param data: The data of this LineItemList.  # noqa: E501
        :type data: list[LineItem]
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def has_more(self):
        """Gets the has_more of this LineItemList.  # noqa: E501


        :return: The has_more of this LineItemList.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this LineItemList.


        :param has_more: The has_more of this LineItemList.  # noqa: E501
        :type has_more: bool
        """
        if self.local_vars_configuration.client_side_validation and has_more is None:  # noqa: E501
            raise ValueError("Invalid value for `has_more`, must not be `None`")  # noqa: E501

        self._has_more = has_more

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
        if not isinstance(other, LineItemList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LineItemList):
            return True

        return self.to_dict() != other.to_dict()
