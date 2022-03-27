# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.28.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class PluginPackage(object):
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
        'created_at': 'datetime',
        'description': 'str',
        'digest': 'str',
        'icon': 'str',
        'keywords': 'list[str]',
        'manifest': 'Plugin',
        'readme': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'digest': 'digest',
        'icon': 'icon',
        'keywords': 'keywords',
        'manifest': 'manifest',
        'readme': 'readme',
        'tag': 'tag'
    }

    def __init__(self, created_at=None, description=None, digest=None, icon=None, keywords=None, manifest=None, readme=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """PluginPackage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._description = None
        self._digest = None
        self._icon = None
        self._keywords = None
        self._manifest = None
        self._readme = None
        self._tag = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        self.digest = digest
        if icon is not None:
            self.icon = icon
        if keywords is not None:
            self.keywords = keywords
        self.manifest = manifest
        if readme is not None:
            self.readme = readme
        self.tag = tag

    @property
    def created_at(self):
        """Gets the created_at of this PluginPackage.  # noqa: E501

        Creation Timestamp  # noqa: E501

        :return: The created_at of this PluginPackage.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PluginPackage.

        Creation Timestamp  # noqa: E501

        :param created_at: The created_at of this PluginPackage.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this PluginPackage.  # noqa: E501

        description  # noqa: E501

        :return: The description of this PluginPackage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PluginPackage.

        description  # noqa: E501

        :param description: The description of this PluginPackage.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def digest(self):
        """Gets the digest of this PluginPackage.  # noqa: E501

        The new package digest  # noqa: E501

        :return: The digest of this PluginPackage.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this PluginPackage.

        The new package digest  # noqa: E501

        :param digest: The digest of this PluginPackage.  # noqa: E501
        :type digest: str
        """
        if self.local_vars_configuration.client_side_validation and digest is None:  # noqa: E501
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest

    @property
    def icon(self):
        """Gets the icon of this PluginPackage.  # noqa: E501

        icon  # noqa: E501

        :return: The icon of this PluginPackage.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this PluginPackage.

        icon  # noqa: E501

        :param icon: The icon of this PluginPackage.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def keywords(self):
        """Gets the keywords of this PluginPackage.  # noqa: E501

        keywords  # noqa: E501

        :return: The keywords of this PluginPackage.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this PluginPackage.

        keywords  # noqa: E501

        :param keywords: The keywords of this PluginPackage.  # noqa: E501
        :type keywords: list[str]
        """

        self._keywords = keywords

    @property
    def manifest(self):
        """Gets the manifest of this PluginPackage.  # noqa: E501


        :return: The manifest of this PluginPackage.  # noqa: E501
        :rtype: Plugin
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this PluginPackage.


        :param manifest: The manifest of this PluginPackage.  # noqa: E501
        :type manifest: Plugin
        """
        if self.local_vars_configuration.client_side_validation and manifest is None:  # noqa: E501
            raise ValueError("Invalid value for `manifest`, must not be `None`")  # noqa: E501

        self._manifest = manifest

    @property
    def readme(self):
        """Gets the readme of this PluginPackage.  # noqa: E501

        The Repository Readme  # noqa: E501

        :return: The readme of this PluginPackage.  # noqa: E501
        :rtype: str
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this PluginPackage.

        The Repository Readme  # noqa: E501

        :param readme: The readme of this PluginPackage.  # noqa: E501
        :type readme: str
        """

        self._readme = readme

    @property
    def tag(self):
        """Gets the tag of this PluginPackage.  # noqa: E501

        The new package tag  # noqa: E501

        :return: The tag of this PluginPackage.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PluginPackage.

        The new package tag  # noqa: E501

        :param tag: The tag of this PluginPackage.  # noqa: E501
        :type tag: str
        """
        if self.local_vars_configuration.client_side_validation and tag is None:  # noqa: E501
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

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
        if not isinstance(other, PluginPackage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginPackage):
            return True

        return self.to_dict() != other.to_dict()
