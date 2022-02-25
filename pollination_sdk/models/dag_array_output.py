# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.26.3
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class DAGArrayOutput(object):
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
        'alias': 'list[AnyOfDAGGenericOutputAliasDAGStringOutputAliasDAGIntegerOutputAliasDAGNumberOutputAliasDAGBooleanOutputAliasDAGFolderOutputAliasDAGFileOutputAliasDAGPathOutputAliasDAGArrayOutputAliasDAGJSONObjectOutputAliasDAGLinkedOutputAlias]',
        'annotations': 'dict(str, str)',
        'description': 'str',
        '_from': 'AnyOfTaskReferenceFileReference',
        'items_type': 'ItemType',
        'name': 'str',
        'required': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'annotations': 'annotations',
        'description': 'description',
        '_from': 'from',
        'items_type': 'items_type',
        'name': 'name',
        'required': 'required',
        'type': 'type'
    }

    def __init__(self, alias=None, annotations=None, description=None, _from=None, items_type=None, name=None, required=True, type='DAGArrayOutput', local_vars_configuration=None):  # noqa: E501
        """DAGArrayOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alias = None
        self._annotations = None
        self._description = None
        self.__from = None
        self._items_type = None
        self._name = None
        self._required = None
        self._type = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if annotations is not None:
            self.annotations = annotations
        if description is not None:
            self.description = description
        self._from = _from
        if items_type is not None:
            self.items_type = items_type
        self.name = name
        if required is not None:
            self.required = required
        if type is not None:
            self.type = type

    @property
    def alias(self):
        """Gets the alias of this DAGArrayOutput.  # noqa: E501

        A list of additional processes for loading this output on different platforms.  # noqa: E501

        :return: The alias of this DAGArrayOutput.  # noqa: E501
        :rtype: list[AnyOfDAGGenericOutputAliasDAGStringOutputAliasDAGIntegerOutputAliasDAGNumberOutputAliasDAGBooleanOutputAliasDAGFolderOutputAliasDAGFileOutputAliasDAGPathOutputAliasDAGArrayOutputAliasDAGJSONObjectOutputAliasDAGLinkedOutputAlias]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this DAGArrayOutput.

        A list of additional processes for loading this output on different platforms.  # noqa: E501

        :param alias: The alias of this DAGArrayOutput.  # noqa: E501
        :type alias: list[AnyOfDAGGenericOutputAliasDAGStringOutputAliasDAGIntegerOutputAliasDAGNumberOutputAliasDAGBooleanOutputAliasDAGFolderOutputAliasDAGFileOutputAliasDAGPathOutputAliasDAGArrayOutputAliasDAGJSONObjectOutputAliasDAGLinkedOutputAlias]
        """

        self._alias = alias

    @property
    def annotations(self):
        """Gets the annotations of this DAGArrayOutput.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this DAGArrayOutput.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this DAGArrayOutput.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this DAGArrayOutput.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def description(self):
        """Gets the description of this DAGArrayOutput.  # noqa: E501

        Optional description for output.  # noqa: E501

        :return: The description of this DAGArrayOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DAGArrayOutput.

        Optional description for output.  # noqa: E501

        :param description: The description of this DAGArrayOutput.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def _from(self):
        """Gets the _from of this DAGArrayOutput.  # noqa: E501

        Reference to a file or a task output. Task output must be file.  # noqa: E501

        :return: The _from of this DAGArrayOutput.  # noqa: E501
        :rtype: AnyOfTaskReferenceFileReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this DAGArrayOutput.

        Reference to a file or a task output. Task output must be file.  # noqa: E501

        :param _from: The _from of this DAGArrayOutput.  # noqa: E501
        :type _from: AnyOfTaskReferenceFileReference
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def items_type(self):
        """Gets the items_type of this DAGArrayOutput.  # noqa: E501

        Type of items in this array. All the items in an array must be from the same type.  # noqa: E501

        :return: The items_type of this DAGArrayOutput.  # noqa: E501
        :rtype: ItemType
        """
        return self._items_type

    @items_type.setter
    def items_type(self, items_type):
        """Sets the items_type of this DAGArrayOutput.

        Type of items in this array. All the items in an array must be from the same type.  # noqa: E501

        :param items_type: The items_type of this DAGArrayOutput.  # noqa: E501
        :type items_type: ItemType
        """

        self._items_type = items_type

    @property
    def name(self):
        """Gets the name of this DAGArrayOutput.  # noqa: E501

        Output name.  # noqa: E501

        :return: The name of this DAGArrayOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DAGArrayOutput.

        Output name.  # noqa: E501

        :param name: The name of this DAGArrayOutput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def required(self):
        """Gets the required of this DAGArrayOutput.  # noqa: E501

        A boolean to indicate if an artifact output is required. A False value makes the artifact optional.  # noqa: E501

        :return: The required of this DAGArrayOutput.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this DAGArrayOutput.

        A boolean to indicate if an artifact output is required. A False value makes the artifact optional.  # noqa: E501

        :param required: The required of this DAGArrayOutput.  # noqa: E501
        :type required: bool
        """

        self._required = required

    @property
    def type(self):
        """Gets the type of this DAGArrayOutput.  # noqa: E501


        :return: The type of this DAGArrayOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DAGArrayOutput.


        :param type: The type of this DAGArrayOutput.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^DAGArrayOutput$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^DAGArrayOutput$/`")  # noqa: E501

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
        if not isinstance(other, DAGArrayOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DAGArrayOutput):
            return True

        return self.to_dict() != other.to_dict()
