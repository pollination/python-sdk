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


class SubscriptionPlan(object):
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
        'account_types': 'list[AccountType]',
        'billing_options': 'list[BillingOption]',
        'name': 'str',
        'quotas': 'list[QuotaPlan]',
        'slug': 'str',
        'type': 'PlanType'
    }

    attribute_map = {
        'account_types': 'account_types',
        'billing_options': 'billing_options',
        'name': 'name',
        'quotas': 'quotas',
        'slug': 'slug',
        'type': 'type'
    }

    def __init__(self, account_types=None, billing_options=[], name=None, quotas=[], slug=None, type=None, local_vars_configuration=None):  # noqa: E501
        """SubscriptionPlan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_types = None
        self._billing_options = None
        self._name = None
        self._quotas = None
        self._slug = None
        self._type = None
        self.discriminator = None

        self.account_types = account_types
        if billing_options is not None:
            self.billing_options = billing_options
        self.name = name
        if quotas is not None:
            self.quotas = quotas
        self.slug = slug
        self.type = type

    @property
    def account_types(self):
        """Gets the account_types of this SubscriptionPlan.  # noqa: E501

        The types of account to which the plan can be applied  # noqa: E501

        :return: The account_types of this SubscriptionPlan.  # noqa: E501
        :rtype: list[AccountType]
        """
        return self._account_types

    @account_types.setter
    def account_types(self, account_types):
        """Sets the account_types of this SubscriptionPlan.

        The types of account to which the plan can be applied  # noqa: E501

        :param account_types: The account_types of this SubscriptionPlan.  # noqa: E501
        :type account_types: list[AccountType]
        """
        if self.local_vars_configuration.client_side_validation and account_types is None:  # noqa: E501
            raise ValueError("Invalid value for `account_types`, must not be `None`")  # noqa: E501

        self._account_types = account_types

    @property
    def billing_options(self):
        """Gets the billing_options of this SubscriptionPlan.  # noqa: E501

        The billing options for this plan  # noqa: E501

        :return: The billing_options of this SubscriptionPlan.  # noqa: E501
        :rtype: list[BillingOption]
        """
        return self._billing_options

    @billing_options.setter
    def billing_options(self, billing_options):
        """Sets the billing_options of this SubscriptionPlan.

        The billing options for this plan  # noqa: E501

        :param billing_options: The billing_options of this SubscriptionPlan.  # noqa: E501
        :type billing_options: list[BillingOption]
        """

        self._billing_options = billing_options

    @property
    def name(self):
        """Gets the name of this SubscriptionPlan.  # noqa: E501

        A name of the config plan used to create this subscription  # noqa: E501

        :return: The name of this SubscriptionPlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionPlan.

        A name of the config plan used to create this subscription  # noqa: E501

        :param name: The name of this SubscriptionPlan.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def quotas(self):
        """Gets the quotas of this SubscriptionPlan.  # noqa: E501

        A list of quota plans for a given subscription  # noqa: E501

        :return: The quotas of this SubscriptionPlan.  # noqa: E501
        :rtype: list[QuotaPlan]
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        """Sets the quotas of this SubscriptionPlan.

        A list of quota plans for a given subscription  # noqa: E501

        :param quotas: The quotas of this SubscriptionPlan.  # noqa: E501
        :type quotas: list[QuotaPlan]
        """

        self._quotas = quotas

    @property
    def slug(self):
        """Gets the slug of this SubscriptionPlan.  # noqa: E501

        A slug of the config plan used to create this subscription  # noqa: E501

        :return: The slug of this SubscriptionPlan.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this SubscriptionPlan.

        A slug of the config plan used to create this subscription  # noqa: E501

        :param slug: The slug of this SubscriptionPlan.  # noqa: E501
        :type slug: str
        """
        if self.local_vars_configuration.client_side_validation and slug is None:  # noqa: E501
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

    @property
    def type(self):
        """Gets the type of this SubscriptionPlan.  # noqa: E501

        The type of plan  # noqa: E501

        :return: The type of this SubscriptionPlan.  # noqa: E501
        :rtype: PlanType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubscriptionPlan.

        The type of plan  # noqa: E501

        :param type: The type of this SubscriptionPlan.  # noqa: E501
        :type type: PlanType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, SubscriptionPlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionPlan):
            return True

        return self.to_dict() != other.to_dict()
