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


class InvoiceList(object):
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
        'has_more': 'bool',
        'resources': 'list[Invoice]'
    }

    attribute_map = {
        'has_more': 'has_more',
        'resources': 'resources'
    }

    def __init__(self, has_more=None, resources=None, local_vars_configuration=None):  # noqa: E501
        """InvoiceList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._has_more = None
        self._resources = None
        self.discriminator = None

        self.has_more = has_more
        self.resources = resources

    @property
    def has_more(self):
        """Gets the has_more of this InvoiceList.  # noqa: E501


        :return: The has_more of this InvoiceList.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this InvoiceList.


        :param has_more: The has_more of this InvoiceList.  # noqa: E501
        :type has_more: bool
        """
        if self.local_vars_configuration.client_side_validation and has_more is None:  # noqa: E501
            raise ValueError("Invalid value for `has_more`, must not be `None`")  # noqa: E501

        self._has_more = has_more

    @property
    def resources(self):
        """Gets the resources of this InvoiceList.  # noqa: E501


        :return: The resources of this InvoiceList.  # noqa: E501
        :rtype: list[Invoice]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this InvoiceList.


        :param resources: The resources of this InvoiceList.  # noqa: E501
        :type resources: list[Invoice]
        """
        if self.local_vars_configuration.client_side_validation and resources is None:  # noqa: E501
            raise ValueError("Invalid value for `resources`, must not be `None`")  # noqa: E501

        self._resources = resources

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
        if not isinstance(other, InvoiceList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceList):
            return True

        return self.to_dict() != other.to_dict()