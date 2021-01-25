# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.17
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Team(object):
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
        'id': 'str',
        'member_count': 'int',
        'name': 'str',
        'slug': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'member_count': 'member_count',
        'name': 'name',
        'slug': 'slug'
    }

    def __init__(self, description=None, id=None, member_count=0, name=None, slug=None, local_vars_configuration=None):  # noqa: E501
        """Team - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._id = None
        self._member_count = None
        self._name = None
        self._slug = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.id = id
        if member_count is not None:
            self.member_count = member_count
        self.name = name
        self.slug = slug

    @property
    def description(self):
        """Gets the description of this Team.  # noqa: E501


        :return: The description of this Team.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Team.


        :param description: The description of this Team.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Team.  # noqa: E501

        The team ID  # noqa: E501

        :return: The id of this Team.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Team.

        The team ID  # noqa: E501

        :param id: The id of this Team.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def member_count(self):
        """Gets the member_count of this Team.  # noqa: E501

        The number of members that are part of this team  # noqa: E501

        :return: The member_count of this Team.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this Team.

        The number of members that are part of this team  # noqa: E501

        :param member_count: The member_count of this Team.  # noqa: E501
        :type member_count: int
        """

        self._member_count = member_count

    @property
    def name(self):
        """Gets the name of this Team.  # noqa: E501


        :return: The name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Team.


        :param name: The name of this Team.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Team.  # noqa: E501

        The slug of the team  # noqa: E501

        :return: The slug of this Team.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Team.

        The slug of the team  # noqa: E501

        :param slug: The slug of this Team.  # noqa: E501
        :type slug: str
        """
        if self.local_vars_configuration.client_side_validation and slug is None:  # noqa: E501
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

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
        if not isinstance(other, Team):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Team):
            return True

        return self.to_dict() != other.to_dict()
