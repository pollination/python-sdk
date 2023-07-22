# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.42.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class SubscriptionUpdate(object):
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
        'plan_id': 'int',
        'quantity': 'int'
    }

    attribute_map = {
        'plan_id': 'plan_id',
        'quantity': 'quantity'
    }

    def __init__(self, plan_id=None, quantity=1, local_vars_configuration=None):  # noqa: E501
        """SubscriptionUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._plan_id = None
        self._quantity = None
        self.discriminator = None

        if plan_id is not None:
            self.plan_id = plan_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def plan_id(self):
        """Gets the plan_id of this SubscriptionUpdate.  # noqa: E501

        The Paddle Plan ID to change the subscription to.  # noqa: E501

        :return: The plan_id of this SubscriptionUpdate.  # noqa: E501
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this SubscriptionUpdate.

        The Paddle Plan ID to change the subscription to.  # noqa: E501

        :param plan_id: The plan_id of this SubscriptionUpdate.  # noqa: E501
        :type plan_id: int
        """

        self._plan_id = plan_id

    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionUpdate.  # noqa: E501

        The number of times this subscription is purchased  # noqa: E501

        :return: The quantity of this SubscriptionUpdate.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionUpdate.

        The number of times this subscription is purchased  # noqa: E501

        :param quantity: The quantity of this SubscriptionUpdate.  # noqa: E501
        :type quantity: int
        """

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
        if not isinstance(other, SubscriptionUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionUpdate):
            return True

        return self.to_dict() != other.to_dict()
