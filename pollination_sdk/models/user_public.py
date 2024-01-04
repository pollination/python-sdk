# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class UserPublic(object):
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
        'name': 'str',
        'picture': 'str',
        'username': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'picture': 'picture',
        'username': 'username'
    }

    def __init__(self, description=None, name=None, picture=None, username=None, local_vars_configuration=None):  # noqa: E501
        """UserPublic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._name = None
        self._picture = None
        self._username = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if picture is not None:
            self.picture = picture
        self.username = username

    @property
    def description(self):
        """Gets the description of this UserPublic.  # noqa: E501

        A short description of the user  # noqa: E501

        :return: The description of this UserPublic.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserPublic.

        A short description of the user  # noqa: E501

        :param description: The description of this UserPublic.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this UserPublic.  # noqa: E501

        The display name for this user  # noqa: E501

        :return: The name of this UserPublic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserPublic.

        The display name for this user  # noqa: E501

        :param name: The name of this UserPublic.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def picture(self):
        """Gets the picture of this UserPublic.  # noqa: E501

        URL to the picture associated with this user  # noqa: E501

        :return: The picture of this UserPublic.  # noqa: E501
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this UserPublic.

        URL to the picture associated with this user  # noqa: E501

        :param picture: The picture of this UserPublic.  # noqa: E501
        :type picture: str
        """

        self._picture = picture

    @property
    def username(self):
        """Gets the username of this UserPublic.  # noqa: E501

        The lowercase account name for this user  # noqa: E501

        :return: The username of this UserPublic.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserPublic.

        The lowercase account name for this user  # noqa: E501

        :param username: The username of this UserPublic.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, UserPublic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserPublic):
            return True

        return self.to_dict() != other.to_dict()
