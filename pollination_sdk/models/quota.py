# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.33.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Quota(object):
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
        'description': 'str',
        'display_name': 'str',
        'enforced': 'bool',
        'exceeded': 'bool',
        'id': 'str',
        'limit': 'float',
        'owner': 'AccountPublic',
        'period_start': 'datetime',
        'resets': 'bool',
        'type': 'QuotaType',
        'unit': 'str',
        'usage': 'float'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'enforced': 'enforced',
        'exceeded': 'exceeded',
        'id': 'id',
        'limit': 'limit',
        'owner': 'owner',
        'period_start': 'period_start',
        'resets': 'resets',
        'type': 'type',
        'unit': 'unit',
        'usage': 'usage'
    }

    def __init__(self, description=None, display_name=None, enforced=False, exceeded=False, id=None, limit=None, owner=None, period_start=None, resets=False, type=None, unit=None, usage=None, local_vars_configuration=None):  # noqa: E501
        """Quota - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._display_name = None
        self._enforced = None
        self._exceeded = None
        self._id = None
        self._limit = None
        self._owner = None
        self._period_start = None
        self._resets = None
        self._type = None
        self._unit = None
        self._usage = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if enforced is not None:
            self.enforced = enforced
        if exceeded is not None:
            self.exceeded = exceeded
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        self.owner = owner
        if period_start is not None:
            self.period_start = period_start
        if resets is not None:
            self.resets = resets
        self.type = type
        if unit is not None:
            self.unit = unit
        if usage is not None:
            self.usage = usage

    @property
    def description(self):
        """Gets the description of this Quota.  # noqa: E501

        The description  # noqa: E501

        :return: The description of this Quota.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Quota.

        The description  # noqa: E501

        :param description: The description of this Quota.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this Quota.  # noqa: E501

        The human-readable name  # noqa: E501

        :return: The display_name of this Quota.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Quota.

        The human-readable name  # noqa: E501

        :param display_name: The display_name of this Quota.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def enforced(self):
        """Gets the enforced of this Quota.  # noqa: E501

        Whether the limit triggers a blocking response from the server  # noqa: E501

        :return: The enforced of this Quota.  # noqa: E501
        :rtype: bool
        """
        return self._enforced

    @enforced.setter
    def enforced(self, enforced):
        """Sets the enforced of this Quota.

        Whether the limit triggers a blocking response from the server  # noqa: E501

        :param enforced: The enforced of this Quota.  # noqa: E501
        :type enforced: bool
        """

        self._enforced = enforced

    @property
    def exceeded(self):
        """Gets the exceeded of this Quota.  # noqa: E501

        Whether the resource usage is greater than or equal to the limit  # noqa: E501

        :return: The exceeded of this Quota.  # noqa: E501
        :rtype: bool
        """
        return self._exceeded

    @exceeded.setter
    def exceeded(self, exceeded):
        """Sets the exceeded of this Quota.

        Whether the resource usage is greater than or equal to the limit  # noqa: E501

        :param exceeded: The exceeded of this Quota.  # noqa: E501
        :type exceeded: bool
        """

        self._exceeded = exceeded

    @property
    def id(self):
        """Gets the id of this Quota.  # noqa: E501

        The unique ID for this Quota  # noqa: E501

        :return: The id of this Quota.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Quota.

        The unique ID for this Quota  # noqa: E501

        :param id: The id of this Quota.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def limit(self):
        """Gets the limit of this Quota.  # noqa: E501

        The maximum amount of a resource the account can consume  # noqa: E501

        :return: The limit of this Quota.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Quota.

        The maximum amount of a resource the account can consume  # noqa: E501

        :param limit: The limit of this Quota.  # noqa: E501
        :type limit: float
        """

        self._limit = limit

    @property
    def owner(self):
        """Gets the owner of this Quota.  # noqa: E501

        The quota owner  # noqa: E501

        :return: The owner of this Quota.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Quota.

        The quota owner  # noqa: E501

        :param owner: The owner of this Quota.  # noqa: E501
        :type owner: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def period_start(self):
        """Gets the period_start of this Quota.  # noqa: E501

        The start of the quota usage tracking period  # noqa: E501

        :return: The period_start of this Quota.  # noqa: E501
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this Quota.

        The start of the quota usage tracking period  # noqa: E501

        :param period_start: The period_start of this Quota.  # noqa: E501
        :type period_start: datetime
        """

        self._period_start = period_start

    @property
    def resets(self):
        """Gets the resets of this Quota.  # noqa: E501

        Whether consumption is reset to 0 every billing period  # noqa: E501

        :return: The resets of this Quota.  # noqa: E501
        :rtype: bool
        """
        return self._resets

    @resets.setter
    def resets(self, resets):
        """Sets the resets of this Quota.

        Whether consumption is reset to 0 every billing period  # noqa: E501

        :param resets: The resets of this Quota.  # noqa: E501
        :type resets: bool
        """

        self._resets = resets

    @property
    def type(self):
        """Gets the type of this Quota.  # noqa: E501

        The type of resource  # noqa: E501

        :return: The type of this Quota.  # noqa: E501
        :rtype: QuotaType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Quota.

        The type of resource  # noqa: E501

        :param type: The type of this Quota.  # noqa: E501
        :type type: QuotaType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def unit(self):
        """Gets the unit of this Quota.  # noqa: E501

        The unit in which the usage and limit are measured  # noqa: E501

        :return: The unit of this Quota.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Quota.

        The unit in which the usage and limit are measured  # noqa: E501

        :param unit: The unit of this Quota.  # noqa: E501
        :type unit: str
        """

        self._unit = unit

    @property
    def usage(self):
        """Gets the usage of this Quota.  # noqa: E501

        The current amount of a resource allocated to the account linked to the subscription  # noqa: E501

        :return: The usage of this Quota.  # noqa: E501
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this Quota.

        The current amount of a resource allocated to the account linked to the subscription  # noqa: E501

        :param usage: The usage of this Quota.  # noqa: E501
        :type usage: float
        """
        if (self.local_vars_configuration.client_side_validation and
                usage is not None and usage < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `usage`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._usage = usage

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
        if not isinstance(other, Quota):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Quota):
            return True

        return self.to_dict() != other.to_dict()
