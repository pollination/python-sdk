# coding: utf-8

"""
    pollination.cloud

    Pollination Cloud API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Model(object):
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
        'type': 'str',
        'name': 'str',
        'convert_to_meters': 'float',
        'faces': 'list[object]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'convert_to_meters': 'convert_to_meters',
        'faces': 'faces'
    }

    def __init__(self, type=None, name=None, convert_to_meters=1, faces=[], local_vars_configuration=None):  # noqa: E501
        """Model - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._convert_to_meters = None
        self._faces = None
        self.discriminator = None

        self.type = type
        self.name = name
        if convert_to_meters is not None:
            self.convert_to_meters = convert_to_meters
        if faces is not None:
            self.faces = faces

    @property
    def type(self):
        """Gets the type of this Model.  # noqa: E501


        :return: The type of this Model.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Model.


        :param type: The type of this Model.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Model"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this Model.  # noqa: E501

        Model name  # noqa: E501

        :return: The name of this Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Model.

        Model name  # noqa: E501

        :param name: The name of this Model.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[.A-Za-z0-9_-]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[.A-Za-z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def convert_to_meters(self):
        """Gets the convert_to_meters of this Model.  # noqa: E501

        Value to use to convert the current model into meters  # noqa: E501

        :return: The convert_to_meters of this Model.  # noqa: E501
        :rtype: float
        """
        return self._convert_to_meters

    @convert_to_meters.setter
    def convert_to_meters(self, convert_to_meters):
        """Sets the convert_to_meters of this Model.

        Value to use to convert the current model into meters  # noqa: E501

        :param convert_to_meters: The convert_to_meters of this Model.  # noqa: E501
        :type: float
        """

        self._convert_to_meters = convert_to_meters

    @property
    def faces(self):
        """Gets the faces of this Model.  # noqa: E501

        List of model faces, can be of type Face or ShadeFace  # noqa: E501

        :return: The faces of this Model.  # noqa: E501
        :rtype: list[object]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this Model.

        List of model faces, can be of type Face or ShadeFace  # noqa: E501

        :param faces: The faces of this Model.  # noqa: E501
        :type: list[object]
        """

        self._faces = faces

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
        if not isinstance(other, Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Model):
            return True

        return self.to_dict() != other.to_dict()
