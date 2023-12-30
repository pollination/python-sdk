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


class MetaData(object):
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
        'annotations': 'dict(str, str)',
        'app_version': 'str',
        'deprecated': 'bool',
        'description': 'str',
        'home': 'str',
        'icon': 'str',
        'keywords': 'list[str]',
        'license': 'License',
        'maintainers': 'list[Maintainer]',
        'name': 'str',
        'sources': 'list[str]',
        'tag': 'str',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'app_version': 'app_version',
        'deprecated': 'deprecated',
        'description': 'description',
        'home': 'home',
        'icon': 'icon',
        'keywords': 'keywords',
        'license': 'license',
        'maintainers': 'maintainers',
        'name': 'name',
        'sources': 'sources',
        'tag': 'tag',
        'type': 'type'
    }

    def __init__(self, annotations=None, app_version=None, deprecated=None, description=None, home=None, icon=None, keywords=None, license=None, maintainers=None, name=None, sources=None, tag=None, type='MetaData', local_vars_configuration=None):  # noqa: E501
        """MetaData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._app_version = None
        self._deprecated = None
        self._description = None
        self._home = None
        self._icon = None
        self._keywords = None
        self._license = None
        self._maintainers = None
        self._name = None
        self._sources = None
        self._tag = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if app_version is not None:
            self.app_version = app_version
        if deprecated is not None:
            self.deprecated = deprecated
        if description is not None:
            self.description = description
        if home is not None:
            self.home = home
        if icon is not None:
            self.icon = icon
        if keywords is not None:
            self.keywords = keywords
        if license is not None:
            self.license = license
        if maintainers is not None:
            self.maintainers = maintainers
        self.name = name
        if sources is not None:
            self.sources = sources
        self.tag = tag
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this MetaData.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this MetaData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this MetaData.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this MetaData.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def app_version(self):
        """Gets the app_version of this MetaData.  # noqa: E501

        The version of the application code underlying the manifest  # noqa: E501

        :return: The app_version of this MetaData.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this MetaData.

        The version of the application code underlying the manifest  # noqa: E501

        :param app_version: The app_version of this MetaData.  # noqa: E501
        :type app_version: str
        """

        self._app_version = app_version

    @property
    def deprecated(self):
        """Gets the deprecated of this MetaData.  # noqa: E501

        Whether this package is deprecated  # noqa: E501

        :return: The deprecated of this MetaData.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this MetaData.

        Whether this package is deprecated  # noqa: E501

        :param deprecated: The deprecated of this MetaData.  # noqa: E501
        :type deprecated: bool
        """

        self._deprecated = deprecated

    @property
    def description(self):
        """Gets the description of this MetaData.  # noqa: E501

        A description of what this package does  # noqa: E501

        :return: The description of this MetaData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MetaData.

        A description of what this package does  # noqa: E501

        :param description: The description of this MetaData.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def home(self):
        """Gets the home of this MetaData.  # noqa: E501

        The URL of this package's home page  # noqa: E501

        :return: The home of this MetaData.  # noqa: E501
        :rtype: str
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this MetaData.

        The URL of this package's home page  # noqa: E501

        :param home: The home of this MetaData.  # noqa: E501
        :type home: str
        """

        self._home = home

    @property
    def icon(self):
        """Gets the icon of this MetaData.  # noqa: E501

        A URL to an SVG or PNG image to be used as an icon  # noqa: E501

        :return: The icon of this MetaData.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this MetaData.

        A URL to an SVG or PNG image to be used as an icon  # noqa: E501

        :param icon: The icon of this MetaData.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def keywords(self):
        """Gets the keywords of this MetaData.  # noqa: E501

        A list of keywords to search the package by  # noqa: E501

        :return: The keywords of this MetaData.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this MetaData.

        A list of keywords to search the package by  # noqa: E501

        :param keywords: The keywords of this MetaData.  # noqa: E501
        :type keywords: list[str]
        """

        self._keywords = keywords

    @property
    def license(self):
        """Gets the license of this MetaData.  # noqa: E501

        The license information.  # noqa: E501

        :return: The license of this MetaData.  # noqa: E501
        :rtype: License
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this MetaData.

        The license information.  # noqa: E501

        :param license: The license of this MetaData.  # noqa: E501
        :type license: License
        """

        self._license = license

    @property
    def maintainers(self):
        """Gets the maintainers of this MetaData.  # noqa: E501

        A list of maintainers for the package  # noqa: E501

        :return: The maintainers of this MetaData.  # noqa: E501
        :rtype: list[Maintainer]
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        """Sets the maintainers of this MetaData.

        A list of maintainers for the package  # noqa: E501

        :param maintainers: The maintainers of this MetaData.  # noqa: E501
        :type maintainers: list[Maintainer]
        """

        self._maintainers = maintainers

    @property
    def name(self):
        """Gets the name of this MetaData.  # noqa: E501

        Package name. Make it descriptive and helpful ;)  # noqa: E501

        :return: The name of this MetaData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetaData.

        Package name. Make it descriptive and helpful ;)  # noqa: E501

        :param name: The name of this MetaData.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sources(self):
        """Gets the sources of this MetaData.  # noqa: E501

        A list of URLs to source code for this project  # noqa: E501

        :return: The sources of this MetaData.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this MetaData.

        A list of URLs to source code for this project  # noqa: E501

        :param sources: The sources of this MetaData.  # noqa: E501
        :type sources: list[str]
        """

        self._sources = sources

    @property
    def tag(self):
        """Gets the tag of this MetaData.  # noqa: E501

        The tag of the package  # noqa: E501

        :return: The tag of this MetaData.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this MetaData.

        The tag of the package  # noqa: E501

        :param tag: The tag of this MetaData.  # noqa: E501
        :type tag: str
        """
        if self.local_vars_configuration.client_side_validation and tag is None:  # noqa: E501
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def type(self):
        """Gets the type of this MetaData.  # noqa: E501


        :return: The type of this MetaData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MetaData.


        :param type: The type of this MetaData.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^MetaData$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^MetaData$/`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, MetaData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetaData):
            return True

        return self.to_dict() != other.to_dict()
