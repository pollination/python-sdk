# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.47.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class BillingInfo(object):
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
        'cancel_url': 'str',
        'last_payment': 'SubscriptionPayment',
        'next_payment': 'SubscriptionPayment',
        'paused_at': 'datetime',
        'paused_from': 'datetime',
        'paused_reason': 'PausedReason',
        'payment_information': 'PaymentMethod',
        'signup_date': 'datetime',
        'update_url': 'str',
        'user_email': 'str'
    }

    attribute_map = {
        'cancel_url': 'cancel_url',
        'last_payment': 'last_payment',
        'next_payment': 'next_payment',
        'paused_at': 'paused_at',
        'paused_from': 'paused_from',
        'paused_reason': 'paused_reason',
        'payment_information': 'payment_information',
        'signup_date': 'signup_date',
        'update_url': 'update_url',
        'user_email': 'user_email'
    }

    def __init__(self, cancel_url=None, last_payment=None, next_payment=None, paused_at=None, paused_from=None, paused_reason=None, payment_information=None, signup_date=None, update_url=None, user_email=None, local_vars_configuration=None):  # noqa: E501
        """BillingInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cancel_url = None
        self._last_payment = None
        self._next_payment = None
        self._paused_at = None
        self._paused_from = None
        self._paused_reason = None
        self._payment_information = None
        self._signup_date = None
        self._update_url = None
        self._user_email = None
        self.discriminator = None

        self.cancel_url = cancel_url
        self.last_payment = last_payment
        if next_payment is not None:
            self.next_payment = next_payment
        if paused_at is not None:
            self.paused_at = paused_at
        if paused_from is not None:
            self.paused_from = paused_from
        if paused_reason is not None:
            self.paused_reason = paused_reason
        self.payment_information = payment_information
        self.signup_date = signup_date
        self.update_url = update_url
        self.user_email = user_email

    @property
    def cancel_url(self):
        """Gets the cancel_url of this BillingInfo.  # noqa: E501

        The url to cancel the subscription  # noqa: E501

        :return: The cancel_url of this BillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this BillingInfo.

        The url to cancel the subscription  # noqa: E501

        :param cancel_url: The cancel_url of this BillingInfo.  # noqa: E501
        :type cancel_url: str
        """
        if self.local_vars_configuration.client_side_validation and cancel_url is None:  # noqa: E501
            raise ValueError("Invalid value for `cancel_url`, must not be `None`")  # noqa: E501

        self._cancel_url = cancel_url

    @property
    def last_payment(self):
        """Gets the last_payment of this BillingInfo.  # noqa: E501

        The last payment made  # noqa: E501

        :return: The last_payment of this BillingInfo.  # noqa: E501
        :rtype: SubscriptionPayment
        """
        return self._last_payment

    @last_payment.setter
    def last_payment(self, last_payment):
        """Sets the last_payment of this BillingInfo.

        The last payment made  # noqa: E501

        :param last_payment: The last_payment of this BillingInfo.  # noqa: E501
        :type last_payment: SubscriptionPayment
        """
        if self.local_vars_configuration.client_side_validation and last_payment is None:  # noqa: E501
            raise ValueError("Invalid value for `last_payment`, must not be `None`")  # noqa: E501

        self._last_payment = last_payment

    @property
    def next_payment(self):
        """Gets the next_payment of this BillingInfo.  # noqa: E501

        The last payment made  # noqa: E501

        :return: The next_payment of this BillingInfo.  # noqa: E501
        :rtype: SubscriptionPayment
        """
        return self._next_payment

    @next_payment.setter
    def next_payment(self, next_payment):
        """Sets the next_payment of this BillingInfo.

        The last payment made  # noqa: E501

        :param next_payment: The next_payment of this BillingInfo.  # noqa: E501
        :type next_payment: SubscriptionPayment
        """

        self._next_payment = next_payment

    @property
    def paused_at(self):
        """Gets the paused_at of this BillingInfo.  # noqa: E501

        The date the subscription was paused  # noqa: E501

        :return: The paused_at of this BillingInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._paused_at

    @paused_at.setter
    def paused_at(self, paused_at):
        """Sets the paused_at of this BillingInfo.

        The date the subscription was paused  # noqa: E501

        :param paused_at: The paused_at of this BillingInfo.  # noqa: E501
        :type paused_at: datetime
        """

        self._paused_at = paused_at

    @property
    def paused_from(self):
        """Gets the paused_from of this BillingInfo.  # noqa: E501

        The date the subscription will be paused from  # noqa: E501

        :return: The paused_from of this BillingInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._paused_from

    @paused_from.setter
    def paused_from(self, paused_from):
        """Sets the paused_from of this BillingInfo.

        The date the subscription will be paused from  # noqa: E501

        :param paused_from: The paused_from of this BillingInfo.  # noqa: E501
        :type paused_from: datetime
        """

        self._paused_from = paused_from

    @property
    def paused_reason(self):
        """Gets the paused_reason of this BillingInfo.  # noqa: E501

        The reason the subscription was paused  # noqa: E501

        :return: The paused_reason of this BillingInfo.  # noqa: E501
        :rtype: PausedReason
        """
        return self._paused_reason

    @paused_reason.setter
    def paused_reason(self, paused_reason):
        """Sets the paused_reason of this BillingInfo.

        The reason the subscription was paused  # noqa: E501

        :param paused_reason: The paused_reason of this BillingInfo.  # noqa: E501
        :type paused_reason: PausedReason
        """

        self._paused_reason = paused_reason

    @property
    def payment_information(self):
        """Gets the payment_information of this BillingInfo.  # noqa: E501

        The payment method used  # noqa: E501

        :return: The payment_information of this BillingInfo.  # noqa: E501
        :rtype: PaymentMethod
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """Sets the payment_information of this BillingInfo.

        The payment method used  # noqa: E501

        :param payment_information: The payment_information of this BillingInfo.  # noqa: E501
        :type payment_information: PaymentMethod
        """
        if self.local_vars_configuration.client_side_validation and payment_information is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_information`, must not be `None`")  # noqa: E501

        self._payment_information = payment_information

    @property
    def signup_date(self):
        """Gets the signup_date of this BillingInfo.  # noqa: E501

        The date the subscription was created  # noqa: E501

        :return: The signup_date of this BillingInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._signup_date

    @signup_date.setter
    def signup_date(self, signup_date):
        """Sets the signup_date of this BillingInfo.

        The date the subscription was created  # noqa: E501

        :param signup_date: The signup_date of this BillingInfo.  # noqa: E501
        :type signup_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and signup_date is None:  # noqa: E501
            raise ValueError("Invalid value for `signup_date`, must not be `None`")  # noqa: E501

        self._signup_date = signup_date

    @property
    def update_url(self):
        """Gets the update_url of this BillingInfo.  # noqa: E501

        The url to update the billing info  # noqa: E501

        :return: The update_url of this BillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._update_url

    @update_url.setter
    def update_url(self, update_url):
        """Sets the update_url of this BillingInfo.

        The url to update the billing info  # noqa: E501

        :param update_url: The update_url of this BillingInfo.  # noqa: E501
        :type update_url: str
        """
        if self.local_vars_configuration.client_side_validation and update_url is None:  # noqa: E501
            raise ValueError("Invalid value for `update_url`, must not be `None`")  # noqa: E501

        self._update_url = update_url

    @property
    def user_email(self):
        """Gets the user_email of this BillingInfo.  # noqa: E501

        The email used for billing on this subscription  # noqa: E501

        :return: The user_email of this BillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this BillingInfo.

        The email used for billing on this subscription  # noqa: E501

        :param user_email: The user_email of this BillingInfo.  # noqa: E501
        :type user_email: str
        """
        if self.local_vars_configuration.client_side_validation and user_email is None:  # noqa: E501
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

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
        if not isinstance(other, BillingInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingInfo):
            return True

        return self.to_dict() != other.to_dict()
