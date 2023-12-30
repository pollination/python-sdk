# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.46.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class RepositoryPolicySubject(object):
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
        'name': 'str',
        'subject_type': 'SubjectType'
    }

    attribute_map = {
        'name': 'name',
        'subject_type': 'subject_type'
    }

    def __init__(self, name=None, subject_type=None, local_vars_configuration=None):  # noqa: E501
        """RepositoryPolicySubject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._subject_type = None
        self.discriminator = None

        self.name = name
        self.subject_type = subject_type

    @property
    def name(self):
        """Gets the name of this RepositoryPolicySubject.  # noqa: E501

        The name of the policy subject  # noqa: E501

        :return: The name of this RepositoryPolicySubject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryPolicySubject.

        The name of the policy subject  # noqa: E501

        :param name: The name of this RepositoryPolicySubject.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subject_type(self):
        """Gets the subject_type of this RepositoryPolicySubject.  # noqa: E501


        :return: The subject_type of this RepositoryPolicySubject.  # noqa: E501
        :rtype: SubjectType
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        """Sets the subject_type of this RepositoryPolicySubject.


        :param subject_type: The subject_type of this RepositoryPolicySubject.  # noqa: E501
        :type subject_type: SubjectType
        """
        if self.local_vars_configuration.client_side_validation and subject_type is None:  # noqa: E501
            raise ValueError("Invalid value for `subject_type`, must not be `None`")  # noqa: E501

        self._subject_type = subject_type

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
        if not isinstance(other, RepositoryPolicySubject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryPolicySubject):
            return True

        return self.to_dict() != other.to_dict()
