# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.28.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class BillingOption(object):
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
        'billing_period': 'int',
        'billing_type': 'str',
        'id': 'int',
        'name': 'str',
        'recurring_price': 'dict(str, float)'
    }

    attribute_map = {
        'billing_period': 'billing_period',
        'billing_type': 'billing_type',
        'id': 'id',
        'name': 'name',
        'recurring_price': 'recurring_price'
    }

    def __init__(self, billing_period=None, billing_type=None, id=None, name=None, recurring_price=None, local_vars_configuration=None):  # noqa: E501
        """BillingOption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._billing_period = None
        self._billing_type = None
        self._id = None
        self._name = None
        self._recurring_price = None
        self.discriminator = None

        self.billing_period = billing_period
        self.billing_type = billing_type
        self.id = id
        self.name = name
        self.recurring_price = recurring_price

    @property
    def billing_period(self):
        """Gets the billing_period of this BillingOption.  # noqa: E501

        The number of period for the billing cycle  # noqa: E501

        :return: The billing_period of this BillingOption.  # noqa: E501
        :rtype: int
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this BillingOption.

        The number of period for the billing cycle  # noqa: E501

        :param billing_period: The billing_period of this BillingOption.  # noqa: E501
        :type billing_period: int
        """
        if self.local_vars_configuration.client_side_validation and billing_period is None:  # noqa: E501
            raise ValueError("Invalid value for `billing_period`, must not be `None`")  # noqa: E501

        self._billing_period = billing_period

    @property
    def billing_type(self):
        """Gets the billing_type of this BillingOption.  # noqa: E501

        The type of billing option, can be daily, monthly or yearly  # noqa: E501

        :return: The billing_type of this BillingOption.  # noqa: E501
        :rtype: str
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this BillingOption.

        The type of billing option, can be daily, monthly or yearly  # noqa: E501

        :param billing_type: The billing_type of this BillingOption.  # noqa: E501
        :type billing_type: str
        """
        if self.local_vars_configuration.client_side_validation and billing_type is None:  # noqa: E501
            raise ValueError("Invalid value for `billing_type`, must not be `None`")  # noqa: E501

        self._billing_type = billing_type

    @property
    def id(self):
        """Gets the id of this BillingOption.  # noqa: E501

        The id of the billing option  # noqa: E501

        :return: The id of this BillingOption.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BillingOption.

        The id of the billing option  # noqa: E501

        :param id: The id of this BillingOption.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this BillingOption.  # noqa: E501

        The name of the billing option  # noqa: E501

        :return: The name of this BillingOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BillingOption.

        The name of the billing option  # noqa: E501

        :param name: The name of this BillingOption.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def recurring_price(self):
        """Gets the recurring_price of this BillingOption.  # noqa: E501

        The price of the billing option  # noqa: E501

        :return: The recurring_price of this BillingOption.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._recurring_price

    @recurring_price.setter
    def recurring_price(self, recurring_price):
        """Sets the recurring_price of this BillingOption.

        The price of the billing option  # noqa: E501

        :param recurring_price: The recurring_price of this BillingOption.  # noqa: E501
        :type recurring_price: dict(str, float)
        """
        if self.local_vars_configuration.client_side_validation and recurring_price is None:  # noqa: E501
            raise ValueError("Invalid value for `recurring_price`, must not be `None`")  # noqa: E501

        self._recurring_price = recurring_price

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
        if not isinstance(other, BillingOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingOption):
            return True

        return self.to_dict() != other.to_dict()
