# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.8.7
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
        'name': 'str',
        'template': 'str',
        'arguments': 'DAGTaskArgument',
        'dependencies': 'list[str]',
        'loop': 'DAGTaskLoop',
        'sub_folder': 'str',
        'outputs': 'DAGTaskOutputs'
    }

    attribute_map = {
        'name': 'name',
        'template': 'template',
        'arguments': 'arguments',
        'dependencies': 'dependencies',
        'loop': 'loop',
        'sub_folder': 'sub_folder',
        'outputs': 'outputs'
    }

    def __init__(self, name=None, template=None, arguments=None, dependencies=None, loop=None, sub_folder=None, outputs=None, local_vars_configuration=None):  # noqa: E501
        """DAGTask - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._template = None
        self._arguments = None
        self._dependencies = None
        self._loop = None
        self._sub_folder = None
        self._outputs = None
        self.discriminator = None

        self.name = name
        self.template = template
        if arguments is not None:
            self.arguments = arguments
        if dependencies is not None:
            self.dependencies = dependencies
        if loop is not None:
            self.loop = loop
        if sub_folder is not None:
            self.sub_folder = sub_folder
        if outputs is not None:
            self.outputs = outputs

    @property
    def name(self):
        """Gets the name of this DAGTask.  # noqa: E501

        Name for this step. It must be unique in DAG.  # noqa: E501

        :return: The name of this DAGTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DAGTask.

        Name for this step. It must be unique in DAG.  # noqa: E501

        :param name: The name of this DAGTask.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def template(self):
        """Gets the template of this DAGTask.  # noqa: E501

        Template name.  # noqa: E501

        :return: The template of this DAGTask.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this DAGTask.

        Template name.  # noqa: E501

        :param template: The template of this DAGTask.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and template is None:  # noqa: E501
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def arguments(self):
        """Gets the arguments of this DAGTask.  # noqa: E501

        The input arguments for this task  # noqa: E501

        :return: The arguments of this DAGTask.  # noqa: E501
        :rtype: DAGTaskArgument
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this DAGTask.

        The input arguments for this task  # noqa: E501

        :param arguments: The arguments of this DAGTask.  # noqa: E501
        :type: DAGTaskArgument
        """

        self._arguments = arguments

    @property
    def dependencies(self):
        """Gets the dependencies of this DAGTask.  # noqa: E501

        Dependencies are name of other DAG steps which this depends on.  # noqa: E501

        :return: The dependencies of this DAGTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this DAGTask.

        Dependencies are name of other DAG steps which this depends on.  # noqa: E501

        :param dependencies: The dependencies of this DAGTask.  # noqa: E501
        :type: list[str]
        """

        self._dependencies = dependencies

    @property
    def loop(self):
        """Gets the loop of this DAGTask.  # noqa: E501

        List of inputs to loop over.  # noqa: E501

        :return: The loop of this DAGTask.  # noqa: E501
        :rtype: DAGTaskLoop
        """
        return self._loop

    @loop.setter
    def loop(self, loop):
        """Sets the loop of this DAGTask.

        List of inputs to loop over.  # noqa: E501

        :param loop: The loop of this DAGTask.  # noqa: E501
        :type: DAGTaskLoop
        """

        self._loop = loop

    @property
    def sub_folder(self):
        """Gets the sub_folder of this DAGTask.  # noqa: E501

        A path relative to the current folder context where artifacts should be saved. This is useful when performing a loop or invoking another workflow and wanting to save results in a specific folder.  # noqa: E501

        :return: The sub_folder of this DAGTask.  # noqa: E501
        :rtype: str
        """
        return self._sub_folder

    @sub_folder.setter
    def sub_folder(self, sub_folder):
        """Sets the sub_folder of this DAGTask.

        A path relative to the current folder context where artifacts should be saved. This is useful when performing a loop or invoking another workflow and wanting to save results in a specific folder.  # noqa: E501

        :param sub_folder: The sub_folder of this DAGTask.  # noqa: E501
        :type: str
        """

        self._sub_folder = sub_folder

    @property
    def outputs(self):
        """Gets the outputs of this DAGTask.  # noqa: E501

        The outputs of this task  # noqa: E501

        :return: The outputs of this DAGTask.  # noqa: E501
        :rtype: DAGTaskOutputs
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this DAGTask.

        The outputs of this task  # noqa: E501

        :param outputs: The outputs of this DAGTask.  # noqa: E501
        :type: DAGTaskOutputs
        """

        self._outputs = outputs

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
