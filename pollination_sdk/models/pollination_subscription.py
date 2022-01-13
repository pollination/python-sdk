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


class PollinationSubscription(object):
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
        'account_id': 'str',
        'current_period_end': 'datetime',
        'current_period_start': 'datetime',
        'external_id': 'str',
        'id': 'str',
        'quota_extensions': 'list[QuotaExtension]',
        'subscription_plan': 'SubscriptionPlan'
    }

    attribute_map = {
        'account_id': 'account_id',
        'current_period_end': 'current_period_end',
        'current_period_start': 'current_period_start',
        'external_id': 'external_id',
        'id': 'id',
        'quota_extensions': 'quota_extensions',
        'subscription_plan': 'subscription_plan'
    }

    def __init__(self, account_id=None, current_period_end=None, current_period_start=None, external_id=None, id=None, quota_extensions=[], subscription_plan=None, local_vars_configuration=None):  # noqa: E501
        """PollinationSubscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._current_period_end = None
        self._current_period_start = None
        self._external_id = None
        self._id = None
        self._quota_extensions = None
        self._subscription_plan = None
        self.discriminator = None

        self.account_id = account_id
        self.current_period_end = current_period_end
        self.current_period_start = current_period_start
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if quota_extensions is not None:
            self.quota_extensions = quota_extensions
        self.subscription_plan = subscription_plan

    @property
    def account_id(self):
        """Gets the account_id of this PollinationSubscription.  # noqa: E501

        The ID of the account this subscription applies to  # noqa: E501

        :return: The account_id of this PollinationSubscription.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PollinationSubscription.

        The ID of the account this subscription applies to  # noqa: E501

        :param account_id: The account_id of this PollinationSubscription.  # noqa: E501
        :type account_id: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def current_period_end(self):
        """Gets the current_period_end of this PollinationSubscription.  # noqa: E501

        The end of the current subscription period  # noqa: E501

        :return: The current_period_end of this PollinationSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._current_period_end

    @current_period_end.setter
    def current_period_end(self, current_period_end):
        """Sets the current_period_end of this PollinationSubscription.

        The end of the current subscription period  # noqa: E501

        :param current_period_end: The current_period_end of this PollinationSubscription.  # noqa: E501
        :type current_period_end: datetime
        """
        if self.local_vars_configuration.client_side_validation and current_period_end is None:  # noqa: E501
            raise ValueError("Invalid value for `current_period_end`, must not be `None`")  # noqa: E501

        self._current_period_end = current_period_end

    @property
    def current_period_start(self):
        """Gets the current_period_start of this PollinationSubscription.  # noqa: E501

        The_start of the current subscription period  # noqa: E501

        :return: The current_period_start of this PollinationSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._current_period_start

    @current_period_start.setter
    def current_period_start(self, current_period_start):
        """Sets the current_period_start of this PollinationSubscription.

        The_start of the current subscription period  # noqa: E501

        :param current_period_start: The current_period_start of this PollinationSubscription.  # noqa: E501
        :type current_period_start: datetime
        """
        if self.local_vars_configuration.client_side_validation and current_period_start is None:  # noqa: E501
            raise ValueError("Invalid value for `current_period_start`, must not be `None`")  # noqa: E501

        self._current_period_start = current_period_start

    @property
    def external_id(self):
        """Gets the external_id of this PollinationSubscription.  # noqa: E501

        The ID of this subscription  # noqa: E501

        :return: The external_id of this PollinationSubscription.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PollinationSubscription.

        The ID of this subscription  # noqa: E501

        :param external_id: The external_id of this PollinationSubscription.  # noqa: E501
        :type external_id: str
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this PollinationSubscription.  # noqa: E501

        The unique ID of this subscription  # noqa: E501

        :return: The id of this PollinationSubscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PollinationSubscription.

        The unique ID of this subscription  # noqa: E501

        :param id: The id of this PollinationSubscription.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def quota_extensions(self):
        """Gets the quota_extensions of this PollinationSubscription.  # noqa: E501

        A list of quota extension plans for a given subscription  # noqa: E501

        :return: The quota_extensions of this PollinationSubscription.  # noqa: E501
        :rtype: list[QuotaExtension]
        """
        return self._quota_extensions

    @quota_extensions.setter
    def quota_extensions(self, quota_extensions):
        """Sets the quota_extensions of this PollinationSubscription.

        A list of quota extension plans for a given subscription  # noqa: E501

        :param quota_extensions: The quota_extensions of this PollinationSubscription.  # noqa: E501
        :type quota_extensions: list[QuotaExtension]
        """

        self._quota_extensions = quota_extensions

    @property
    def subscription_plan(self):
        """Gets the subscription_plan of this PollinationSubscription.  # noqa: E501

        A subscription plan  # noqa: E501

        :return: The subscription_plan of this PollinationSubscription.  # noqa: E501
        :rtype: SubscriptionPlan
        """
        return self._subscription_plan

    @subscription_plan.setter
    def subscription_plan(self, subscription_plan):
        """Sets the subscription_plan of this PollinationSubscription.

        A subscription plan  # noqa: E501

        :param subscription_plan: The subscription_plan of this PollinationSubscription.  # noqa: E501
        :type subscription_plan: SubscriptionPlan
        """
        if self.local_vars_configuration.client_side_validation and subscription_plan is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_plan`, must not be `None`")  # noqa: E501

        self._subscription_plan = subscription_plan

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
        if not isinstance(other, PollinationSubscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PollinationSubscription):
            return True

        return self.to_dict() != other.to_dict()
