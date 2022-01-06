# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.22.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class RepositoryAccessPolicy(object):
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
        'permission': 'Permission',
        'subject': 'PolicySubject'
    }

    attribute_map = {
        'permission': 'permission',
        'subject': 'subject'
    }

    def __init__(self, permission=None, subject=None, local_vars_configuration=None):  # noqa: E501
        """RepositoryAccessPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._permission = None
        self._subject = None
        self.discriminator = None

        self.permission = permission
        self.subject = subject

    @property
    def permission(self):
        """Gets the permission of this RepositoryAccessPolicy.  # noqa: E501

        The permission given to the subject of the access policy  # noqa: E501

        :return: The permission of this RepositoryAccessPolicy.  # noqa: E501
        :rtype: Permission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this RepositoryAccessPolicy.

        The permission given to the subject of the access policy  # noqa: E501

        :param permission: The permission of this RepositoryAccessPolicy.  # noqa: E501
        :type permission: Permission
        """
        if self.local_vars_configuration.client_side_validation and permission is None:  # noqa: E501
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501

        self._permission = permission

    @property
    def subject(self):
        """Gets the subject of this RepositoryAccessPolicy.  # noqa: E501

        The subject of the access policy  # noqa: E501

        :return: The subject of this RepositoryAccessPolicy.  # noqa: E501
        :rtype: PolicySubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this RepositoryAccessPolicy.

        The subject of the access policy  # noqa: E501

        :param subject: The subject of this RepositoryAccessPolicy.  # noqa: E501
        :type subject: PolicySubject
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

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
        if not isinstance(other, RepositoryAccessPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryAccessPolicy):
            return True

        return self.to_dict() != other.to_dict()
