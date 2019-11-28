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


class Plastic(object):
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
        'r_reflectance': 'float',
        'g_reflectance': 'float',
        'b_reflectance': 'float',
        'specularity': 'float',
        'roughness': 'float',
        'modifier': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'r_reflectance': 'r_reflectance',
        'g_reflectance': 'g_reflectance',
        'b_reflectance': 'b_reflectance',
        'specularity': 'specularity',
        'roughness': 'roughness',
        'modifier': 'modifier'
    }

    def __init__(self, type=None, name=None, r_reflectance=None, g_reflectance=None, b_reflectance=None, specularity=None, roughness=None, modifier='void', local_vars_configuration=None):  # noqa: E501
        """Plastic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._r_reflectance = None
        self._g_reflectance = None
        self._b_reflectance = None
        self._specularity = None
        self._roughness = None
        self._modifier = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.r_reflectance = r_reflectance
        self.g_reflectance = g_reflectance
        self.b_reflectance = b_reflectance
        self.specularity = specularity
        self.roughness = roughness
        if modifier is not None:
            self.modifier = modifier

    @property
    def type(self):
        """Gets the type of this Plastic.  # noqa: E501


        :return: The type of this Plastic.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Plastic.


        :param type: The type of this Plastic.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Plastic"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this Plastic.  # noqa: E501


        :return: The name of this Plastic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Plastic.


        :param name: The name of this Plastic.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[.A-Za-z0-9_-]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[.A-Za-z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def r_reflectance(self):
        """Gets the r_reflectance of this Plastic.  # noqa: E501


        :return: The r_reflectance of this Plastic.  # noqa: E501
        :rtype: float
        """
        return self._r_reflectance

    @r_reflectance.setter
    def r_reflectance(self, r_reflectance):
        """Sets the r_reflectance of this Plastic.


        :param r_reflectance: The r_reflectance of this Plastic.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and r_reflectance is None:  # noqa: E501
            raise ValueError("Invalid value for `r_reflectance`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                r_reflectance is not None and r_reflectance > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `r_reflectance`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                r_reflectance is not None and r_reflectance < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `r_reflectance`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._r_reflectance = r_reflectance

    @property
    def g_reflectance(self):
        """Gets the g_reflectance of this Plastic.  # noqa: E501


        :return: The g_reflectance of this Plastic.  # noqa: E501
        :rtype: float
        """
        return self._g_reflectance

    @g_reflectance.setter
    def g_reflectance(self, g_reflectance):
        """Sets the g_reflectance of this Plastic.


        :param g_reflectance: The g_reflectance of this Plastic.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and g_reflectance is None:  # noqa: E501
            raise ValueError("Invalid value for `g_reflectance`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                g_reflectance is not None and g_reflectance > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `g_reflectance`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                g_reflectance is not None and g_reflectance < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `g_reflectance`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._g_reflectance = g_reflectance

    @property
    def b_reflectance(self):
        """Gets the b_reflectance of this Plastic.  # noqa: E501


        :return: The b_reflectance of this Plastic.  # noqa: E501
        :rtype: float
        """
        return self._b_reflectance

    @b_reflectance.setter
    def b_reflectance(self, b_reflectance):
        """Sets the b_reflectance of this Plastic.


        :param b_reflectance: The b_reflectance of this Plastic.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and b_reflectance is None:  # noqa: E501
            raise ValueError("Invalid value for `b_reflectance`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                b_reflectance is not None and b_reflectance > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `b_reflectance`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                b_reflectance is not None and b_reflectance < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `b_reflectance`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._b_reflectance = b_reflectance

    @property
    def specularity(self):
        """Gets the specularity of this Plastic.  # noqa: E501


        :return: The specularity of this Plastic.  # noqa: E501
        :rtype: float
        """
        return self._specularity

    @specularity.setter
    def specularity(self, specularity):
        """Sets the specularity of this Plastic.


        :param specularity: The specularity of this Plastic.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and specularity is None:  # noqa: E501
            raise ValueError("Invalid value for `specularity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                specularity is not None and specularity > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `specularity`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                specularity is not None and specularity < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `specularity`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._specularity = specularity

    @property
    def roughness(self):
        """Gets the roughness of this Plastic.  # noqa: E501


        :return: The roughness of this Plastic.  # noqa: E501
        :rtype: float
        """
        return self._roughness

    @roughness.setter
    def roughness(self, roughness):
        """Sets the roughness of this Plastic.


        :param roughness: The roughness of this Plastic.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and roughness is None:  # noqa: E501
            raise ValueError("Invalid value for `roughness`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                roughness is not None and roughness > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `roughness`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                roughness is not None and roughness < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `roughness`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._roughness = roughness

    @property
    def modifier(self):
        """Gets the modifier of this Plastic.  # noqa: E501


        :return: The modifier of this Plastic.  # noqa: E501
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this Plastic.


        :param modifier: The modifier of this Plastic.  # noqa: E501
        :type: str
        """

        self._modifier = modifier

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
        if not isinstance(other, Plastic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Plastic):
            return True

        return self.to_dict() != other.to_dict()
