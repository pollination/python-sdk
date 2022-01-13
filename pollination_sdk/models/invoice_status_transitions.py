# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.24.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class InvoiceStatusTransitions(object):
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
        'finalized_at': 'datetime',
        'marked_uncollectible_at': 'datetime',
        'paid_at': 'datetime',
        'voided_at': 'datetime'
    }

    attribute_map = {
        'finalized_at': 'finalized_at',
        'marked_uncollectible_at': 'marked_uncollectible_at',
        'paid_at': 'paid_at',
        'voided_at': 'voided_at'
    }

    def __init__(self, finalized_at=None, marked_uncollectible_at=None, paid_at=None, voided_at=None, local_vars_configuration=None):  # noqa: E501
        """InvoiceStatusTransitions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._finalized_at = None
        self._marked_uncollectible_at = None
        self._paid_at = None
        self._voided_at = None
        self.discriminator = None

        if finalized_at is not None:
            self.finalized_at = finalized_at
        if marked_uncollectible_at is not None:
            self.marked_uncollectible_at = marked_uncollectible_at
        if paid_at is not None:
            self.paid_at = paid_at
        if voided_at is not None:
            self.voided_at = voided_at

    @property
    def finalized_at(self):
        """Gets the finalized_at of this InvoiceStatusTransitions.  # noqa: E501


        :return: The finalized_at of this InvoiceStatusTransitions.  # noqa: E501
        :rtype: datetime
        """
        return self._finalized_at

    @finalized_at.setter
    def finalized_at(self, finalized_at):
        """Sets the finalized_at of this InvoiceStatusTransitions.


        :param finalized_at: The finalized_at of this InvoiceStatusTransitions.  # noqa: E501
        :type finalized_at: datetime
        """

        self._finalized_at = finalized_at

    @property
    def marked_uncollectible_at(self):
        """Gets the marked_uncollectible_at of this InvoiceStatusTransitions.  # noqa: E501


        :return: The marked_uncollectible_at of this InvoiceStatusTransitions.  # noqa: E501
        :rtype: datetime
        """
        return self._marked_uncollectible_at

    @marked_uncollectible_at.setter
    def marked_uncollectible_at(self, marked_uncollectible_at):
        """Sets the marked_uncollectible_at of this InvoiceStatusTransitions.


        :param marked_uncollectible_at: The marked_uncollectible_at of this InvoiceStatusTransitions.  # noqa: E501
        :type marked_uncollectible_at: datetime
        """

        self._marked_uncollectible_at = marked_uncollectible_at

    @property
    def paid_at(self):
        """Gets the paid_at of this InvoiceStatusTransitions.  # noqa: E501


        :return: The paid_at of this InvoiceStatusTransitions.  # noqa: E501
        :rtype: datetime
        """
        return self._paid_at

    @paid_at.setter
    def paid_at(self, paid_at):
        """Sets the paid_at of this InvoiceStatusTransitions.


        :param paid_at: The paid_at of this InvoiceStatusTransitions.  # noqa: E501
        :type paid_at: datetime
        """

        self._paid_at = paid_at

    @property
    def voided_at(self):
        """Gets the voided_at of this InvoiceStatusTransitions.  # noqa: E501


        :return: The voided_at of this InvoiceStatusTransitions.  # noqa: E501
        :rtype: datetime
        """
        return self._voided_at

    @voided_at.setter
    def voided_at(self, voided_at):
        """Sets the voided_at of this InvoiceStatusTransitions.


        :param voided_at: The voided_at of this InvoiceStatusTransitions.  # noqa: E501
        :type voided_at: datetime
        """

        self._voided_at = voided_at

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
        if not isinstance(other, InvoiceStatusTransitions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceStatusTransitions):
            return True

        return self.to_dict() != other.to_dict()
