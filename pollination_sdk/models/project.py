# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.41.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Project(object):
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
        'name': 'str',
        'owner': 'AccountPublic',
        'permissions': 'UserPermission',
        'public': 'bool',
        'slug': 'str',
        'usage': 'Usage'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'owner': 'owner',
        'permissions': 'permissions',
        'public': 'public',
        'slug': 'slug',
        'usage': 'usage'
    }

    def __init__(self, description='', id=None, name=None, owner=None, permissions=None, public=True, slug=None, usage=None, local_vars_configuration=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._id = None
        self._name = None
        self._owner = None
        self._permissions = None
        self._public = None
        self._slug = None
        self._usage = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.id = id
        self.name = name
        self.owner = owner
        self.permissions = permissions
        if public is not None:
            self.public = public
        self.slug = slug
        if usage is not None:
            self.usage = usage

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501

        A description of the project  # noqa: E501

        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        A description of the project  # noqa: E501

        :param description: The description of this Project.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501

        The project ID  # noqa: E501

        :return: The id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        The project ID  # noqa: E501

        :param id: The id of this Project.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        The name of the project. Must be unique to a given owner  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        The name of the project. Must be unique to a given owner  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this Project.  # noqa: E501

        The project owner  # noqa: E501

        :return: The owner of this Project.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Project.

        The project owner  # noqa: E501

        :param owner: The owner of this Project.  # noqa: E501
        :type owner: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def permissions(self):
        """Gets the permissions of this Project.  # noqa: E501


        :return: The permissions of this Project.  # noqa: E501
        :rtype: UserPermission
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Project.


        :param permissions: The permissions of this Project.  # noqa: E501
        :type permissions: UserPermission
        """
        if self.local_vars_configuration.client_side_validation and permissions is None:  # noqa: E501
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def public(self):
        """Gets the public of this Project.  # noqa: E501

        Whether or not a project is publicly viewable  # noqa: E501

        :return: The public of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this Project.

        Whether or not a project is publicly viewable  # noqa: E501

        :param public: The public of this Project.  # noqa: E501
        :type public: bool
        """

        self._public = public

    @property
    def slug(self):
        """Gets the slug of this Project.  # noqa: E501

        The project name in slug format  # noqa: E501

        :return: The slug of this Project.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Project.

        The project name in slug format  # noqa: E501

        :param slug: The slug of this Project.  # noqa: E501
        :type slug: str
        """
        if self.local_vars_configuration.client_side_validation and slug is None:  # noqa: E501
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

    @property
    def usage(self):
        """Gets the usage of this Project.  # noqa: E501

        The resource consumption of this project  # noqa: E501

        :return: The usage of this Project.  # noqa: E501
        :rtype: Usage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this Project.

        The resource consumption of this project  # noqa: E501

        :param usage: The usage of this Project.  # noqa: E501
        :type usage: Usage
        """

        self._usage = usage

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
