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


class Invoice(object):
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
        'auto_advance': 'bool',
        'collection_method': 'str',
        'currency': 'str',
        'customer': 'str',
        'description': 'str',
        'hosted_invoice_url': 'str',
        'id': 'str',
        'lines': 'LineItemList',
        'metadata': 'object',
        'period_end': 'datetime',
        'period_start': 'datetime',
        'status': 'InvoiceStatus',
        'status_transitions': 'InvoiceStatusTransitions',
        'subscription': 'str',
        'total': 'int'
    }

    attribute_map = {
        'auto_advance': 'auto_advance',
        'collection_method': 'collection_method',
        'currency': 'currency',
        'customer': 'customer',
        'description': 'description',
        'hosted_invoice_url': 'hosted_invoice_url',
        'id': 'id',
        'lines': 'lines',
        'metadata': 'metadata',
        'period_end': 'period_end',
        'period_start': 'period_start',
        'status': 'status',
        'status_transitions': 'status_transitions',
        'subscription': 'subscription',
        'total': 'total'
    }

    def __init__(self, auto_advance=None, collection_method=None, currency=None, customer=None, description=None, hosted_invoice_url=None, id=None, lines=None, metadata=None, period_end=None, period_start=None, status=None, status_transitions=None, subscription=None, total=None, local_vars_configuration=None):  # noqa: E501
        """Invoice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auto_advance = None
        self._collection_method = None
        self._currency = None
        self._customer = None
        self._description = None
        self._hosted_invoice_url = None
        self._id = None
        self._lines = None
        self._metadata = None
        self._period_end = None
        self._period_start = None
        self._status = None
        self._status_transitions = None
        self._subscription = None
        self._total = None
        self.discriminator = None

        if auto_advance is not None:
            self.auto_advance = auto_advance
        self.collection_method = collection_method
        self.currency = currency
        self.customer = customer
        if description is not None:
            self.description = description
        if hosted_invoice_url is not None:
            self.hosted_invoice_url = hosted_invoice_url
        self.id = id
        self.lines = lines
        if metadata is not None:
            self.metadata = metadata
        self.period_end = period_end
        self.period_start = period_start
        self.status = status
        self.status_transitions = status_transitions
        if subscription is not None:
            self.subscription = subscription
        self.total = total

    @property
    def auto_advance(self):
        """Gets the auto_advance of this Invoice.  # noqa: E501


        :return: The auto_advance of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._auto_advance

    @auto_advance.setter
    def auto_advance(self, auto_advance):
        """Sets the auto_advance of this Invoice.


        :param auto_advance: The auto_advance of this Invoice.  # noqa: E501
        :type auto_advance: bool
        """

        self._auto_advance = auto_advance

    @property
    def collection_method(self):
        """Gets the collection_method of this Invoice.  # noqa: E501


        :return: The collection_method of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._collection_method

    @collection_method.setter
    def collection_method(self, collection_method):
        """Sets the collection_method of this Invoice.


        :param collection_method: The collection_method of this Invoice.  # noqa: E501
        :type collection_method: str
        """
        if self.local_vars_configuration.client_side_validation and collection_method is None:  # noqa: E501
            raise ValueError("Invalid value for `collection_method`, must not be `None`")  # noqa: E501

        self._collection_method = collection_method

    @property
    def currency(self):
        """Gets the currency of this Invoice.  # noqa: E501


        :return: The currency of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Invoice.


        :param currency: The currency of this Invoice.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def customer(self):
        """Gets the customer of this Invoice.  # noqa: E501


        :return: The customer of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Invoice.


        :param customer: The customer of this Invoice.  # noqa: E501
        :type customer: str
        """
        if self.local_vars_configuration.client_side_validation and customer is None:  # noqa: E501
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def description(self):
        """Gets the description of this Invoice.  # noqa: E501


        :return: The description of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Invoice.


        :param description: The description of this Invoice.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def hosted_invoice_url(self):
        """Gets the hosted_invoice_url of this Invoice.  # noqa: E501


        :return: The hosted_invoice_url of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._hosted_invoice_url

    @hosted_invoice_url.setter
    def hosted_invoice_url(self, hosted_invoice_url):
        """Sets the hosted_invoice_url of this Invoice.


        :param hosted_invoice_url: The hosted_invoice_url of this Invoice.  # noqa: E501
        :type hosted_invoice_url: str
        """

        self._hosted_invoice_url = hosted_invoice_url

    @property
    def id(self):
        """Gets the id of this Invoice.  # noqa: E501


        :return: The id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invoice.


        :param id: The id of this Invoice.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def lines(self):
        """Gets the lines of this Invoice.  # noqa: E501


        :return: The lines of this Invoice.  # noqa: E501
        :rtype: LineItemList
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this Invoice.


        :param lines: The lines of this Invoice.  # noqa: E501
        :type lines: LineItemList
        """
        if self.local_vars_configuration.client_side_validation and lines is None:  # noqa: E501
            raise ValueError("Invalid value for `lines`, must not be `None`")  # noqa: E501

        self._lines = lines

    @property
    def metadata(self):
        """Gets the metadata of this Invoice.  # noqa: E501


        :return: The metadata of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Invoice.


        :param metadata: The metadata of this Invoice.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def period_end(self):
        """Gets the period_end of this Invoice.  # noqa: E501


        :return: The period_end of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """Sets the period_end of this Invoice.


        :param period_end: The period_end of this Invoice.  # noqa: E501
        :type period_end: datetime
        """
        if self.local_vars_configuration.client_side_validation and period_end is None:  # noqa: E501
            raise ValueError("Invalid value for `period_end`, must not be `None`")  # noqa: E501

        self._period_end = period_end

    @property
    def period_start(self):
        """Gets the period_start of this Invoice.  # noqa: E501


        :return: The period_start of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this Invoice.


        :param period_start: The period_start of this Invoice.  # noqa: E501
        :type period_start: datetime
        """
        if self.local_vars_configuration.client_side_validation and period_start is None:  # noqa: E501
            raise ValueError("Invalid value for `period_start`, must not be `None`")  # noqa: E501

        self._period_start = period_start

    @property
    def status(self):
        """Gets the status of this Invoice.  # noqa: E501


        :return: The status of this Invoice.  # noqa: E501
        :rtype: InvoiceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.


        :param status: The status of this Invoice.  # noqa: E501
        :type status: InvoiceStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_transitions(self):
        """Gets the status_transitions of this Invoice.  # noqa: E501


        :return: The status_transitions of this Invoice.  # noqa: E501
        :rtype: InvoiceStatusTransitions
        """
        return self._status_transitions

    @status_transitions.setter
    def status_transitions(self, status_transitions):
        """Sets the status_transitions of this Invoice.


        :param status_transitions: The status_transitions of this Invoice.  # noqa: E501
        :type status_transitions: InvoiceStatusTransitions
        """
        if self.local_vars_configuration.client_side_validation and status_transitions is None:  # noqa: E501
            raise ValueError("Invalid value for `status_transitions`, must not be `None`")  # noqa: E501

        self._status_transitions = status_transitions

    @property
    def subscription(self):
        """Gets the subscription of this Invoice.  # noqa: E501


        :return: The subscription of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this Invoice.


        :param subscription: The subscription of this Invoice.  # noqa: E501
        :type subscription: str
        """

        self._subscription = subscription

    @property
    def total(self):
        """Gets the total of this Invoice.  # noqa: E501


        :return: The total of this Invoice.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Invoice.


        :param total: The total of this Invoice.  # noqa: E501
        :type total: int
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, Invoice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Invoice):
            return True

        return self.to_dict() != other.to_dict()
