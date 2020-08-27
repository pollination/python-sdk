# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.8.7
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
        'metadata': 'QueenbeeRecipeMetadataMetaData',
        'dependencies': 'list[Dependency]',
        'flow': 'list[DAG]'
    }

    attribute_map = {
        'metadata': 'metadata',
        'dependencies': 'dependencies',
        'flow': 'flow'
    }

    def __init__(self, metadata=None, dependencies=None, flow=None, local_vars_configuration=None):  # noqa: E501
        """Recipe - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metadata = None
        self._dependencies = None
        self._flow = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if dependencies is not None:
            self.dependencies = dependencies
        self.flow = flow

    @property
    def metadata(self):
        """Gets the metadata of this Recipe.  # noqa: E501

        Recipe metadata information.  # noqa: E501

        :return: The metadata of this Recipe.  # noqa: E501
        :rtype: QueenbeeRecipeMetadataMetaData
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Recipe.

        Recipe metadata information.  # noqa: E501

        :param metadata: The metadata of this Recipe.  # noqa: E501
        :type: QueenbeeRecipeMetadataMetaData
        """

        self._metadata = metadata

    @property
    def dependencies(self):
        """Gets the dependencies of this Recipe.  # noqa: E501

        A list of operators and other recipes this recipe depends on.  # noqa: E501

        :return: The dependencies of this Recipe.  # noqa: E501
        :rtype: list[Dependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this Recipe.

        A list of operators and other recipes this recipe depends on.  # noqa: E501

        :param dependencies: The dependencies of this Recipe.  # noqa: E501
        :type: list[Dependency]
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
        :type: list[DAG]
        """
        if self.local_vars_configuration.client_side_validation and flow is None:  # noqa: E501
            raise ValueError("Invalid value for `flow`, must not be `None`")  # noqa: E501

        self._flow = flow

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
