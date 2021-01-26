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


class Plugin(object):
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
        'config': 'PluginConfig',
        'functions': 'list[Function]',
        'metadata': 'MetaData',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'api_version': 'api_version',
        'config': 'config',
        'functions': 'functions',
        'metadata': 'metadata',
        'type': 'type'
    }

    def __init__(self, annotations=None, api_version='v1beta1', config=None, functions=None, metadata=None, type='Plugin', local_vars_configuration=None):  # noqa: E501
        """Plugin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._api_version = None
        self._config = None
        self._functions = None
        self._metadata = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if api_version is not None:
            self.api_version = api_version
        self.config = config
        self.functions = functions
        self.metadata = metadata
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this Plugin.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this Plugin.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Plugin.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this Plugin.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def api_version(self):
        """Gets the api_version of this Plugin.  # noqa: E501


        :return: The api_version of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this Plugin.


        :param api_version: The api_version of this Plugin.  # noqa: E501
        :type api_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_version is not None and not re.search(r'^v1beta1$', api_version)):  # noqa: E501
            raise ValueError(r"Invalid value for `api_version`, must be a follow pattern or equal to `/^v1beta1$/`")  # noqa: E501

        self._api_version = api_version

    @property
    def config(self):
        """Gets the config of this Plugin.  # noqa: E501

        The configuration information to run this plugin  # noqa: E501

        :return: The config of this Plugin.  # noqa: E501
        :rtype: PluginConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Plugin.

        The configuration information to run this plugin  # noqa: E501

        :param config: The config of this Plugin.  # noqa: E501
        :type config: PluginConfig
        """
        if self.local_vars_configuration.client_side_validation and config is None:  # noqa: E501
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def functions(self):
        """Gets the functions of this Plugin.  # noqa: E501

        List of Plugin functions  # noqa: E501

        :return: The functions of this Plugin.  # noqa: E501
        :rtype: list[Function]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """Sets the functions of this Plugin.

        List of Plugin functions  # noqa: E501

        :param functions: The functions of this Plugin.  # noqa: E501
        :type functions: list[Function]
        """
        if self.local_vars_configuration.client_side_validation and functions is None:  # noqa: E501
            raise ValueError("Invalid value for `functions`, must not be `None`")  # noqa: E501

        self._functions = functions

    @property
    def metadata(self):
        """Gets the metadata of this Plugin.  # noqa: E501

        The Plugin metadata information  # noqa: E501

        :return: The metadata of this Plugin.  # noqa: E501
        :rtype: MetaData
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Plugin.

        The Plugin metadata information  # noqa: E501

        :param metadata: The metadata of this Plugin.  # noqa: E501
        :type metadata: MetaData
        """
        if self.local_vars_configuration.client_side_validation and metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def type(self):
        """Gets the type of this Plugin.  # noqa: E501


        :return: The type of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Plugin.


        :param type: The type of this Plugin.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^Plugin', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^Plugin/`")  # noqa: E501

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
        if not isinstance(other, Plugin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Plugin):
            return True

        return self.to_dict() != other.to_dict()
