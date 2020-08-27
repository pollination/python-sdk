# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.8.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class RepositoryPermissions(object):
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
        'contribute': 'bool',
        'read': 'bool'
    }

    attribute_map = {
        'admin': 'admin',
        'contribute': 'contribute',
        'read': 'read'
    }

    def __init__(self, admin=None, contribute=None, read=None, local_vars_configuration=None):  # noqa: E501
        """RepositoryPermissions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin = None
        self._contribute = None
        self._read = None
        self.discriminator = None

        self.admin = admin
        self.contribute = contribute
        self.read = read

    @property
    def admin(self):
        """Gets the admin of this RepositoryPermissions.  # noqa: E501


        :return: The admin of this RepositoryPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this RepositoryPermissions.


        :param admin: The admin of this RepositoryPermissions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and admin is None:  # noqa: E501
            raise ValueError("Invalid value for `admin`, must not be `None`")  # noqa: E501

        self._admin = admin

    @property
    def contribute(self):
        """Gets the contribute of this RepositoryPermissions.  # noqa: E501


        :return: The contribute of this RepositoryPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._contribute

    @contribute.setter
    def contribute(self, contribute):
        """Sets the contribute of this RepositoryPermissions.


        :param contribute: The contribute of this RepositoryPermissions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and contribute is None:  # noqa: E501
            raise ValueError("Invalid value for `contribute`, must not be `None`")  # noqa: E501

        self._contribute = contribute

    @property
    def read(self):
        """Gets the read of this RepositoryPermissions.  # noqa: E501


        :return: The read of this RepositoryPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this RepositoryPermissions.


        :param read: The read of this RepositoryPermissions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and read is None:  # noqa: E501
            raise ValueError("Invalid value for `read`, must not be `None`")  # noqa: E501

        self._read = read

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
        if not isinstance(other, RepositoryPermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryPermissions):
            return True

        return self.to_dict() != other.to_dict()
