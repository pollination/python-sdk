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


class PriceTier(object):
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
        'flat_amount': 'int',
        'flat_amount_decimal': 'str',
        'unit_amount': 'int',
        'unit_amount_decimal': 'str',
        'up_to': 'int'
    }

    attribute_map = {
        'flat_amount': 'flat_amount',
        'flat_amount_decimal': 'flat_amount_decimal',
        'unit_amount': 'unit_amount',
        'unit_amount_decimal': 'unit_amount_decimal',
        'up_to': 'up_to'
    }

    def __init__(self, flat_amount=None, flat_amount_decimal=None, unit_amount=None, unit_amount_decimal=None, up_to=None, local_vars_configuration=None):  # noqa: E501
        """PriceTier - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._flat_amount = None
        self._flat_amount_decimal = None
        self._unit_amount = None
        self._unit_amount_decimal = None
        self._up_to = None
        self.discriminator = None

        if flat_amount is not None:
            self.flat_amount = flat_amount
        if flat_amount_decimal is not None:
            self.flat_amount_decimal = flat_amount_decimal
        self.unit_amount = unit_amount
        self.unit_amount_decimal = unit_amount_decimal
        if up_to is not None:
            self.up_to = up_to

    @property
    def flat_amount(self):
        """Gets the flat_amount of this PriceTier.  # noqa: E501


        :return: The flat_amount of this PriceTier.  # noqa: E501
        :rtype: int
        """
        return self._flat_amount

    @flat_amount.setter
    def flat_amount(self, flat_amount):
        """Sets the flat_amount of this PriceTier.


        :param flat_amount: The flat_amount of this PriceTier.  # noqa: E501
        :type flat_amount: int
        """

        self._flat_amount = flat_amount

    @property
    def flat_amount_decimal(self):
        """Gets the flat_amount_decimal of this PriceTier.  # noqa: E501


        :return: The flat_amount_decimal of this PriceTier.  # noqa: E501
        :rtype: str
        """
        return self._flat_amount_decimal

    @flat_amount_decimal.setter
    def flat_amount_decimal(self, flat_amount_decimal):
        """Sets the flat_amount_decimal of this PriceTier.


        :param flat_amount_decimal: The flat_amount_decimal of this PriceTier.  # noqa: E501
        :type flat_amount_decimal: str
        """

        self._flat_amount_decimal = flat_amount_decimal

    @property
    def unit_amount(self):
        """Gets the unit_amount of this PriceTier.  # noqa: E501


        :return: The unit_amount of this PriceTier.  # noqa: E501
        :rtype: int
        """
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        """Sets the unit_amount of this PriceTier.


        :param unit_amount: The unit_amount of this PriceTier.  # noqa: E501
        :type unit_amount: int
        """
        if self.local_vars_configuration.client_side_validation and unit_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_amount`, must not be `None`")  # noqa: E501

        self._unit_amount = unit_amount

    @property
    def unit_amount_decimal(self):
        """Gets the unit_amount_decimal of this PriceTier.  # noqa: E501


        :return: The unit_amount_decimal of this PriceTier.  # noqa: E501
        :rtype: str
        """
        return self._unit_amount_decimal

    @unit_amount_decimal.setter
    def unit_amount_decimal(self, unit_amount_decimal):
        """Sets the unit_amount_decimal of this PriceTier.


        :param unit_amount_decimal: The unit_amount_decimal of this PriceTier.  # noqa: E501
        :type unit_amount_decimal: str
        """
        if self.local_vars_configuration.client_side_validation and unit_amount_decimal is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_amount_decimal`, must not be `None`")  # noqa: E501

        self._unit_amount_decimal = unit_amount_decimal

    @property
    def up_to(self):
        """Gets the up_to of this PriceTier.  # noqa: E501


        :return: The up_to of this PriceTier.  # noqa: E501
        :rtype: int
        """
        return self._up_to

    @up_to.setter
    def up_to(self, up_to):
        """Sets the up_to of this PriceTier.


        :param up_to: The up_to of this PriceTier.  # noqa: E501
        :type up_to: int
        """

        self._up_to = up_to

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
        if not isinstance(other, PriceTier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PriceTier):
            return True

        return self.to_dict() != other.to_dict()
