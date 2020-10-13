# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Dependency(object):
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
        'alias': 'str',
        'hash': 'str',
        'name': 'str',
        'source': 'str',
        'tag': 'str',
        'type': 'DependencyType'
    }

    attribute_map = {
        'alias': 'alias',
        'hash': 'hash',
        'name': 'name',
        'source': 'source',
        'tag': 'tag',
        'type': 'type'
    }

    def __init__(self, alias=None, hash=None, name=None, source=None, tag=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Dependency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alias = None
        self._hash = None
        self._name = None
        self._source = None
        self._tag = None
        self._type = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if hash is not None:
            self.hash = hash
        self.name = name
        self.source = source
        self.tag = tag
        self.type = type

    @property
    def alias(self):
        """Gets the alias of this Dependency.  # noqa: E501

        An optional alias to refer to this dependency. Useful if the name is already used somewhere else.  # noqa: E501

        :return: The alias of this Dependency.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this Dependency.

        An optional alias to refer to this dependency. Useful if the name is already used somewhere else.  # noqa: E501

        :param alias: The alias of this Dependency.  # noqa: E501
        :type alias: str
        """

        self._alias = alias

    @property
    def hash(self):
        """Gets the hash of this Dependency.  # noqa: E501

        The digest hash of the dependency when retrieved from its source. This is locked when the resource dependencies are downloaded.  # noqa: E501

        :return: The hash of this Dependency.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Dependency.

        The digest hash of the dependency when retrieved from its source. This is locked when the resource dependencies are downloaded.  # noqa: E501

        :param hash: The hash of this Dependency.  # noqa: E501
        :type hash: str
        """

        self._hash = hash

    @property
    def name(self):
        """Gets the name of this Dependency.  # noqa: E501

        Workflow name. This name should be unique among all the resources in your resource. Use an alias if this is not the case.  # noqa: E501

        :return: The name of this Dependency.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dependency.

        Workflow name. This name should be unique among all the resources in your resource. Use an alias if this is not the case.  # noqa: E501

        :param name: The name of this Dependency.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def source(self):
        """Gets the source of this Dependency.  # noqa: E501

        URL to a repository where this resource can be found.  # noqa: E501

        :return: The source of this Dependency.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Dependency.

        URL to a repository where this resource can be found.  # noqa: E501

        :param source: The source of this Dependency.  # noqa: E501
        :type source: str
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def tag(self):
        """Gets the tag of this Dependency.  # noqa: E501

        Tag of the resource.  # noqa: E501

        :return: The tag of this Dependency.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Dependency.

        Tag of the resource.  # noqa: E501

        :param tag: The tag of this Dependency.  # noqa: E501
        :type tag: str
        """
        if self.local_vars_configuration.client_side_validation and tag is None:  # noqa: E501
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def type(self):
        """Gets the type of this Dependency.  # noqa: E501


        :return: The type of this Dependency.  # noqa: E501
        :rtype: DependencyType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Dependency.


        :param type: The type of this Dependency.  # noqa: E501
        :type type: DependencyType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, Dependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Dependency):
            return True

        return self.to_dict() != other.to_dict()