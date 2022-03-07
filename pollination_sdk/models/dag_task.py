# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.27.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class DAGTask(object):
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
        'arguments': 'list[AnyOfTaskArgumentTaskPathArgument]',
        'loop': 'DAGTaskLoop',
        'name': 'str',
        'needs': 'list[str]',
        'returns': 'list[AnyOfTaskReturnTaskPathReturn]',
        'sub_folder': 'str',
        'template': 'str',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'arguments': 'arguments',
        'loop': 'loop',
        'name': 'name',
        'needs': 'needs',
        'returns': 'returns',
        'sub_folder': 'sub_folder',
        'template': 'template',
        'type': 'type'
    }

    def __init__(self, annotations=None, arguments=None, loop=None, name=None, needs=None, returns=None, sub_folder=None, template=None, type='DAGTask', local_vars_configuration=None):  # noqa: E501
        """DAGTask - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._arguments = None
        self._loop = None
        self._name = None
        self._needs = None
        self._returns = None
        self._sub_folder = None
        self._template = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if arguments is not None:
            self.arguments = arguments
        if loop is not None:
            self.loop = loop
        self.name = name
        if needs is not None:
            self.needs = needs
        if returns is not None:
            self.returns = returns
        if sub_folder is not None:
            self.sub_folder = sub_folder
        self.template = template
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this DAGTask.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this DAGTask.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this DAGTask.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this DAGTask.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def arguments(self):
        """Gets the arguments of this DAGTask.  # noqa: E501

        The input arguments for this task.  # noqa: E501

        :return: The arguments of this DAGTask.  # noqa: E501
        :rtype: list[AnyOfTaskArgumentTaskPathArgument]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this DAGTask.

        The input arguments for this task.  # noqa: E501

        :param arguments: The arguments of this DAGTask.  # noqa: E501
        :type arguments: list[AnyOfTaskArgumentTaskPathArgument]
        """

        self._arguments = arguments

    @property
    def loop(self):
        """Gets the loop of this DAGTask.  # noqa: E501

        Loop configuration for this task.  # noqa: E501

        :return: The loop of this DAGTask.  # noqa: E501
        :rtype: DAGTaskLoop
        """
        return self._loop

    @loop.setter
    def loop(self, loop):
        """Sets the loop of this DAGTask.

        Loop configuration for this task.  # noqa: E501

        :param loop: The loop of this DAGTask.  # noqa: E501
        :type loop: DAGTaskLoop
        """

        self._loop = loop

    @property
    def name(self):
        """Gets the name of this DAGTask.  # noqa: E501

        Name for this task. It must be unique in a DAG.  # noqa: E501

        :return: The name of this DAGTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DAGTask.

        Name for this task. It must be unique in a DAG.  # noqa: E501

        :param name: The name of this DAGTask.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def needs(self):
        """Gets the needs of this DAGTask.  # noqa: E501

        List of DAG tasks that this task depends on and needs to be executed before this task.  # noqa: E501

        :return: The needs of this DAGTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._needs

    @needs.setter
    def needs(self, needs):
        """Sets the needs of this DAGTask.

        List of DAG tasks that this task depends on and needs to be executed before this task.  # noqa: E501

        :param needs: The needs of this DAGTask.  # noqa: E501
        :type needs: list[str]
        """

        self._needs = needs

    @property
    def returns(self):
        """Gets the returns of this DAGTask.  # noqa: E501

        List of task returns.  # noqa: E501

        :return: The returns of this DAGTask.  # noqa: E501
        :rtype: list[AnyOfTaskReturnTaskPathReturn]
        """
        return self._returns

    @returns.setter
    def returns(self, returns):
        """Sets the returns of this DAGTask.

        List of task returns.  # noqa: E501

        :param returns: The returns of this DAGTask.  # noqa: E501
        :type returns: list[AnyOfTaskReturnTaskPathReturn]
        """

        self._returns = returns

    @property
    def sub_folder(self):
        """Gets the sub_folder of this DAGTask.  # noqa: E501

        A path relative to the current folder context where artifacts should be saved. This is useful when performing a loop or invoking another workflow and wanting to save results in a specific sub_folder.  # noqa: E501

        :return: The sub_folder of this DAGTask.  # noqa: E501
        :rtype: str
        """
        return self._sub_folder

    @sub_folder.setter
    def sub_folder(self, sub_folder):
        """Sets the sub_folder of this DAGTask.

        A path relative to the current folder context where artifacts should be saved. This is useful when performing a loop or invoking another workflow and wanting to save results in a specific sub_folder.  # noqa: E501

        :param sub_folder: The sub_folder of this DAGTask.  # noqa: E501
        :type sub_folder: str
        """

        self._sub_folder = sub_folder

    @property
    def template(self):
        """Gets the template of this DAGTask.  # noqa: E501

        Template name. A template is a Function or a DAG. This template must be available in the dependencies.  # noqa: E501

        :return: The template of this DAGTask.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this DAGTask.

        Template name. A template is a Function or a DAG. This template must be available in the dependencies.  # noqa: E501

        :param template: The template of this DAGTask.  # noqa: E501
        :type template: str
        """
        if self.local_vars_configuration.client_side_validation and template is None:  # noqa: E501
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def type(self):
        """Gets the type of this DAGTask.  # noqa: E501


        :return: The type of this DAGTask.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DAGTask.


        :param type: The type of this DAGTask.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^DAGTask$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^DAGTask$/`")  # noqa: E501

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
        if not isinstance(other, DAGTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DAGTask):
            return True

        return self.to_dict() != other.to_dict()
