# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: v0.9.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class DAGInputArtifact(object):
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
        'default': 'AnyOfHTTPSourceS3SourceProjectFolderSource',
        'description': 'str',
        'name': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'annotations': 'annotations',
        'default': 'default',
        'description': 'description',
        'name': 'name',
        'required': 'required'
    }

    def __init__(self, annotations=None, default=None, description=None, name=None, required=None, local_vars_configuration=None):  # noqa: E501
        """DAGInputArtifact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._default = None
        self._description = None
        self._name = None
        self._required = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        self.name = name
        if required is not None:
            self.required = required

    @property
    def annotations(self):
        """Gets the annotations of this DAGInputArtifact.  # noqa: E501

        Optional annotations for Queenbee objects.  # noqa: E501

        :return: The annotations of this DAGInputArtifact.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this DAGInputArtifact.

        Optional annotations for Queenbee objects.  # noqa: E501

        :param annotations: The annotations of this DAGInputArtifact.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def default(self):
        """Gets the default of this DAGInputArtifact.  # noqa: E501

        If no artifact is specified then pull it from this source location.  # noqa: E501

        :return: The default of this DAGInputArtifact.  # noqa: E501
        :rtype: AnyOfHTTPSourceS3SourceProjectFolderSource
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this DAGInputArtifact.

        If no artifact is specified then pull it from this source location.  # noqa: E501

        :param default: The default of this DAGInputArtifact.  # noqa: E501
        :type default: AnyOfHTTPSourceS3SourceProjectFolderSource
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this DAGInputArtifact.  # noqa: E501

        Optional description for the input artifact  # noqa: E501

        :return: The description of this DAGInputArtifact.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DAGInputArtifact.

        Optional description for the input artifact  # noqa: E501

        :param description: The description of this DAGInputArtifact.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this DAGInputArtifact.  # noqa: E501

        The name of the artifact within the scope of the DAG  # noqa: E501

        :return: The name of this DAGInputArtifact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DAGInputArtifact.

        The name of the artifact within the scope of the DAG  # noqa: E501

        :param name: The name of this DAGInputArtifact.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def required(self):
        """Gets the required of this DAGInputArtifact.  # noqa: E501

        Whether this value must be specified in a task argument.  # noqa: E501

        :return: The required of this DAGInputArtifact.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this DAGInputArtifact.

        Whether this value must be specified in a task argument.  # noqa: E501

        :param required: The required of this DAGInputArtifact.  # noqa: E501
        :type required: bool
        """

        self._required = required

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
        if not isinstance(other, DAGInputArtifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DAGInputArtifact):
            return True

        return self.to_dict() != other.to_dict()
