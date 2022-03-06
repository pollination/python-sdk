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


class PaymentMethod(object):
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
        'card_type': 'CardType',
        'expiry_date': 'str',
        'last_four_digits': 'str',
        'payment_method': 'PaymentMethodEnum'
    }

    attribute_map = {
        'card_type': 'card_type',
        'expiry_date': 'expiry_date',
        'last_four_digits': 'last_four_digits',
        'payment_method': 'payment_method'
    }

    def __init__(self, card_type=None, expiry_date=None, last_four_digits=None, payment_method=None, local_vars_configuration=None):  # noqa: E501
        """PaymentMethod - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._card_type = None
        self._expiry_date = None
        self._last_four_digits = None
        self._payment_method = None
        self.discriminator = None

        self.card_type = card_type
        self.expiry_date = expiry_date
        self.last_four_digits = last_four_digits
        self.payment_method = payment_method

    @property
    def card_type(self):
        """Gets the card_type of this PaymentMethod.  # noqa: E501


        :return: The card_type of this PaymentMethod.  # noqa: E501
        :rtype: CardType
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this PaymentMethod.


        :param card_type: The card_type of this PaymentMethod.  # noqa: E501
        :type card_type: CardType
        """
        if self.local_vars_configuration.client_side_validation and card_type is None:  # noqa: E501
            raise ValueError("Invalid value for `card_type`, must not be `None`")  # noqa: E501

        self._card_type = card_type

    @property
    def expiry_date(self):
        """Gets the expiry_date of this PaymentMethod.  # noqa: E501


        :return: The expiry_date of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this PaymentMethod.


        :param expiry_date: The expiry_date of this PaymentMethod.  # noqa: E501
        :type expiry_date: str
        """
        if self.local_vars_configuration.client_side_validation and expiry_date is None:  # noqa: E501
            raise ValueError("Invalid value for `expiry_date`, must not be `None`")  # noqa: E501

        self._expiry_date = expiry_date

    @property
    def last_four_digits(self):
        """Gets the last_four_digits of this PaymentMethod.  # noqa: E501


        :return: The last_four_digits of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._last_four_digits

    @last_four_digits.setter
    def last_four_digits(self, last_four_digits):
        """Sets the last_four_digits of this PaymentMethod.


        :param last_four_digits: The last_four_digits of this PaymentMethod.  # noqa: E501
        :type last_four_digits: str
        """
        if self.local_vars_configuration.client_side_validation and last_four_digits is None:  # noqa: E501
            raise ValueError("Invalid value for `last_four_digits`, must not be `None`")  # noqa: E501

        self._last_four_digits = last_four_digits

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentMethod.  # noqa: E501


        :return: The payment_method of this PaymentMethod.  # noqa: E501
        :rtype: PaymentMethodEnum
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentMethod.


        :param payment_method: The payment_method of this PaymentMethod.  # noqa: E501
        :type payment_method: PaymentMethodEnum
        """
        if self.local_vars_configuration.client_side_validation and payment_method is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

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
        if not isinstance(other, PaymentMethod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentMethod):
            return True

        return self.to_dict() != other.to_dict()