# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.31.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class TeamMember(object):
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
        'role': 'TeamRoleEnum',
        'user': 'UserPublic'
    }

    attribute_map = {
        'role': 'role',
        'user': 'user'
    }

    def __init__(self, role=None, user=None, local_vars_configuration=None):  # noqa: E501
        """TeamMember - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._role = None
        self._user = None
        self.discriminator = None

        self.role = role
        self.user = user

    @property
    def role(self):
        """Gets the role of this TeamMember.  # noqa: E501

        The role the user has within the team  # noqa: E501

        :return: The role of this TeamMember.  # noqa: E501
        :rtype: TeamRoleEnum
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this TeamMember.

        The role the user has within the team  # noqa: E501

        :param role: The role of this TeamMember.  # noqa: E501
        :type role: TeamRoleEnum
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def user(self):
        """Gets the user of this TeamMember.  # noqa: E501

        The team member  # noqa: E501

        :return: The user of this TeamMember.  # noqa: E501
        :rtype: UserPublic
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TeamMember.

        The team member  # noqa: E501

        :param user: The user of this TeamMember.  # noqa: E501
        :type user: UserPublic
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, TeamMember):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamMember):
            return True

        return self.to_dict() != other.to_dict()
