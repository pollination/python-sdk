# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.23.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class SubscriptionItemPublic(object):
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
        'metadata': 'object',
        'price': 'Price',
        'quantity': 'int'
    }

    attribute_map = {
        'id': 'id',
        'metadata': 'metadata',
        'price': 'price',
        'quantity': 'quantity'
    }

    def __init__(self, id=None, metadata=None, price=None, quantity=None, local_vars_configuration=None):  # noqa: E501
        """SubscriptionItemPublic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._metadata = None
        self._price = None
        self._quantity = None
        self.discriminator = None

        self.id = id
        if metadata is not None:
            self.metadata = metadata
        self.price = price
        self.quantity = quantity

    @property
    def id(self):
        """Gets the id of this SubscriptionItemPublic.  # noqa: E501


        :return: The id of this SubscriptionItemPublic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionItemPublic.


        :param id: The id of this SubscriptionItemPublic.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this SubscriptionItemPublic.  # noqa: E501


        :return: The metadata of this SubscriptionItemPublic.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SubscriptionItemPublic.


        :param metadata: The metadata of this SubscriptionItemPublic.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def price(self):
        """Gets the price of this SubscriptionItemPublic.  # noqa: E501


        :return: The price of this SubscriptionItemPublic.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SubscriptionItemPublic.


        :param price: The price of this SubscriptionItemPublic.  # noqa: E501
        :type price: Price
        """
        if self.local_vars_configuration.client_side_validation and price is None:  # noqa: E501
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionItemPublic.  # noqa: E501


        :return: The quantity of this SubscriptionItemPublic.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionItemPublic.


        :param quantity: The quantity of this SubscriptionItemPublic.  # noqa: E501
        :type quantity: int
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

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
        if not isinstance(other, SubscriptionItemPublic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionItemPublic):
            return True

        return self.to_dict() != other.to_dict()
