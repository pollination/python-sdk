# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.20.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class ProductFamily(object):
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
        'active': 'bool',
        'description': 'str',
        'id': 'str',
        'metadata': 'object',
        'name': 'str',
        'prices': 'list[Price]'
    }

    attribute_map = {
        'active': 'active',
        'description': 'description',
        'id': 'id',
        'metadata': 'metadata',
        'name': 'name',
        'prices': 'prices'
    }

    def __init__(self, active=None, description=None, id=None, metadata=None, name=None, prices=None, local_vars_configuration=None):  # noqa: E501
        """ProductFamily - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._description = None
        self._id = None
        self._metadata = None
        self._name = None
        self._prices = None
        self.discriminator = None

        self.active = active
        if description is not None:
            self.description = description
        self.id = id
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        self.prices = prices

    @property
    def active(self):
        """Gets the active of this ProductFamily.  # noqa: E501


        :return: The active of this ProductFamily.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ProductFamily.


        :param active: The active of this ProductFamily.  # noqa: E501
        :type active: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def description(self):
        """Gets the description of this ProductFamily.  # noqa: E501


        :return: The description of this ProductFamily.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductFamily.


        :param description: The description of this ProductFamily.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ProductFamily.  # noqa: E501


        :return: The id of this ProductFamily.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductFamily.


        :param id: The id of this ProductFamily.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this ProductFamily.  # noqa: E501


        :return: The metadata of this ProductFamily.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ProductFamily.


        :param metadata: The metadata of this ProductFamily.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this ProductFamily.  # noqa: E501


        :return: The name of this ProductFamily.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductFamily.


        :param name: The name of this ProductFamily.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def prices(self):
        """Gets the prices of this ProductFamily.  # noqa: E501


        :return: The prices of this ProductFamily.  # noqa: E501
        :rtype: list[Price]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this ProductFamily.


        :param prices: The prices of this ProductFamily.  # noqa: E501
        :type prices: list[Price]
        """
        if self.local_vars_configuration.client_side_validation and prices is None:  # noqa: E501
            raise ValueError("Invalid value for `prices`, must not be `None`")  # noqa: E501

        self._prices = prices

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
        if not isinstance(other, ProductFamily):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductFamily):
            return True

        return self.to_dict() != other.to_dict()
