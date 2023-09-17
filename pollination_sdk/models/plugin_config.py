# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.44.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class PluginConfig(object):
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
        'docker': 'DockerConfig',
        'local': 'LocalConfig',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'docker': 'docker',
        'local': 'local',
        'type': 'type'
    }

    def __init__(self, annotations=None, docker=None, local=None, type='PluginConfig', local_vars_configuration=None):  # noqa: E501
        """PluginConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._docker = None
        self._local = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        self.docker = docker
        if local is not None:
            self.local = local
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this PluginConfig.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this PluginConfig.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this PluginConfig.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this PluginConfig.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def docker(self):
        """Gets the docker of this PluginConfig.  # noqa: E501

        The configuration to use this plugin in a docker container  # noqa: E501

        :return: The docker of this PluginConfig.  # noqa: E501
        :rtype: DockerConfig
        """
        return self._docker

    @docker.setter
    def docker(self, docker):
        """Sets the docker of this PluginConfig.

        The configuration to use this plugin in a docker container  # noqa: E501

        :param docker: The docker of this PluginConfig.  # noqa: E501
        :type docker: DockerConfig
        """
        if self.local_vars_configuration.client_side_validation and docker is None:  # noqa: E501
            raise ValueError("Invalid value for `docker`, must not be `None`")  # noqa: E501

        self._docker = docker

    @property
    def local(self):
        """Gets the local of this PluginConfig.  # noqa: E501

        The configuration to use this plugin locally  # noqa: E501

        :return: The local of this PluginConfig.  # noqa: E501
        :rtype: LocalConfig
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this PluginConfig.

        The configuration to use this plugin locally  # noqa: E501

        :param local: The local of this PluginConfig.  # noqa: E501
        :type local: LocalConfig
        """

        self._local = local

    @property
    def type(self):
        """Gets the type of this PluginConfig.  # noqa: E501


        :return: The type of this PluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PluginConfig.


        :param type: The type of this PluginConfig.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^PluginConfig', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^PluginConfig/`")  # noqa: E501

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
        if not isinstance(other, PluginConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginConfig):
            return True

        return self.to_dict() != other.to_dict()
