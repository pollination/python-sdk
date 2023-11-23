# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.45.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class TaskPathArgument(object):
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
        '_from': 'AnyOfInputFileReferenceInputFolderReferenceInputPathReferenceTaskFileReferenceTaskFolderReferenceTaskPathReferenceValueFileReferenceValueFolderReference',
        'name': 'str',
        'sub_path': 'str',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        '_from': 'from',
        'name': 'name',
        'sub_path': 'sub_path',
        'type': 'type'
    }

    def __init__(self, annotations=None, _from=None, name=None, sub_path=None, type='TaskPathArgument', local_vars_configuration=None):  # noqa: E501
        """TaskPathArgument - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self.__from = None
        self._name = None
        self._sub_path = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        self._from = _from
        self.name = name
        if sub_path is not None:
            self.sub_path = sub_path
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this TaskPathArgument.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this TaskPathArgument.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this TaskPathArgument.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this TaskPathArgument.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def _from(self):
        """Gets the _from of this TaskPathArgument.  # noqa: E501

        A reference to a DAG input, a DAG output or another task output. You can also use the ValueReference type to hard-code an input value.  # noqa: E501

        :return: The _from of this TaskPathArgument.  # noqa: E501
        :rtype: AnyOfInputFileReferenceInputFolderReferenceInputPathReferenceTaskFileReferenceTaskFolderReferenceTaskPathReferenceValueFileReferenceValueFolderReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this TaskPathArgument.

        A reference to a DAG input, a DAG output or another task output. You can also use the ValueReference type to hard-code an input value.  # noqa: E501

        :param _from: The _from of this TaskPathArgument.  # noqa: E501
        :type _from: AnyOfInputFileReferenceInputFolderReferenceInputPathReferenceTaskFileReferenceTaskFolderReferenceTaskPathReferenceValueFileReferenceValueFolderReference
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def name(self):
        """Gets the name of this TaskPathArgument.  # noqa: E501

        Argument name. The name must match one of the input names from Task's template which can be a function or DAG.  # noqa: E501

        :return: The name of this TaskPathArgument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskPathArgument.

        Argument name. The name must match one of the input names from Task's template which can be a function or DAG.  # noqa: E501

        :param name: The name of this TaskPathArgument.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sub_path(self):
        """Gets the sub_path of this TaskPathArgument.  # noqa: E501

        A sub_path inside the path that is provided in the ``from`` field. Use sub_path to only access part of the Path that is needed instead of copying all the files and folders inside the path.  # noqa: E501

        :return: The sub_path of this TaskPathArgument.  # noqa: E501
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this TaskPathArgument.

        A sub_path inside the path that is provided in the ``from`` field. Use sub_path to only access part of the Path that is needed instead of copying all the files and folders inside the path.  # noqa: E501

        :param sub_path: The sub_path of this TaskPathArgument.  # noqa: E501
        :type sub_path: str
        """

        self._sub_path = sub_path

    @property
    def type(self):
        """Gets the type of this TaskPathArgument.  # noqa: E501


        :return: The type of this TaskPathArgument.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskPathArgument.


        :param type: The type of this TaskPathArgument.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^TaskPathArgument$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^TaskPathArgument$/`")  # noqa: E501

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
        if not isinstance(other, TaskPathArgument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskPathArgument):
            return True

        return self.to_dict() != other.to_dict()
