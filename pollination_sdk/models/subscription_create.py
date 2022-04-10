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


class SubscriptionCreate(object):
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
        'account': 'str',
        'plan_id': 'int',
        'quantity': 'int'
    }

    attribute_map = {
        'account': 'account',
        'plan_id': 'plan_id',
        'quantity': 'quantity'
    }

    def __init__(self, account=None, plan_id=None, quantity=1, local_vars_configuration=None):  # noqa: E501
        """SubscriptionCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account = None
        self._plan_id = None
        self._quantity = None
        self.discriminator = None

        self.account = account
        self.plan_id = plan_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def account(self):
        """Gets the account of this SubscriptionCreate.  # noqa: E501

        The name of the account to create subscription for  # noqa: E501

        :return: The account of this SubscriptionCreate.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this SubscriptionCreate.

        The name of the account to create subscription for  # noqa: E501

        :param account: The account of this SubscriptionCreate.  # noqa: E501
        :type account: str
        """
        if self.local_vars_configuration.client_side_validation and account is None:  # noqa: E501
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def plan_id(self):
        """Gets the plan_id of this SubscriptionCreate.  # noqa: E501

        The ID of the plan to subscribe to  # noqa: E501

        :return: The plan_id of this SubscriptionCreate.  # noqa: E501
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this SubscriptionCreate.

        The ID of the plan to subscribe to  # noqa: E501

        :param plan_id: The plan_id of this SubscriptionCreate.  # noqa: E501
        :type plan_id: int
        """
        if self.local_vars_configuration.client_side_validation and plan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `plan_id`, must not be `None`")  # noqa: E501

        self._plan_id = plan_id

    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionCreate.  # noqa: E501

        The number of subscriptions to create  # noqa: E501

        :return: The quantity of this SubscriptionCreate.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionCreate.

        The number of subscriptions to create  # noqa: E501

        :param quantity: The quantity of this SubscriptionCreate.  # noqa: E501
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
        if not isinstance(other, SubscriptionCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionCreate):
            return True

        return self.to_dict() != other.to_dict()
