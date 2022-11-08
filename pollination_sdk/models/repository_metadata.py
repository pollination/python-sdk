# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.32.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class RepositoryMetadata(object):
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
        'description': 'str',
        'name': 'str',
        'plugin_count': 'int',
        'recipe_count': 'int',
        'source': 'str',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'description': 'description',
        'name': 'name',
        'plugin_count': 'plugin_count',
        'recipe_count': 'recipe_count',
        'source': 'source',
        'type': 'type'
    }

    def __init__(self, annotations=None, description='A Queenbee package repository', name=None, plugin_count=0, recipe_count=0, source=None, type='RepositoryMetadata', local_vars_configuration=None):  # noqa: E501
        """RepositoryMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._description = None
        self._name = None
        self._plugin_count = None
        self._recipe_count = None
        self._source = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if plugin_count is not None:
            self.plugin_count = plugin_count
        if recipe_count is not None:
            self.recipe_count = recipe_count
        if source is not None:
            self.source = source
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this RepositoryMetadata.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this RepositoryMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this RepositoryMetadata.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this RepositoryMetadata.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def description(self):
        """Gets the description of this RepositoryMetadata.  # noqa: E501

        A short description of the repository  # noqa: E501

        :return: The description of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RepositoryMetadata.

        A short description of the repository  # noqa: E501

        :param description: The description of this RepositoryMetadata.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this RepositoryMetadata.  # noqa: E501

        The name of the repository  # noqa: E501

        :return: The name of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryMetadata.

        The name of the repository  # noqa: E501

        :param name: The name of this RepositoryMetadata.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def plugin_count(self):
        """Gets the plugin_count of this RepositoryMetadata.  # noqa: E501

        The number of plugins hosted by the repository  # noqa: E501

        :return: The plugin_count of this RepositoryMetadata.  # noqa: E501
        :rtype: int
        """
        return self._plugin_count

    @plugin_count.setter
    def plugin_count(self, plugin_count):
        """Sets the plugin_count of this RepositoryMetadata.

        The number of plugins hosted by the repository  # noqa: E501

        :param plugin_count: The plugin_count of this RepositoryMetadata.  # noqa: E501
        :type plugin_count: int
        """

        self._plugin_count = plugin_count

    @property
    def recipe_count(self):
        """Gets the recipe_count of this RepositoryMetadata.  # noqa: E501

        The number of recipes hosted by the repository  # noqa: E501

        :return: The recipe_count of this RepositoryMetadata.  # noqa: E501
        :rtype: int
        """
        return self._recipe_count

    @recipe_count.setter
    def recipe_count(self, recipe_count):
        """Sets the recipe_count of this RepositoryMetadata.

        The number of recipes hosted by the repository  # noqa: E501

        :param recipe_count: The recipe_count of this RepositoryMetadata.  # noqa: E501
        :type recipe_count: int
        """

        self._recipe_count = recipe_count

    @property
    def source(self):
        """Gets the source of this RepositoryMetadata.  # noqa: E501

        The source path (url or local) to the repository  # noqa: E501

        :return: The source of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RepositoryMetadata.

        The source path (url or local) to the repository  # noqa: E501

        :param source: The source of this RepositoryMetadata.  # noqa: E501
        :type source: str
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this RepositoryMetadata.  # noqa: E501


        :return: The type of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RepositoryMetadata.


        :param type: The type of this RepositoryMetadata.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^RepositoryMetadata$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^RepositoryMetadata$/`")  # noqa: E501

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
        if not isinstance(other, RepositoryMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryMetadata):
            return True

        return self.to_dict() != other.to_dict()
