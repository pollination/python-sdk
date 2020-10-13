# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class InputArtifactReference(object):
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
        'type': 'InputReference',
        'variable': 'str'
    }

    attribute_map = {
        'type': 'type',
        'variable': 'variable'
    }

    def __init__(self, type=None, variable=None, local_vars_configuration=None):  # noqa: E501
        """InputArtifactReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._variable = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.variable = variable

    @property
    def type(self):
        """Gets the type of this InputArtifactReference.  # noqa: E501


        :return: The type of this InputArtifactReference.  # noqa: E501
        :rtype: InputReference
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InputArtifactReference.


        :param type: The type of this InputArtifactReference.  # noqa: E501
        :type type: InputReference
        """

        self._type = type

    @property
    def variable(self):
        """Gets the variable of this InputArtifactReference.  # noqa: E501

        The name of the DAG input variable  # noqa: E501

        :return: The variable of this InputArtifactReference.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this InputArtifactReference.

        The name of the DAG input variable  # noqa: E501

        :param variable: The variable of this InputArtifactReference.  # noqa: E501
        :type variable: str
        """
        if self.local_vars_configuration.client_side_validation and variable is None:  # noqa: E501
            raise ValueError("Invalid value for `variable`, must not be `None`")  # noqa: E501

        self._variable = variable

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
        if not isinstance(other, InputArtifactReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputArtifactReference):
            return True

        return self.to_dict() != other.to_dict()
