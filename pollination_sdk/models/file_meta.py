# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.12.3
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class FileMeta(object):
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
        'file_name': 'str',
        'file_type': 'str',
        'key': 'str',
        'last_modified': 'datetime',
        'size': 'int'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_type': 'file_type',
        'key': 'key',
        'last_modified': 'last_modified',
        'size': 'size'
    }

    def __init__(self, file_name=None, file_type=None, key=None, last_modified=None, size=None, local_vars_configuration=None):  # noqa: E501
        """FileMeta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_name = None
        self._file_type = None
        self._key = None
        self._last_modified = None
        self._size = None
        self.discriminator = None

        self.file_name = file_name
        self.file_type = file_type
        self.key = key
        if last_modified is not None:
            self.last_modified = last_modified
        if size is not None:
            self.size = size

    @property
    def file_name(self):
        """Gets the file_name of this FileMeta.  # noqa: E501


        :return: The file_name of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileMeta.


        :param file_name: The file_name of this FileMeta.  # noqa: E501
        :type file_name: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def file_type(self):
        """Gets the file_type of this FileMeta.  # noqa: E501


        :return: The file_type of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this FileMeta.


        :param file_type: The file_type of this FileMeta.  # noqa: E501
        :type file_type: str
        """
        if self.local_vars_configuration.client_side_validation and file_type is None:  # noqa: E501
            raise ValueError("Invalid value for `file_type`, must not be `None`")  # noqa: E501

        self._file_type = file_type

    @property
    def key(self):
        """Gets the key of this FileMeta.  # noqa: E501


        :return: The key of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FileMeta.


        :param key: The key of this FileMeta.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def last_modified(self):
        """Gets the last_modified of this FileMeta.  # noqa: E501


        :return: The last_modified of this FileMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this FileMeta.


        :param last_modified: The last_modified of this FileMeta.  # noqa: E501
        :type last_modified: datetime
        """

        self._last_modified = last_modified

    @property
    def size(self):
        """Gets the size of this FileMeta.  # noqa: E501


        :return: The size of this FileMeta.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileMeta.


        :param size: The size of this FileMeta.  # noqa: E501
        :type size: int
        """

        self._size = size

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
        if not isinstance(other, FileMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileMeta):
            return True

        return self.to_dict() != other.to_dict()
