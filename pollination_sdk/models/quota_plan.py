# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.24.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class QuotaPlan(object):
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
        'enforced': 'bool',
        'limit': 'float',
        'name': 'str',
        'resets': 'bool'
    }

    attribute_map = {
        'enforced': 'enforced',
        'limit': 'limit',
        'name': 'name',
        'resets': 'resets'
    }

    def __init__(self, enforced=False, limit=None, name=None, resets=False, local_vars_configuration=None):  # noqa: E501
        """QuotaPlan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enforced = None
        self._limit = None
        self._name = None
        self._resets = None
        self.discriminator = None

        if enforced is not None:
            self.enforced = enforced
        if limit is not None:
            self.limit = limit
        self.name = name
        if resets is not None:
            self.resets = resets

    @property
    def enforced(self):
        """Gets the enforced of this QuotaPlan.  # noqa: E501

        Whether the limit is triggers a blocking response from the server  # noqa: E501

        :return: The enforced of this QuotaPlan.  # noqa: E501
        :rtype: bool
        """
        return self._enforced

    @enforced.setter
    def enforced(self, enforced):
        """Sets the enforced of this QuotaPlan.

        Whether the limit is triggers a blocking response from the server  # noqa: E501

        :param enforced: The enforced of this QuotaPlan.  # noqa: E501
        :type enforced: bool
        """

        self._enforced = enforced

    @property
    def limit(self):
        """Gets the limit of this QuotaPlan.  # noqa: E501

        The maximum amount of a resource that a subscription allows  # noqa: E501

        :return: The limit of this QuotaPlan.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QuotaPlan.

        The maximum amount of a resource that a subscription allows  # noqa: E501

        :param limit: The limit of this QuotaPlan.  # noqa: E501
        :type limit: float
        """

        self._limit = limit

    @property
    def name(self):
        """Gets the name of this QuotaPlan.  # noqa: E501

        The name of the quota  # noqa: E501

        :return: The name of this QuotaPlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuotaPlan.

        The name of the quota  # noqa: E501

        :param name: The name of this QuotaPlan.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resets(self):
        """Gets the resets of this QuotaPlan.  # noqa: E501

        Whether consumption is reset to 0 every month  # noqa: E501

        :return: The resets of this QuotaPlan.  # noqa: E501
        :rtype: bool
        """
        return self._resets

    @resets.setter
    def resets(self, resets):
        """Sets the resets of this QuotaPlan.

        Whether consumption is reset to 0 every month  # noqa: E501

        :param resets: The resets of this QuotaPlan.  # noqa: E501
        :type resets: bool
        """

        self._resets = resets

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
        if not isinstance(other, QuotaPlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuotaPlan):
            return True

        return self.to_dict() != other.to_dict()
