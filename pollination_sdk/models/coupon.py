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


class Coupon(object):
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
        'amount_off': 'float',
        'duration': 'CouponDuration',
        'duration_in_months': 'int',
        'id': 'str',
        'metadata': 'object',
        'name': 'str',
        'percent_off': 'float',
        'valid': 'bool'
    }

    attribute_map = {
        'amount_off': 'amount_off',
        'duration': 'duration',
        'duration_in_months': 'duration_in_months',
        'id': 'id',
        'metadata': 'metadata',
        'name': 'name',
        'percent_off': 'percent_off',
        'valid': 'valid'
    }

    def __init__(self, amount_off=None, duration=None, duration_in_months=None, id=None, metadata=None, name=None, percent_off=None, valid=None, local_vars_configuration=None):  # noqa: E501
        """Coupon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount_off = None
        self._duration = None
        self._duration_in_months = None
        self._id = None
        self._metadata = None
        self._name = None
        self._percent_off = None
        self._valid = None
        self.discriminator = None

        if amount_off is not None:
            self.amount_off = amount_off
        self.duration = duration
        if duration_in_months is not None:
            self.duration_in_months = duration_in_months
        self.id = id
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if percent_off is not None:
            self.percent_off = percent_off
        self.valid = valid

    @property
    def amount_off(self):
        """Gets the amount_off of this Coupon.  # noqa: E501


        :return: The amount_off of this Coupon.  # noqa: E501
        :rtype: float
        """
        return self._amount_off

    @amount_off.setter
    def amount_off(self, amount_off):
        """Sets the amount_off of this Coupon.


        :param amount_off: The amount_off of this Coupon.  # noqa: E501
        :type amount_off: float
        """

        self._amount_off = amount_off

    @property
    def duration(self):
        """Gets the duration of this Coupon.  # noqa: E501


        :return: The duration of this Coupon.  # noqa: E501
        :rtype: CouponDuration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Coupon.


        :param duration: The duration of this Coupon.  # noqa: E501
        :type duration: CouponDuration
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def duration_in_months(self):
        """Gets the duration_in_months of this Coupon.  # noqa: E501


        :return: The duration_in_months of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._duration_in_months

    @duration_in_months.setter
    def duration_in_months(self, duration_in_months):
        """Sets the duration_in_months of this Coupon.


        :param duration_in_months: The duration_in_months of this Coupon.  # noqa: E501
        :type duration_in_months: int
        """

        self._duration_in_months = duration_in_months

    @property
    def id(self):
        """Gets the id of this Coupon.  # noqa: E501


        :return: The id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Coupon.


        :param id: The id of this Coupon.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this Coupon.  # noqa: E501


        :return: The metadata of this Coupon.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Coupon.


        :param metadata: The metadata of this Coupon.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this Coupon.  # noqa: E501


        :return: The name of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Coupon.


        :param name: The name of this Coupon.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def percent_off(self):
        """Gets the percent_off of this Coupon.  # noqa: E501


        :return: The percent_off of this Coupon.  # noqa: E501
        :rtype: float
        """
        return self._percent_off

    @percent_off.setter
    def percent_off(self, percent_off):
        """Sets the percent_off of this Coupon.


        :param percent_off: The percent_off of this Coupon.  # noqa: E501
        :type percent_off: float
        """

        self._percent_off = percent_off

    @property
    def valid(self):
        """Gets the valid of this Coupon.  # noqa: E501


        :return: The valid of this Coupon.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this Coupon.


        :param valid: The valid of this Coupon.  # noqa: E501
        :type valid: bool
        """
        if self.local_vars_configuration.client_side_validation and valid is None:  # noqa: E501
            raise ValueError("Invalid value for `valid`, must not be `None`")  # noqa: E501

        self._valid = valid

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
        if not isinstance(other, Coupon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Coupon):
            return True

        return self.to_dict() != other.to_dict()
