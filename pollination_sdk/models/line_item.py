# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.21.2
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class LineItem(object):
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
        'amount': 'int',
        'currency': 'str',
        'description': 'str',
        'id': 'str',
        'metadata': 'object',
        'period': 'Period',
        'price': 'Price',
        'proration': 'bool',
        'quantity': 'int',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'description': 'description',
        'id': 'id',
        'metadata': 'metadata',
        'period': 'period',
        'price': 'price',
        'proration': 'proration',
        'quantity': 'quantity',
        'type': 'type'
    }

    def __init__(self, amount=None, currency=None, description=None, id=None, metadata=None, period=None, price=None, proration=None, quantity=None, type=None, local_vars_configuration=None):  # noqa: E501
        """LineItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._currency = None
        self._description = None
        self._id = None
        self._metadata = None
        self._period = None
        self._price = None
        self._proration = None
        self._quantity = None
        self._type = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        self.description = description
        self.id = id
        if metadata is not None:
            self.metadata = metadata
        self.period = period
        self.price = price
        self.proration = proration
        self.quantity = quantity
        self.type = type

    @property
    def amount(self):
        """Gets the amount of this LineItem.  # noqa: E501


        :return: The amount of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LineItem.


        :param amount: The amount of this LineItem.  # noqa: E501
        :type amount: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this LineItem.  # noqa: E501


        :return: The currency of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this LineItem.


        :param currency: The currency of this LineItem.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def description(self):
        """Gets the description of this LineItem.  # noqa: E501


        :return: The description of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LineItem.


        :param description: The description of this LineItem.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this LineItem.  # noqa: E501


        :return: The id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LineItem.


        :param id: The id of this LineItem.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this LineItem.  # noqa: E501


        :return: The metadata of this LineItem.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this LineItem.


        :param metadata: The metadata of this LineItem.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def period(self):
        """Gets the period of this LineItem.  # noqa: E501


        :return: The period of this LineItem.  # noqa: E501
        :rtype: Period
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this LineItem.


        :param period: The period of this LineItem.  # noqa: E501
        :type period: Period
        """
        if self.local_vars_configuration.client_side_validation and period is None:  # noqa: E501
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501

        self._period = period

    @property
    def price(self):
        """Gets the price of this LineItem.  # noqa: E501


        :return: The price of this LineItem.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this LineItem.


        :param price: The price of this LineItem.  # noqa: E501
        :type price: Price
        """
        if self.local_vars_configuration.client_side_validation and price is None:  # noqa: E501
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def proration(self):
        """Gets the proration of this LineItem.  # noqa: E501


        :return: The proration of this LineItem.  # noqa: E501
        :rtype: bool
        """
        return self._proration

    @proration.setter
    def proration(self, proration):
        """Sets the proration of this LineItem.


        :param proration: The proration of this LineItem.  # noqa: E501
        :type proration: bool
        """
        if self.local_vars_configuration.client_side_validation and proration is None:  # noqa: E501
            raise ValueError("Invalid value for `proration`, must not be `None`")  # noqa: E501

        self._proration = proration

    @property
    def quantity(self):
        """Gets the quantity of this LineItem.  # noqa: E501


        :return: The quantity of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItem.


        :param quantity: The quantity of this LineItem.  # noqa: E501
        :type quantity: int
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def type(self):
        """Gets the type of this LineItem.  # noqa: E501


        :return: The type of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LineItem.


        :param type: The type of this LineItem.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, LineItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LineItem):
            return True

        return self.to_dict() != other.to_dict()
