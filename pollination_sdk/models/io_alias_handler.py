# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: v0.20.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class IOAliasHandler(object):
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
        'function': 'str',
        'index': 'int',
        'language': 'str',
        'module': 'str',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'function': 'function',
        'index': 'index',
        'language': 'language',
        'module': 'module',
        'type': 'type'
    }

    def __init__(self, annotations=None, function=None, index=0, language=None, module=None, type='IOAliasHandler', local_vars_configuration=None):  # noqa: E501
        """IOAliasHandler - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._function = None
        self._index = None
        self._language = None
        self._module = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        self.function = function
        if index is not None:
            self.index = index
        self.language = language
        self.module = module
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this IOAliasHandler.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this IOAliasHandler.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this IOAliasHandler.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this IOAliasHandler.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def function(self):
        """Gets the function of this IOAliasHandler.  # noqa: E501

        Name of the function. The input value will be passed to this function as the first argument.  # noqa: E501

        :return: The function of this IOAliasHandler.  # noqa: E501
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this IOAliasHandler.

        Name of the function. The input value will be passed to this function as the first argument.  # noqa: E501

        :param function: The function of this IOAliasHandler.  # noqa: E501
        :type function: str
        """
        if self.local_vars_configuration.client_side_validation and function is None:  # noqa: E501
            raise ValueError("Invalid value for `function`, must not be `None`")  # noqa: E501

        self._function = function

    @property
    def index(self):
        """Gets the index of this IOAliasHandler.  # noqa: E501

        An integer to set the index for the order of execution. This input is only useful when there are more than one handler for the same platform and the output of one handler should be passed to another handler. This is also called chained handlers. By default all the handlers are indexed as 0 assuming they are not chained.  # noqa: E501

        :return: The index of this IOAliasHandler.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this IOAliasHandler.

        An integer to set the index for the order of execution. This input is only useful when there are more than one handler for the same platform and the output of one handler should be passed to another handler. This is also called chained handlers. By default all the handlers are indexed as 0 assuming they are not chained.  # noqa: E501

        :param index: The index of this IOAliasHandler.  # noqa: E501
        :type index: int
        """

        self._index = index

    @property
    def language(self):
        """Gets the language of this IOAliasHandler.  # noqa: E501

        Declare the language (e.g. python, csharp, etc.). This option allows the recipe to be flexible on handling different programming languages.  # noqa: E501

        :return: The language of this IOAliasHandler.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this IOAliasHandler.

        Declare the language (e.g. python, csharp, etc.). This option allows the recipe to be flexible on handling different programming languages.  # noqa: E501

        :param language: The language of this IOAliasHandler.  # noqa: E501
        :type language: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def module(self):
        """Gets the module of this IOAliasHandler.  # noqa: E501

        Target module or namespace to load the alias function.  # noqa: E501

        :return: The module of this IOAliasHandler.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this IOAliasHandler.

        Target module or namespace to load the alias function.  # noqa: E501

        :param module: The module of this IOAliasHandler.  # noqa: E501
        :type module: str
        """
        if self.local_vars_configuration.client_side_validation and module is None:  # noqa: E501
            raise ValueError("Invalid value for `module`, must not be `None`")  # noqa: E501

        self._module = module

    @property
    def type(self):
        """Gets the type of this IOAliasHandler.  # noqa: E501


        :return: The type of this IOAliasHandler.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IOAliasHandler.


        :param type: The type of this IOAliasHandler.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^IOAliasHandler$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^IOAliasHandler$/`")  # noqa: E501

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
        if not isinstance(other, IOAliasHandler):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IOAliasHandler):
            return True

        return self.to_dict() != other.to_dict()
