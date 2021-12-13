# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.20.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class QuotaExtension(object):
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
        'id': 'str',
        'name': 'str',
        'quantity': 'int',
        'type': 'QuotaType',
        'unit_amount': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'quantity': 'quantity',
        'type': 'type',
        'unit_amount': 'unit_amount'
    }

    def __init__(self, id=None, name=None, quantity=None, type=None, unit_amount=None, local_vars_configuration=None):  # noqa: E501
        """QuotaExtension - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._quantity = None
        self._type = None
        self._unit_amount = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.quantity = quantity
        self.type = type
        self.unit_amount = unit_amount

    @property
    def id(self):
        """Gets the id of this QuotaExtension.  # noqa: E501

        The ID of the quota extension  # noqa: E501

        :return: The id of this QuotaExtension.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuotaExtension.

        The ID of the quota extension  # noqa: E501

        :param id: The id of this QuotaExtension.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this QuotaExtension.  # noqa: E501

        Name of the quota extension plan  # noqa: E501

        :return: The name of this QuotaExtension.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuotaExtension.

        Name of the quota extension plan  # noqa: E501

        :param name: The name of this QuotaExtension.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def quantity(self):
        """Gets the quantity of this QuotaExtension.  # noqa: E501

        The number of times to count this extension  # noqa: E501

        :return: The quantity of this QuotaExtension.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this QuotaExtension.

        The number of times to count this extension  # noqa: E501

        :param quantity: The quantity of this QuotaExtension.  # noqa: E501
        :type quantity: int
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def type(self):
        """Gets the type of this QuotaExtension.  # noqa: E501

        The type of quota this applies to  # noqa: E501

        :return: The type of this QuotaExtension.  # noqa: E501
        :rtype: QuotaType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaExtension.

        The type of quota this applies to  # noqa: E501

        :param type: The type of this QuotaExtension.  # noqa: E501
        :type type: QuotaType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def unit_amount(self):
        """Gets the unit_amount of this QuotaExtension.  # noqa: E501

        The amount by which this object extends a given quota  # noqa: E501

        :return: The unit_amount of this QuotaExtension.  # noqa: E501
        :rtype: float
        """
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        """Sets the unit_amount of this QuotaExtension.

        The amount by which this object extends a given quota  # noqa: E501

        :param unit_amount: The unit_amount of this QuotaExtension.  # noqa: E501
        :type unit_amount: float
        """
        if self.local_vars_configuration.client_side_validation and unit_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_amount`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unit_amount is not None and unit_amount < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `unit_amount`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._unit_amount = unit_amount

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
        if not isinstance(other, QuotaExtension):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuotaExtension):
            return True

        return self.to_dict() != other.to_dict()
