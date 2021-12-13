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


class UserPermission(object):
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
        'admin': 'bool',
        'read': 'bool',
        'write': 'bool'
    }

    attribute_map = {
        'admin': 'admin',
        'read': 'read',
        'write': 'write'
    }

    def __init__(self, admin=False, read=False, write=False, local_vars_configuration=None):  # noqa: E501
        """UserPermission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin = None
        self._read = None
        self._write = None
        self.discriminator = None

        if admin is not None:
            self.admin = admin
        if read is not None:
            self.read = read
        if write is not None:
            self.write = write

    @property
    def admin(self):
        """Gets the admin of this UserPermission.  # noqa: E501

        The user has admin permission to this resource  # noqa: E501

        :return: The admin of this UserPermission.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this UserPermission.

        The user has admin permission to this resource  # noqa: E501

        :param admin: The admin of this UserPermission.  # noqa: E501
        :type admin: bool
        """

        self._admin = admin

    @property
    def read(self):
        """Gets the read of this UserPermission.  # noqa: E501

        The user has read permission on this resource  # noqa: E501

        :return: The read of this UserPermission.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this UserPermission.

        The user has read permission on this resource  # noqa: E501

        :param read: The read of this UserPermission.  # noqa: E501
        :type read: bool
        """

        self._read = read

    @property
    def write(self):
        """Gets the write of this UserPermission.  # noqa: E501

        The user has write permission on this resource  # noqa: E501

        :return: The write of this UserPermission.  # noqa: E501
        :rtype: bool
        """
        return self._write

    @write.setter
    def write(self, write):
        """Sets the write of this UserPermission.

        The user has write permission on this resource  # noqa: E501

        :param write: The write of this UserPermission.  # noqa: E501
        :type write: bool
        """

        self._write = write

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
        if not isinstance(other, UserPermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserPermission):
            return True

        return self.to_dict() != other.to_dict()