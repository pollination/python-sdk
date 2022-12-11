# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.33.0
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
        'description': 'str',
        'display_name': 'str',
        'enforced': 'bool',
        'limit': 'float',
        'max_limit': 'float',
        'resets': 'bool',
        'type': 'QuotaType',
        'unit': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'enforced': 'enforced',
        'limit': 'limit',
        'max_limit': 'max_limit',
        'resets': 'resets',
        'type': 'type',
        'unit': 'unit'
    }

    def __init__(self, description=None, display_name=None, enforced=False, limit=None, max_limit=None, resets=False, type=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """QuotaPlan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._display_name = None
        self._enforced = None
        self._limit = None
        self._max_limit = None
        self._resets = None
        self._type = None
        self._unit = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if enforced is not None:
            self.enforced = enforced
        if limit is not None:
            self.limit = limit
        if max_limit is not None:
            self.max_limit = max_limit
        if resets is not None:
            self.resets = resets
        self.type = type
        if unit is not None:
            self.unit = unit

    @property
    def description(self):
        """Gets the description of this QuotaPlan.  # noqa: E501

        The description  # noqa: E501

        :return: The description of this QuotaPlan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QuotaPlan.

        The description  # noqa: E501

        :param description: The description of this QuotaPlan.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this QuotaPlan.  # noqa: E501

        The human-readable name  # noqa: E501

        :return: The display_name of this QuotaPlan.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this QuotaPlan.

        The human-readable name  # noqa: E501

        :param display_name: The display_name of this QuotaPlan.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

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
    def max_limit(self):
        """Gets the max_limit of this QuotaPlan.  # noqa: E501

        The maximum amount of a resource that a subscription allows  # noqa: E501

        :return: The max_limit of this QuotaPlan.  # noqa: E501
        :rtype: float
        """
        return self._max_limit

    @max_limit.setter
    def max_limit(self, max_limit):
        """Sets the max_limit of this QuotaPlan.

        The maximum amount of a resource that a subscription allows  # noqa: E501

        :param max_limit: The max_limit of this QuotaPlan.  # noqa: E501
        :type max_limit: float
        """

        self._max_limit = max_limit

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

    @property
    def type(self):
        """Gets the type of this QuotaPlan.  # noqa: E501

        The name of the quota  # noqa: E501

        :return: The type of this QuotaPlan.  # noqa: E501
        :rtype: QuotaType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaPlan.

        The name of the quota  # noqa: E501

        :param type: The type of this QuotaPlan.  # noqa: E501
        :type type: QuotaType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def unit(self):
        """Gets the unit of this QuotaPlan.  # noqa: E501

        The unit in which the usage and limit are measured  # noqa: E501

        :return: The unit of this QuotaPlan.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this QuotaPlan.

        The unit in which the usage and limit are measured  # noqa: E501

        :param unit: The unit of this QuotaPlan.  # noqa: E501
        :type unit: str
        """

        self._unit = unit

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
