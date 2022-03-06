# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.27.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class PackageVersion(object):
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
        'created': 'datetime',
        'deprecated': 'bool',
        'description': 'str',
        'digest': 'str',
        'home': 'str',
        'icon': 'str',
        'keywords': 'list[str]',
        'kind': 'str',
        'license': 'License',
        'maintainers': 'list[Maintainer]',
        'manifest': 'AnyOfRecipePlugin',
        'name': 'str',
        'readme': 'str',
        'slug': 'str',
        'sources': 'list[str]',
        'tag': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'app_version': 'app_version',
        'created': 'created',
        'deprecated': 'deprecated',
        'description': 'description',
        'digest': 'digest',
        'home': 'home',
        'icon': 'icon',
        'keywords': 'keywords',
        'kind': 'kind',
        'license': 'license',
        'maintainers': 'maintainers',
        'manifest': 'manifest',
        'name': 'name',
        'readme': 'readme',
        'slug': 'slug',
        'sources': 'sources',
        'tag': 'tag',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, annotations=None, app_version=None, created=None, deprecated=None, description=None, digest=None, home=None, icon=None, keywords=None, kind='', license=None, maintainers=None, manifest=None, name=None, readme=None, slug=None, sources=None, tag=None, type='PackageVersion', url=None, local_vars_configuration=None):  # noqa: E501
        """PackageVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._app_version = None
        self._created = None
        self._deprecated = None
        self._description = None
        self._digest = None
        self._home = None
        self._icon = None
        self._keywords = None
        self._kind = None
        self._license = None
        self._maintainers = None
        self._manifest = None
        self._name = None
        self._readme = None
        self._slug = None
        self._sources = None
        self._tag = None
        self._type = None
        self._url = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if app_version is not None:
            self.app_version = app_version
        self.created = created
        if deprecated is not None:
            self.deprecated = deprecated
        if description is not None:
            self.description = description
        self.digest = digest
        if home is not None:
            self.home = home
        if icon is not None:
            self.icon = icon
        if keywords is not None:
            self.keywords = keywords
        if kind is not None:
            self.kind = kind
        if license is not None:
            self.license = license
        if maintainers is not None:
            self.maintainers = maintainers
        if manifest is not None:
            self.manifest = manifest
        self.name = name
        if readme is not None:
            self.readme = readme
        if slug is not None:
            self.slug = slug
        if sources is not None:
            self.sources = sources
        self.tag = tag
        if type is not None:
            self.type = type
        self.url = url

    @property
    def annotations(self):
        """Gets the annotations of this PackageVersion.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this PackageVersion.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this PackageVersion.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this PackageVersion.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def app_version(self):
        """Gets the app_version of this PackageVersion.  # noqa: E501

        The version of the application code underlying the manifest  # noqa: E501

        :return: The app_version of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this PackageVersion.

        The version of the application code underlying the manifest  # noqa: E501

        :param app_version: The app_version of this PackageVersion.  # noqa: E501
        :type app_version: str
        """

        self._app_version = app_version

    @property
    def created(self):
        """Gets the created of this PackageVersion.  # noqa: E501


        :return: The created of this PackageVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PackageVersion.


        :param created: The created of this PackageVersion.  # noqa: E501
        :type created: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def deprecated(self):
        """Gets the deprecated of this PackageVersion.  # noqa: E501

        Whether this package is deprecated  # noqa: E501

        :return: The deprecated of this PackageVersion.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this PackageVersion.

        Whether this package is deprecated  # noqa: E501

        :param deprecated: The deprecated of this PackageVersion.  # noqa: E501
        :type deprecated: bool
        """

        self._deprecated = deprecated

    @property
    def description(self):
        """Gets the description of this PackageVersion.  # noqa: E501

        A description of what this package does  # noqa: E501

        :return: The description of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PackageVersion.

        A description of what this package does  # noqa: E501

        :param description: The description of this PackageVersion.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def digest(self):
        """Gets the digest of this PackageVersion.  # noqa: E501


        :return: The digest of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this PackageVersion.


        :param digest: The digest of this PackageVersion.  # noqa: E501
        :type digest: str
        """
        if self.local_vars_configuration.client_side_validation and digest is None:  # noqa: E501
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest

    @property
    def home(self):
        """Gets the home of this PackageVersion.  # noqa: E501

        The URL of this package's home page  # noqa: E501

        :return: The home of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this PackageVersion.

        The URL of this package's home page  # noqa: E501

        :param home: The home of this PackageVersion.  # noqa: E501
        :type home: str
        """

        self._home = home

    @property
    def icon(self):
        """Gets the icon of this PackageVersion.  # noqa: E501

        A URL to an SVG or PNG image to be used as an icon  # noqa: E501

        :return: The icon of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this PackageVersion.

        A URL to an SVG or PNG image to be used as an icon  # noqa: E501

        :param icon: The icon of this PackageVersion.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def keywords(self):
        """Gets the keywords of this PackageVersion.  # noqa: E501

        A list of keywords to search the package by  # noqa: E501

        :return: The keywords of this PackageVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this PackageVersion.

        A list of keywords to search the package by  # noqa: E501

        :param keywords: The keywords of this PackageVersion.  # noqa: E501
        :type keywords: list[str]
        """

        self._keywords = keywords

    @property
    def kind(self):
        """Gets the kind of this PackageVersion.  # noqa: E501

        The type of Queenbee package (ie: recipe or plugin)  # noqa: E501

        :return: The kind of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PackageVersion.

        The type of Queenbee package (ie: recipe or plugin)  # noqa: E501

        :param kind: The kind of this PackageVersion.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def license(self):
        """Gets the license of this PackageVersion.  # noqa: E501

        The license information.  # noqa: E501

        :return: The license of this PackageVersion.  # noqa: E501
        :rtype: License
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this PackageVersion.

        The license information.  # noqa: E501

        :param license: The license of this PackageVersion.  # noqa: E501
        :type license: License
        """

        self._license = license

    @property
    def maintainers(self):
        """Gets the maintainers of this PackageVersion.  # noqa: E501

        A list of maintainers for the package  # noqa: E501

        :return: The maintainers of this PackageVersion.  # noqa: E501
        :rtype: list[Maintainer]
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        """Sets the maintainers of this PackageVersion.

        A list of maintainers for the package  # noqa: E501

        :param maintainers: The maintainers of this PackageVersion.  # noqa: E501
        :type maintainers: list[Maintainer]
        """

        self._maintainers = maintainers

    @property
    def manifest(self):
        """Gets the manifest of this PackageVersion.  # noqa: E501

        The package Recipe or Plugin manifest  # noqa: E501

        :return: The manifest of this PackageVersion.  # noqa: E501
        :rtype: AnyOfRecipePlugin
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this PackageVersion.

        The package Recipe or Plugin manifest  # noqa: E501

        :param manifest: The manifest of this PackageVersion.  # noqa: E501
        :type manifest: AnyOfRecipePlugin
        """

        self._manifest = manifest

    @property
    def name(self):
        """Gets the name of this PackageVersion.  # noqa: E501

        Package name. Make it descriptive and helpful ;)  # noqa: E501

        :return: The name of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageVersion.

        Package name. Make it descriptive and helpful ;)  # noqa: E501

        :param name: The name of this PackageVersion.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def readme(self):
        """Gets the readme of this PackageVersion.  # noqa: E501

        The README file string for this package  # noqa: E501

        :return: The readme of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this PackageVersion.

        The README file string for this package  # noqa: E501

        :param readme: The readme of this PackageVersion.  # noqa: E501
        :type readme: str
        """

        self._readme = readme

    @property
    def slug(self):
        """Gets the slug of this PackageVersion.  # noqa: E501

        A slug of the repository name and the package name.  # noqa: E501

        :return: The slug of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this PackageVersion.

        A slug of the repository name and the package name.  # noqa: E501

        :param slug: The slug of this PackageVersion.  # noqa: E501
        :type slug: str
        """

        self._slug = slug

    @property
    def sources(self):
        """Gets the sources of this PackageVersion.  # noqa: E501

        A list of URLs to source code for this project  # noqa: E501

        :return: The sources of this PackageVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this PackageVersion.

        A list of URLs to source code for this project  # noqa: E501

        :param sources: The sources of this PackageVersion.  # noqa: E501
        :type sources: list[str]
        """

        self._sources = sources

    @property
    def tag(self):
        """Gets the tag of this PackageVersion.  # noqa: E501

        The tag of the package  # noqa: E501

        :return: The tag of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PackageVersion.

        The tag of the package  # noqa: E501

        :param tag: The tag of this PackageVersion.  # noqa: E501
        :type tag: str
        """
        if self.local_vars_configuration.client_side_validation and tag is None:  # noqa: E501
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def type(self):
        """Gets the type of this PackageVersion.  # noqa: E501


        :return: The type of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PackageVersion.


        :param type: The type of this PackageVersion.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^PackageVersion$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^PackageVersion$/`")  # noqa: E501

        self._type = type

    @property
    def url(self):
        """Gets the url of this PackageVersion.  # noqa: E501


        :return: The url of this PackageVersion.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PackageVersion.


        :param url: The url of this PackageVersion.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, PackageVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PackageVersion):
            return True

        return self.to_dict() != other.to_dict()
