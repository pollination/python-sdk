# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.34.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Payment(object):
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
        'id': 'int',
        'is_one_off_charge': 'bool',
        'is_paid': 'bool',
        'payout_date': 'date',
        'receipt_url': 'str',
        'subscription_id': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'id': 'id',
        'is_one_off_charge': 'is_one_off_charge',
        'is_paid': 'is_paid',
        'payout_date': 'payout_date',
        'receipt_url': 'receipt_url',
        'subscription_id': 'subscription_id'
    }

    def __init__(self, amount=None, currency=None, id=None, is_one_off_charge=None, is_paid=None, payout_date=None, receipt_url=None, subscription_id=None, local_vars_configuration=None):  # noqa: E501
        """Payment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._currency = None
        self._id = None
        self._is_one_off_charge = None
        self._is_paid = None
        self._payout_date = None
        self._receipt_url = None
        self._subscription_id = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        self.id = id
        self.is_one_off_charge = is_one_off_charge
        self.is_paid = is_paid
        self.payout_date = payout_date
        if receipt_url is not None:
            self.receipt_url = receipt_url
        self.subscription_id = subscription_id

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501


        :return: The amount of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.


        :param amount: The amount of this Payment.  # noqa: E501
        :type amount: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Payment.  # noqa: E501


        :return: The currency of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Payment.


        :param currency: The currency of this Payment.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def id(self):
        """Gets the id of this Payment.  # noqa: E501


        :return: The id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Payment.


        :param id: The id of this Payment.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_one_off_charge(self):
        """Gets the is_one_off_charge of this Payment.  # noqa: E501


        :return: The is_one_off_charge of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._is_one_off_charge

    @is_one_off_charge.setter
    def is_one_off_charge(self, is_one_off_charge):
        """Sets the is_one_off_charge of this Payment.


        :param is_one_off_charge: The is_one_off_charge of this Payment.  # noqa: E501
        :type is_one_off_charge: bool
        """
        if self.local_vars_configuration.client_side_validation and is_one_off_charge is None:  # noqa: E501
            raise ValueError("Invalid value for `is_one_off_charge`, must not be `None`")  # noqa: E501

        self._is_one_off_charge = is_one_off_charge

    @property
    def is_paid(self):
        """Gets the is_paid of this Payment.  # noqa: E501


        :return: The is_paid of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._is_paid

    @is_paid.setter
    def is_paid(self, is_paid):
        """Sets the is_paid of this Payment.


        :param is_paid: The is_paid of this Payment.  # noqa: E501
        :type is_paid: bool
        """
        if self.local_vars_configuration.client_side_validation and is_paid is None:  # noqa: E501
            raise ValueError("Invalid value for `is_paid`, must not be `None`")  # noqa: E501

        self._is_paid = is_paid

    @property
    def payout_date(self):
        """Gets the payout_date of this Payment.  # noqa: E501


        :return: The payout_date of this Payment.  # noqa: E501
        :rtype: date
        """
        return self._payout_date

    @payout_date.setter
    def payout_date(self, payout_date):
        """Sets the payout_date of this Payment.


        :param payout_date: The payout_date of this Payment.  # noqa: E501
        :type payout_date: date
        """
        if self.local_vars_configuration.client_side_validation and payout_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payout_date`, must not be `None`")  # noqa: E501

        self._payout_date = payout_date

    @property
    def receipt_url(self):
        """Gets the receipt_url of this Payment.  # noqa: E501


        :return: The receipt_url of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._receipt_url

    @receipt_url.setter
    def receipt_url(self, receipt_url):
        """Sets the receipt_url of this Payment.


        :param receipt_url: The receipt_url of this Payment.  # noqa: E501
        :type receipt_url: str
        """

        self._receipt_url = receipt_url

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Payment.  # noqa: E501


        :return: The subscription_id of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Payment.


        :param subscription_id: The subscription_id of this Payment.  # noqa: E501
        :type subscription_id: int
        """
        if self.local_vars_configuration.client_side_validation and subscription_id is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id

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
        if not isinstance(other, Payment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Payment):
            return True

        return self.to_dict() != other.to_dict()
