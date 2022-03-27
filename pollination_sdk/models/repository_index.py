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


class RepositoryIndex(object):
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
        'api_version': 'str',
        'generated': 'datetime',
        'metadata': 'RepositoryMetadata',
        'plugin': 'dict(str, list[PackageVersion])',
        'recipe': 'dict(str, list[PackageVersion])',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'api_version': 'api_version',
        'generated': 'generated',
        'metadata': 'metadata',
        'plugin': 'plugin',
        'recipe': 'recipe',
        'type': 'type'
    }

    def __init__(self, annotations=None, api_version='v1beta1', generated=None, metadata=None, plugin=None, recipe=None, type='RepositoryIndex', local_vars_configuration=None):  # noqa: E501
        """RepositoryIndex - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._api_version = None
        self._generated = None
        self._metadata = None
        self._plugin = None
        self._recipe = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if api_version is not None:
            self.api_version = api_version
        if generated is not None:
            self.generated = generated
        if metadata is not None:
            self.metadata = metadata
        if plugin is not None:
            self.plugin = plugin
        if recipe is not None:
            self.recipe = recipe
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this RepositoryIndex.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this RepositoryIndex.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this RepositoryIndex.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this RepositoryIndex.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def api_version(self):
        """Gets the api_version of this RepositoryIndex.  # noqa: E501


        :return: The api_version of this RepositoryIndex.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this RepositoryIndex.


        :param api_version: The api_version of this RepositoryIndex.  # noqa: E501
        :type api_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_version is not None and not re.search(r'^v1beta1$', api_version)):  # noqa: E501
            raise ValueError(r"Invalid value for `api_version`, must be a follow pattern or equal to `/^v1beta1$/`")  # noqa: E501

        self._api_version = api_version

    @property
    def generated(self):
        """Gets the generated of this RepositoryIndex.  # noqa: E501

        The timestamp at which the index was generated  # noqa: E501

        :return: The generated of this RepositoryIndex.  # noqa: E501
        :rtype: datetime
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this RepositoryIndex.

        The timestamp at which the index was generated  # noqa: E501

        :param generated: The generated of this RepositoryIndex.  # noqa: E501
        :type generated: datetime
        """

        self._generated = generated

    @property
    def metadata(self):
        """Gets the metadata of this RepositoryIndex.  # noqa: E501

        Extra information about the repository  # noqa: E501

        :return: The metadata of this RepositoryIndex.  # noqa: E501
        :rtype: RepositoryMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RepositoryIndex.

        Extra information about the repository  # noqa: E501

        :param metadata: The metadata of this RepositoryIndex.  # noqa: E501
        :type metadata: RepositoryMetadata
        """

        self._metadata = metadata

    @property
    def plugin(self):
        """Gets the plugin of this RepositoryIndex.  # noqa: E501

        A dict of plugins accessible by name. Each name key points to a list of plugin versions  # noqa: E501

        :return: The plugin of this RepositoryIndex.  # noqa: E501
        :rtype: dict(str, list[PackageVersion])
        """
        return self._plugin

    @plugin.setter
    def plugin(self, plugin):
        """Sets the plugin of this RepositoryIndex.

        A dict of plugins accessible by name. Each name key points to a list of plugin versions  # noqa: E501

        :param plugin: The plugin of this RepositoryIndex.  # noqa: E501
        :type plugin: dict(str, list[PackageVersion])
        """

        self._plugin = plugin

    @property
    def recipe(self):
        """Gets the recipe of this RepositoryIndex.  # noqa: E501

        A dict of recipes accessible by name. Each name key points to a list of recipesversions  # noqa: E501

        :return: The recipe of this RepositoryIndex.  # noqa: E501
        :rtype: dict(str, list[PackageVersion])
        """
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        """Sets the recipe of this RepositoryIndex.

        A dict of recipes accessible by name. Each name key points to a list of recipesversions  # noqa: E501

        :param recipe: The recipe of this RepositoryIndex.  # noqa: E501
        :type recipe: dict(str, list[PackageVersion])
        """

        self._recipe = recipe

    @property
    def type(self):
        """Gets the type of this RepositoryIndex.  # noqa: E501


        :return: The type of this RepositoryIndex.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RepositoryIndex.


        :param type: The type of this RepositoryIndex.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^RepositoryIndex$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^RepositoryIndex$/`")  # noqa: E501

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
        if not isinstance(other, RepositoryIndex):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryIndex):
            return True

        return self.to_dict() != other.to_dict()
