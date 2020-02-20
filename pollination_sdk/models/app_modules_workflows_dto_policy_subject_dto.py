# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.2.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class AppModulesWorkflowsDtoPolicySubjectDto(object):
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
        'type': 'str',
        'id': 'str',
        'role': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'role': 'role'
    }

    def __init__(self, type=None, id=None, role=None, local_vars_configuration=None):  # noqa: E501
        """AppModulesWorkflowsDtoPolicySubjectDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._id = None
        self._role = None
        self.discriminator = None

        self.type = type
        self.id = id
        self.role = role

    @property
    def type(self):
        """Gets the type of this AppModulesWorkflowsDtoPolicySubjectDto.  # noqa: E501

        The type of policy subject. Can be `team`, `org` or `user`  # noqa: E501

        :return: The type of this AppModulesWorkflowsDtoPolicySubjectDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AppModulesWorkflowsDtoPolicySubjectDto.

        The type of policy subject. Can be `team`, `org` or `user`  # noqa: E501

        :param type: The type of this AppModulesWorkflowsDtoPolicySubjectDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this AppModulesWorkflowsDtoPolicySubjectDto.  # noqa: E501

        The ID of the policy subject  # noqa: E501

        :return: The id of this AppModulesWorkflowsDtoPolicySubjectDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppModulesWorkflowsDtoPolicySubjectDto.

        The ID of the policy subject  # noqa: E501

        :param id: The id of this AppModulesWorkflowsDtoPolicySubjectDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def role(self):
        """Gets the role of this AppModulesWorkflowsDtoPolicySubjectDto.  # noqa: E501

        The role within the policy subject that the access policy refers  # noqa: E501

        :return: The role of this AppModulesWorkflowsDtoPolicySubjectDto.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AppModulesWorkflowsDtoPolicySubjectDto.

        The role within the policy subject that the access policy refers  # noqa: E501

        :param role: The role of this AppModulesWorkflowsDtoPolicySubjectDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

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
        if not isinstance(other, AppModulesWorkflowsDtoPolicySubjectDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppModulesWorkflowsDtoPolicySubjectDto):
            return True

        return self.to_dict() != other.to_dict()
