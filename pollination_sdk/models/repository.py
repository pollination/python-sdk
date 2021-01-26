# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.10.18
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Repository(object):
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
        'icon': 'str',
        'id': 'str',
        'keywords': 'list[str]',
        'latest_tag': 'str',
        'name': 'str',
        'owner': 'AccountPublic',
        'permissions': 'RepositoryUserPermissions',
        'public': 'bool',
        'slug': 'str'
    }

    attribute_map = {
        'description': 'description',
        'icon': 'icon',
        'id': 'id',
        'keywords': 'keywords',
        'latest_tag': 'latest_tag',
        'name': 'name',
        'owner': 'owner',
        'permissions': 'permissions',
        'public': 'public',
        'slug': 'slug'
    }

    def __init__(self, description=None, icon=None, id=None, keywords=None, latest_tag=None, name=None, owner=None, permissions=None, public=True, slug=None, local_vars_configuration=None):  # noqa: E501
        """Repository - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._icon = None
        self._id = None
        self._keywords = None
        self._latest_tag = None
        self._name = None
        self._owner = None
        self._permissions = None
        self._public = None
        self._slug = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if icon is not None:
            self.icon = icon
        self.id = id
        if keywords is not None:
            self.keywords = keywords
        self.latest_tag = latest_tag
        self.name = name
        self.owner = owner
        if permissions is not None:
            self.permissions = permissions
        if public is not None:
            self.public = public
        if slug is not None:
            self.slug = slug

    @property
    def description(self):
        """Gets the description of this Repository.  # noqa: E501

        A description of the repository  # noqa: E501

        :return: The description of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Repository.

        A description of the repository  # noqa: E501

        :param description: The description of this Repository.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this Repository.  # noqa: E501

        An icon to represent this repository  # noqa: E501

        :return: The icon of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Repository.

        An icon to represent this repository  # noqa: E501

        :param icon: The icon of this Repository.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this Repository.  # noqa: E501

        The recipe unique ID  # noqa: E501

        :return: The id of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Repository.

        The recipe unique ID  # noqa: E501

        :param id: The id of this Repository.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def keywords(self):
        """Gets the keywords of this Repository.  # noqa: E501

        A list of keywords to index the repository by  # noqa: E501

        :return: The keywords of this Repository.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Repository.

        A list of keywords to index the repository by  # noqa: E501

        :param keywords: The keywords of this Repository.  # noqa: E501
        :type keywords: list[str]
        """

        self._keywords = keywords

    @property
    def latest_tag(self):
        """Gets the latest_tag of this Repository.  # noqa: E501

        The latest package version to be indexed  # noqa: E501

        :return: The latest_tag of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._latest_tag

    @latest_tag.setter
    def latest_tag(self, latest_tag):
        """Sets the latest_tag of this Repository.

        The latest package version to be indexed  # noqa: E501

        :param latest_tag: The latest_tag of this Repository.  # noqa: E501
        :type latest_tag: str
        """
        if self.local_vars_configuration.client_side_validation and latest_tag is None:  # noqa: E501
            raise ValueError("Invalid value for `latest_tag`, must not be `None`")  # noqa: E501

        self._latest_tag = latest_tag

    @property
    def name(self):
        """Gets the name of this Repository.  # noqa: E501

        The name of the repository  # noqa: E501

        :return: The name of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Repository.

        The name of the repository  # noqa: E501

        :param name: The name of this Repository.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this Repository.  # noqa: E501

        The owner of the repository  # noqa: E501

        :return: The owner of this Repository.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Repository.

        The owner of the repository  # noqa: E501

        :param owner: The owner of this Repository.  # noqa: E501
        :type owner: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def permissions(self):
        """Gets the permissions of this Repository.  # noqa: E501

        The permissions the user making the API call has on the resource  # noqa: E501

        :return: The permissions of this Repository.  # noqa: E501
        :rtype: RepositoryUserPermissions
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Repository.

        The permissions the user making the API call has on the resource  # noqa: E501

        :param permissions: The permissions of this Repository.  # noqa: E501
        :type permissions: RepositoryUserPermissions
        """

        self._permissions = permissions

    @property
    def public(self):
        """Gets the public of this Repository.  # noqa: E501

        Whether or not a repository is publicly viewable  # noqa: E501

        :return: The public of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this Repository.

        Whether or not a repository is publicly viewable  # noqa: E501

        :param public: The public of this Repository.  # noqa: E501
        :type public: bool
        """

        self._public = public

    @property
    def slug(self):
        """Gets the slug of this Repository.  # noqa: E501

        The repository slug  # noqa: E501

        :return: The slug of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Repository.

        The repository slug  # noqa: E501

        :param slug: The slug of this Repository.  # noqa: E501
        :type slug: str
        """

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
        if not isinstance(other, Repository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Repository):
            return True

        return self.to_dict() != other.to_dict()
