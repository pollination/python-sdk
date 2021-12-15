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


class Price(object):
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
        'active': 'bool',
        'currency': 'str',
        'id': 'str',
        'metadata': 'object',
        'nickname': 'str',
        'product': 'str',
        'recurring': 'PriceRecurrence',
        'tiers': 'list[PriceTier]',
        'type': 'PriceType',
        'unit_amount': 'int'
    }

    attribute_map = {
        'active': 'active',
        'currency': 'currency',
        'id': 'id',
        'metadata': 'metadata',
        'nickname': 'nickname',
        'product': 'product',
        'recurring': 'recurring',
        'tiers': 'tiers',
        'type': 'type',
        'unit_amount': 'unit_amount'
    }

    def __init__(self, active=None, currency=None, id=None, metadata=None, nickname=None, product=None, recurring=None, tiers=None, type=None, unit_amount=None, local_vars_configuration=None):  # noqa: E501
        """Price - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._currency = None
        self._id = None
        self._metadata = None
        self._nickname = None
        self._product = None
        self._recurring = None
        self._tiers = None
        self._type = None
        self._unit_amount = None
        self.discriminator = None

        self.active = active
        self.currency = currency
        self.id = id
        if metadata is not None:
            self.metadata = metadata
        if nickname is not None:
            self.nickname = nickname
        self.product = product
        if recurring is not None:
            self.recurring = recurring
        if tiers is not None:
            self.tiers = tiers
        self.type = type
        if unit_amount is not None:
            self.unit_amount = unit_amount

    @property
    def active(self):
        """Gets the active of this Price.  # noqa: E501


        :return: The active of this Price.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Price.


        :param active: The active of this Price.  # noqa: E501
        :type active: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def currency(self):
        """Gets the currency of this Price.  # noqa: E501


        :return: The currency of this Price.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Price.


        :param currency: The currency of this Price.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def id(self):
        """Gets the id of this Price.  # noqa: E501


        :return: The id of this Price.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Price.


        :param id: The id of this Price.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this Price.  # noqa: E501


        :return: The metadata of this Price.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Price.


        :param metadata: The metadata of this Price.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def nickname(self):
        """Gets the nickname of this Price.  # noqa: E501


        :return: The nickname of this Price.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this Price.


        :param nickname: The nickname of this Price.  # noqa: E501
        :type nickname: str
        """

        self._nickname = nickname

    @property
    def product(self):
        """Gets the product of this Price.  # noqa: E501


        :return: The product of this Price.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Price.


        :param product: The product of this Price.  # noqa: E501
        :type product: str
        """
        if self.local_vars_configuration.client_side_validation and product is None:  # noqa: E501
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def recurring(self):
        """Gets the recurring of this Price.  # noqa: E501


        :return: The recurring of this Price.  # noqa: E501
        :rtype: PriceRecurrence
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """Sets the recurring of this Price.


        :param recurring: The recurring of this Price.  # noqa: E501
        :type recurring: PriceRecurrence
        """

        self._recurring = recurring

    @property
    def tiers(self):
        """Gets the tiers of this Price.  # noqa: E501


        :return: The tiers of this Price.  # noqa: E501
        :rtype: list[PriceTier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this Price.


        :param tiers: The tiers of this Price.  # noqa: E501
        :type tiers: list[PriceTier]
        """

        self._tiers = tiers

    @property
    def type(self):
        """Gets the type of this Price.  # noqa: E501


        :return: The type of this Price.  # noqa: E501
        :rtype: PriceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Price.


        :param type: The type of this Price.  # noqa: E501
        :type type: PriceType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def unit_amount(self):
        """Gets the unit_amount of this Price.  # noqa: E501


        :return: The unit_amount of this Price.  # noqa: E501
        :rtype: int
        """
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        """Sets the unit_amount of this Price.


        :param unit_amount: The unit_amount of this Price.  # noqa: E501
        :type unit_amount: int
        """

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
        if not isinstance(other, Price):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Price):
            return True

        return self.to_dict() != other.to_dict()
