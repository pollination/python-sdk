# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.35.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class DAGFolderInput(object):
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
        'alias': 'list[AnyOfDAGGenericInputAliasDAGStringInputAliasDAGIntegerInputAliasDAGNumberInputAliasDAGBooleanInputAliasDAGFolderInputAliasDAGFileInputAliasDAGPathInputAliasDAGArrayInputAliasDAGJSONObjectInputAliasDAGLinkedInputAlias]',
        'annotations': 'dict(str, str)',
        'default': 'AnyOfHTTPS3ProjectFolder',
        'description': 'str',
        'name': 'str',
        'required': 'bool',
        'spec': 'object',
        'type': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'annotations': 'annotations',
        'default': 'default',
        'description': 'description',
        'name': 'name',
        'required': 'required',
        'spec': 'spec',
        'type': 'type'
    }

    def __init__(self, alias=None, annotations=None, default=None, description=None, name=None, required=False, spec=None, type='DAGFolderInput', local_vars_configuration=None):  # noqa: E501
        """DAGFolderInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alias = None
        self._annotations = None
        self._default = None
        self._description = None
        self._name = None
        self._required = None
        self._spec = None
        self._type = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if annotations is not None:
            self.annotations = annotations
        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        self.name = name
        if required is not None:
            self.required = required
        if spec is not None:
            self.spec = spec
        if type is not None:
            self.type = type

    @property
    def alias(self):
        """Gets the alias of this DAGFolderInput.  # noqa: E501

        A list of aliases for this input in different platforms.  # noqa: E501

        :return: The alias of this DAGFolderInput.  # noqa: E501
        :rtype: list[AnyOfDAGGenericInputAliasDAGStringInputAliasDAGIntegerInputAliasDAGNumberInputAliasDAGBooleanInputAliasDAGFolderInputAliasDAGFileInputAliasDAGPathInputAliasDAGArrayInputAliasDAGJSONObjectInputAliasDAGLinkedInputAlias]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this DAGFolderInput.

        A list of aliases for this input in different platforms.  # noqa: E501

        :param alias: The alias of this DAGFolderInput.  # noqa: E501
        :type alias: list[AnyOfDAGGenericInputAliasDAGStringInputAliasDAGIntegerInputAliasDAGNumberInputAliasDAGBooleanInputAliasDAGFolderInputAliasDAGFileInputAliasDAGPathInputAliasDAGArrayInputAliasDAGJSONObjectInputAliasDAGLinkedInputAlias]
        """

        self._alias = alias

    @property
    def annotations(self):
        """Gets the annotations of this DAGFolderInput.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this DAGFolderInput.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this DAGFolderInput.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this DAGFolderInput.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def default(self):
        """Gets the default of this DAGFolderInput.  # noqa: E501

        The default source for file if the value is not provided.  # noqa: E501

        :return: The default of this DAGFolderInput.  # noqa: E501
        :rtype: AnyOfHTTPS3ProjectFolder
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this DAGFolderInput.

        The default source for file if the value is not provided.  # noqa: E501

        :param default: The default of this DAGFolderInput.  # noqa: E501
        :type default: AnyOfHTTPS3ProjectFolder
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this DAGFolderInput.  # noqa: E501

        Optional description for input.  # noqa: E501

        :return: The description of this DAGFolderInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DAGFolderInput.

        Optional description for input.  # noqa: E501

        :param description: The description of this DAGFolderInput.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this DAGFolderInput.  # noqa: E501

        Input name.  # noqa: E501

        :return: The name of this DAGFolderInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DAGFolderInput.

        Input name.  # noqa: E501

        :param name: The name of this DAGFolderInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def required(self):
        """Gets the required of this DAGFolderInput.  # noqa: E501

        A field to indicate if this input is required. This input needs to be set explicitly even when a default value is provided.  # noqa: E501

        :return: The required of this DAGFolderInput.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this DAGFolderInput.

        A field to indicate if this input is required. This input needs to be set explicitly even when a default value is provided.  # noqa: E501

        :param required: The required of this DAGFolderInput.  # noqa: E501
        :type required: bool
        """

        self._required = required

    @property
    def spec(self):
        """Gets the spec of this DAGFolderInput.  # noqa: E501

        An optional JSON Schema specification to validate the input value. You can use validate_spec method to validate a value against the spec.  # noqa: E501

        :return: The spec of this DAGFolderInput.  # noqa: E501
        :rtype: object
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this DAGFolderInput.

        An optional JSON Schema specification to validate the input value. You can use validate_spec method to validate a value against the spec.  # noqa: E501

        :param spec: The spec of this DAGFolderInput.  # noqa: E501
        :type spec: object
        """

        self._spec = spec

    @property
    def type(self):
        """Gets the type of this DAGFolderInput.  # noqa: E501


        :return: The type of this DAGFolderInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DAGFolderInput.


        :param type: The type of this DAGFolderInput.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^DAGFolderInput$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^DAGFolderInput$/`")  # noqa: E501

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
        if not isinstance(other, DAGFolderInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DAGFolderInput):
            return True

        return self.to_dict() != other.to_dict()
