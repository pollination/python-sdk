# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.37.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Recipe(object):
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
        'dependencies': 'list[Dependency]',
        'flow': 'list[DAG]',
        'metadata': 'MetaData',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'api_version': 'api_version',
        'dependencies': 'dependencies',
        'flow': 'flow',
        'metadata': 'metadata',
        'type': 'type'
    }

    def __init__(self, annotations=None, api_version='v1beta1', dependencies=None, flow=None, metadata=None, type='Recipe', local_vars_configuration=None):  # noqa: E501
        """Recipe - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._api_version = None
        self._dependencies = None
        self._flow = None
        self._metadata = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if api_version is not None:
            self.api_version = api_version
        if dependencies is not None:
            self.dependencies = dependencies
        self.flow = flow
        if metadata is not None:
            self.metadata = metadata
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this Recipe.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this Recipe.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Recipe.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this Recipe.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def api_version(self):
        """Gets the api_version of this Recipe.  # noqa: E501


        :return: The api_version of this Recipe.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this Recipe.


        :param api_version: The api_version of this Recipe.  # noqa: E501
        :type api_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_version is not None and not re.search(r'^v1beta1$', api_version)):  # noqa: E501
            raise ValueError(r"Invalid value for `api_version`, must be a follow pattern or equal to `/^v1beta1$/`")  # noqa: E501

        self._api_version = api_version

    @property
    def dependencies(self):
        """Gets the dependencies of this Recipe.  # noqa: E501

        A list of plugins and other recipes this recipe depends on.  # noqa: E501

        :return: The dependencies of this Recipe.  # noqa: E501
        :rtype: list[Dependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this Recipe.

        A list of plugins and other recipes this recipe depends on.  # noqa: E501

        :param dependencies: The dependencies of this Recipe.  # noqa: E501
        :type dependencies: list[Dependency]
        """

        self._dependencies = dependencies

    @property
    def flow(self):
        """Gets the flow of this Recipe.  # noqa: E501

        A list of tasks to create a DAG recipe.  # noqa: E501

        :return: The flow of this Recipe.  # noqa: E501
        :rtype: list[DAG]
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this Recipe.

        A list of tasks to create a DAG recipe.  # noqa: E501

        :param flow: The flow of this Recipe.  # noqa: E501
        :type flow: list[DAG]
        """
        if self.local_vars_configuration.client_side_validation and flow is None:  # noqa: E501
            raise ValueError("Invalid value for `flow`, must not be `None`")  # noqa: E501

        self._flow = flow

    @property
    def metadata(self):
        """Gets the metadata of this Recipe.  # noqa: E501

        Recipe metadata information.  # noqa: E501

        :return: The metadata of this Recipe.  # noqa: E501
        :rtype: MetaData
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Recipe.

        Recipe metadata information.  # noqa: E501

        :param metadata: The metadata of this Recipe.  # noqa: E501
        :type metadata: MetaData
        """

        self._metadata = metadata

    @property
    def type(self):
        """Gets the type of this Recipe.  # noqa: E501


        :return: The type of this Recipe.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Recipe.


        :param type: The type of this Recipe.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^Recipe$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^Recipe$/`")  # noqa: E501

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
        if not isinstance(other, Recipe):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Recipe):
            return True

        return self.to_dict() != other.to_dict()
