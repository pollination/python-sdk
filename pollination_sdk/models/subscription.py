# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: v0.20.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Subscription(object):
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
        'cancel_at_period_end': 'bool',
        'current_period_end': 'datetime',
        'current_period_start': 'datetime',
        'customer': 'str',
        'default_payment_method': 'str',
        'id': 'str',
        'items': 'SubscriptionItemPublicList',
        'latest_invoice': 'str',
        'metadata': 'object',
        'schedule': 'str'
    }

    attribute_map = {
        'cancel_at_period_end': 'cancel_at_period_end',
        'current_period_end': 'current_period_end',
        'current_period_start': 'current_period_start',
        'customer': 'customer',
        'default_payment_method': 'default_payment_method',
        'id': 'id',
        'items': 'items',
        'latest_invoice': 'latest_invoice',
        'metadata': 'metadata',
        'schedule': 'schedule'
    }

    def __init__(self, cancel_at_period_end=None, current_period_end=None, current_period_start=None, customer=None, default_payment_method=None, id=None, items=None, latest_invoice=None, metadata=None, schedule=None, local_vars_configuration=None):  # noqa: E501
        """Subscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cancel_at_period_end = None
        self._current_period_end = None
        self._current_period_start = None
        self._customer = None
        self._default_payment_method = None
        self._id = None
        self._items = None
        self._latest_invoice = None
        self._metadata = None
        self._schedule = None
        self.discriminator = None

        self.cancel_at_period_end = cancel_at_period_end
        self.current_period_end = current_period_end
        self.current_period_start = current_period_start
        self.customer = customer
        if default_payment_method is not None:
            self.default_payment_method = default_payment_method
        self.id = id
        self.items = items
        self.latest_invoice = latest_invoice
        if metadata is not None:
            self.metadata = metadata
        if schedule is not None:
            self.schedule = schedule

    @property
    def cancel_at_period_end(self):
        """Gets the cancel_at_period_end of this Subscription.  # noqa: E501


        :return: The cancel_at_period_end of this Subscription.  # noqa: E501
        :rtype: bool
        """
        return self._cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, cancel_at_period_end):
        """Sets the cancel_at_period_end of this Subscription.


        :param cancel_at_period_end: The cancel_at_period_end of this Subscription.  # noqa: E501
        :type cancel_at_period_end: bool
        """
        if self.local_vars_configuration.client_side_validation and cancel_at_period_end is None:  # noqa: E501
            raise ValueError("Invalid value for `cancel_at_period_end`, must not be `None`")  # noqa: E501

        self._cancel_at_period_end = cancel_at_period_end

    @property
    def current_period_end(self):
        """Gets the current_period_end of this Subscription.  # noqa: E501


        :return: The current_period_end of this Subscription.  # noqa: E501
        :rtype: datetime
        """
        return self._current_period_end

    @current_period_end.setter
    def current_period_end(self, current_period_end):
        """Sets the current_period_end of this Subscription.


        :param current_period_end: The current_period_end of this Subscription.  # noqa: E501
        :type current_period_end: datetime
        """
        if self.local_vars_configuration.client_side_validation and current_period_end is None:  # noqa: E501
            raise ValueError("Invalid value for `current_period_end`, must not be `None`")  # noqa: E501

        self._current_period_end = current_period_end

    @property
    def current_period_start(self):
        """Gets the current_period_start of this Subscription.  # noqa: E501


        :return: The current_period_start of this Subscription.  # noqa: E501
        :rtype: datetime
        """
        return self._current_period_start

    @current_period_start.setter
    def current_period_start(self, current_period_start):
        """Sets the current_period_start of this Subscription.


        :param current_period_start: The current_period_start of this Subscription.  # noqa: E501
        :type current_period_start: datetime
        """
        if self.local_vars_configuration.client_side_validation and current_period_start is None:  # noqa: E501
            raise ValueError("Invalid value for `current_period_start`, must not be `None`")  # noqa: E501

        self._current_period_start = current_period_start

    @property
    def customer(self):
        """Gets the customer of this Subscription.  # noqa: E501


        :return: The customer of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Subscription.


        :param customer: The customer of this Subscription.  # noqa: E501
        :type customer: str
        """
        if self.local_vars_configuration.client_side_validation and customer is None:  # noqa: E501
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def default_payment_method(self):
        """Gets the default_payment_method of this Subscription.  # noqa: E501


        :return: The default_payment_method of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, default_payment_method):
        """Sets the default_payment_method of this Subscription.


        :param default_payment_method: The default_payment_method of this Subscription.  # noqa: E501
        :type default_payment_method: str
        """

        self._default_payment_method = default_payment_method

    @property
    def id(self):
        """Gets the id of this Subscription.  # noqa: E501


        :return: The id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscription.


        :param id: The id of this Subscription.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def items(self):
        """Gets the items of this Subscription.  # noqa: E501


        :return: The items of this Subscription.  # noqa: E501
        :rtype: SubscriptionItemPublicList
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Subscription.


        :param items: The items of this Subscription.  # noqa: E501
        :type items: SubscriptionItemPublicList
        """
        if self.local_vars_configuration.client_side_validation and items is None:  # noqa: E501
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def latest_invoice(self):
        """Gets the latest_invoice of this Subscription.  # noqa: E501


        :return: The latest_invoice of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._latest_invoice

    @latest_invoice.setter
    def latest_invoice(self, latest_invoice):
        """Sets the latest_invoice of this Subscription.


        :param latest_invoice: The latest_invoice of this Subscription.  # noqa: E501
        :type latest_invoice: str
        """
        if self.local_vars_configuration.client_side_validation and latest_invoice is None:  # noqa: E501
            raise ValueError("Invalid value for `latest_invoice`, must not be `None`")  # noqa: E501

        self._latest_invoice = latest_invoice

    @property
    def metadata(self):
        """Gets the metadata of this Subscription.  # noqa: E501


        :return: The metadata of this Subscription.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Subscription.


        :param metadata: The metadata of this Subscription.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def schedule(self):
        """Gets the schedule of this Subscription.  # noqa: E501


        :return: The schedule of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this Subscription.


        :param schedule: The schedule of this Subscription.  # noqa: E501
        :type schedule: str
        """

        self._schedule = schedule

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
        if not isinstance(other, Subscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Subscription):
            return True

        return self.to_dict() != other.to_dict()