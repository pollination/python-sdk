# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.27.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Function(object):
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
        'command': 'str',
        'description': 'str',
        'inputs': 'list[AnyOfFunctionStringInputFunctionIntegerInputFunctionNumberInputFunctionBooleanInputFunctionFolderInputFunctionFileInputFunctionPathInputFunctionArrayInputFunctionJSONObjectInput]',
        'name': 'str',
        'outputs': 'list[AnyOfFunctionStringOutputFunctionIntegerOutputFunctionNumberOutputFunctionBooleanOutputFunctionFolderOutputFunctionFileOutputFunctionPathOutputFunctionArrayOutputFunctionJSONObjectOutput]',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'command': 'command',
        'description': 'description',
        'inputs': 'inputs',
        'name': 'name',
        'outputs': 'outputs',
        'type': 'type'
    }

    def __init__(self, annotations=None, command=None, description=None, inputs=None, name=None, outputs=None, type='Function', local_vars_configuration=None):  # noqa: E501
        """Function - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._command = None
        self._description = None
        self._inputs = None
        self._name = None
        self._outputs = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        self.command = command
        if description is not None:
            self.description = description
        if inputs is not None:
            self.inputs = inputs
        self.name = name
        if outputs is not None:
            self.outputs = outputs
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this Function.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this Function.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Function.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this Function.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def command(self):
        """Gets the command of this Function.  # noqa: E501

        Full shell command for this function. Each function accepts only one command. The command will be executed as a shell command in plugin. For running several commands after each other use && between the commands or pipe data from one to another using |  # noqa: E501

        :return: The command of this Function.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this Function.

        Full shell command for this function. Each function accepts only one command. The command will be executed as a shell command in plugin. For running several commands after each other use && between the commands or pipe data from one to another using |  # noqa: E501

        :param command: The command of this Function.  # noqa: E501
        :type command: str
        """
        if self.local_vars_configuration.client_side_validation and command is None:  # noqa: E501
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def description(self):
        """Gets the description of this Function.  # noqa: E501

        Function description. A short human readable description for this function.  # noqa: E501

        :return: The description of this Function.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Function.

        Function description. A short human readable description for this function.  # noqa: E501

        :param description: The description of this Function.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def inputs(self):
        """Gets the inputs of this Function.  # noqa: E501

        Input arguments for this function.  # noqa: E501

        :return: The inputs of this Function.  # noqa: E501
        :rtype: list[AnyOfFunctionStringInputFunctionIntegerInputFunctionNumberInputFunctionBooleanInputFunctionFolderInputFunctionFileInputFunctionPathInputFunctionArrayInputFunctionJSONObjectInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this Function.

        Input arguments for this function.  # noqa: E501

        :param inputs: The inputs of this Function.  # noqa: E501
        :type inputs: list[AnyOfFunctionStringInputFunctionIntegerInputFunctionNumberInputFunctionBooleanInputFunctionFolderInputFunctionFileInputFunctionPathInputFunctionArrayInputFunctionJSONObjectInput]
        """

        self._inputs = inputs

    @property
    def name(self):
        """Gets the name of this Function.  # noqa: E501

        Function name. Must be unique within a plugin.  # noqa: E501

        :return: The name of this Function.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Function.

        Function name. Must be unique within a plugin.  # noqa: E501

        :param name: The name of this Function.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def outputs(self):
        """Gets the outputs of this Function.  # noqa: E501

        List of output arguments.  # noqa: E501

        :return: The outputs of this Function.  # noqa: E501
        :rtype: list[AnyOfFunctionStringOutputFunctionIntegerOutputFunctionNumberOutputFunctionBooleanOutputFunctionFolderOutputFunctionFileOutputFunctionPathOutputFunctionArrayOutputFunctionJSONObjectOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Function.

        List of output arguments.  # noqa: E501

        :param outputs: The outputs of this Function.  # noqa: E501
        :type outputs: list[AnyOfFunctionStringOutputFunctionIntegerOutputFunctionNumberOutputFunctionBooleanOutputFunctionFolderOutputFunctionFileOutputFunctionPathOutputFunctionArrayOutputFunctionJSONObjectOutput]
        """

        self._outputs = outputs

    @property
    def type(self):
        """Gets the type of this Function.  # noqa: E501


        :return: The type of this Function.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Function.


        :param type: The type of this Function.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^Function$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^Function$/`")  # noqa: E501

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
        if not isinstance(other, Function):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Function):
            return True

        return self.to_dict() != other.to_dict()
