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


class UpdateInvoicePreview(object):
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
        'exceeded_quotas': 'list[Quota]',
        'immediate': 'InvoicePreview',
        'payment_method': 'CardPublic',
        'upcoming': 'InvoicePreview'
    }

    attribute_map = {
        'exceeded_quotas': 'exceeded_quotas',
        'immediate': 'immediate',
        'payment_method': 'payment_method',
        'upcoming': 'upcoming'
    }

    def __init__(self, exceeded_quotas=[], immediate=None, payment_method=None, upcoming=None, local_vars_configuration=None):  # noqa: E501
        """UpdateInvoicePreview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exceeded_quotas = None
        self._immediate = None
        self._payment_method = None
        self._upcoming = None
        self.discriminator = None

        if exceeded_quotas is not None:
            self.exceeded_quotas = exceeded_quotas
        self.immediate = immediate
        if payment_method is not None:
            self.payment_method = payment_method
        self.upcoming = upcoming

    @property
    def exceeded_quotas(self):
        """Gets the exceeded_quotas of this UpdateInvoicePreview.  # noqa: E501

        A list of quotas that would be exceeded by the update  # noqa: E501

        :return: The exceeded_quotas of this UpdateInvoicePreview.  # noqa: E501
        :rtype: list[Quota]
        """
        return self._exceeded_quotas

    @exceeded_quotas.setter
    def exceeded_quotas(self, exceeded_quotas):
        """Sets the exceeded_quotas of this UpdateInvoicePreview.

        A list of quotas that would be exceeded by the update  # noqa: E501

        :param exceeded_quotas: The exceeded_quotas of this UpdateInvoicePreview.  # noqa: E501
        :type exceeded_quotas: list[Quota]
        """

        self._exceeded_quotas = exceeded_quotas

    @property
    def immediate(self):
        """Gets the immediate of this UpdateInvoicePreview.  # noqa: E501

        The invoice that will be finalized right after changes are applied  # noqa: E501

        :return: The immediate of this UpdateInvoicePreview.  # noqa: E501
        :rtype: InvoicePreview
        """
        return self._immediate

    @immediate.setter
    def immediate(self, immediate):
        """Sets the immediate of this UpdateInvoicePreview.

        The invoice that will be finalized right after changes are applied  # noqa: E501

        :param immediate: The immediate of this UpdateInvoicePreview.  # noqa: E501
        :type immediate: InvoicePreview
        """
        if self.local_vars_configuration.client_side_validation and immediate is None:  # noqa: E501
            raise ValueError("Invalid value for `immediate`, must not be `None`")  # noqa: E501

        self._immediate = immediate

    @property
    def payment_method(self):
        """Gets the payment_method of this UpdateInvoicePreview.  # noqa: E501

        The payment method that will be billed when this invoice is due.  # noqa: E501

        :return: The payment_method of this UpdateInvoicePreview.  # noqa: E501
        :rtype: CardPublic
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this UpdateInvoicePreview.

        The payment method that will be billed when this invoice is due.  # noqa: E501

        :param payment_method: The payment_method of this UpdateInvoicePreview.  # noqa: E501
        :type payment_method: CardPublic
        """

        self._payment_method = payment_method

    @property
    def upcoming(self):
        """Gets the upcoming of this UpdateInvoicePreview.  # noqa: E501

        The invoice that will be finalized at the end of the current billing cycle  # noqa: E501

        :return: The upcoming of this UpdateInvoicePreview.  # noqa: E501
        :rtype: InvoicePreview
        """
        return self._upcoming

    @upcoming.setter
    def upcoming(self, upcoming):
        """Sets the upcoming of this UpdateInvoicePreview.

        The invoice that will be finalized at the end of the current billing cycle  # noqa: E501

        :param upcoming: The upcoming of this UpdateInvoicePreview.  # noqa: E501
        :type upcoming: InvoicePreview
        """
        if self.local_vars_configuration.client_side_validation and upcoming is None:  # noqa: E501
            raise ValueError("Invalid value for `upcoming`, must not be `None`")  # noqa: E501

        self._upcoming = upcoming

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
        if not isinstance(other, UpdateInvoicePreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateInvoicePreview):
            return True

        return self.to_dict() != other.to_dict()
