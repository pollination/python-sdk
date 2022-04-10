# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.29.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class SubscriptionUpdateDryRun(object):
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
        'exceeded_quotas': 'list[Quota]'
    }

    attribute_map = {
        'exceeded_quotas': 'exceeded_quotas'
    }

    def __init__(self, exceeded_quotas=[], local_vars_configuration=None):  # noqa: E501
        """SubscriptionUpdateDryRun - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exceeded_quotas = None
        self.discriminator = None

        if exceeded_quotas is not None:
            self.exceeded_quotas = exceeded_quotas

    @property
    def exceeded_quotas(self):
        """Gets the exceeded_quotas of this SubscriptionUpdateDryRun.  # noqa: E501

        A list of quotas exceeded by a proposed subscription update  # noqa: E501

        :return: The exceeded_quotas of this SubscriptionUpdateDryRun.  # noqa: E501
        :rtype: list[Quota]
        """
        return self._exceeded_quotas

    @exceeded_quotas.setter
    def exceeded_quotas(self, exceeded_quotas):
        """Sets the exceeded_quotas of this SubscriptionUpdateDryRun.

        A list of quotas exceeded by a proposed subscription update  # noqa: E501

        :param exceeded_quotas: The exceeded_quotas of this SubscriptionUpdateDryRun.  # noqa: E501
        :type exceeded_quotas: list[Quota]
        """

        self._exceeded_quotas = exceeded_quotas

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
        if not isinstance(other, SubscriptionUpdateDryRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionUpdateDryRun):
            return True

        return self.to_dict() != other.to_dict()
