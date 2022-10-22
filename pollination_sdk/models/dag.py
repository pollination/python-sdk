# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.31.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class DAG(object):
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
        'fail_fast': 'bool',
        'inputs': 'list[AnyOfDAGGenericInputDAGStringInputDAGIntegerInputDAGNumberInputDAGBooleanInputDAGFolderInputDAGFileInputDAGPathInputDAGArrayInputDAGJSONObjectInput]',
        'name': 'str',
        'outputs': 'list[AnyOfDAGGenericOutputDAGStringOutputDAGIntegerOutputDAGNumberOutputDAGBooleanOutputDAGFolderOutputDAGFileOutputDAGPathOutputDAGArrayOutputDAGJSONObjectOutput]',
        'tasks': 'list[DAGTask]',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'fail_fast': 'fail_fast',
        'inputs': 'inputs',
        'name': 'name',
        'outputs': 'outputs',
        'tasks': 'tasks',
        'type': 'type'
    }

    def __init__(self, annotations=None, fail_fast=True, inputs=None, name=None, outputs=None, tasks=None, type='DAG', local_vars_configuration=None):  # noqa: E501
        """DAG - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._fail_fast = None
        self._inputs = None
        self._name = None
        self._outputs = None
        self._tasks = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if fail_fast is not None:
            self.fail_fast = fail_fast
        if inputs is not None:
            self.inputs = inputs
        self.name = name
        if outputs is not None:
            self.outputs = outputs
        self.tasks = tasks
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this DAG.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this DAG.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this DAG.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this DAG.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def fail_fast(self):
        """Gets the fail_fast of this DAG.  # noqa: E501

        Stop scheduling new steps, as soon as it detects that one of the DAG nodes is failed. Default is True.  # noqa: E501

        :return: The fail_fast of this DAG.  # noqa: E501
        :rtype: bool
        """
        return self._fail_fast

    @fail_fast.setter
    def fail_fast(self, fail_fast):
        """Sets the fail_fast of this DAG.

        Stop scheduling new steps, as soon as it detects that one of the DAG nodes is failed. Default is True.  # noqa: E501

        :param fail_fast: The fail_fast of this DAG.  # noqa: E501
        :type fail_fast: bool
        """

        self._fail_fast = fail_fast

    @property
    def inputs(self):
        """Gets the inputs of this DAG.  # noqa: E501

        Inputs for the DAG.  # noqa: E501

        :return: The inputs of this DAG.  # noqa: E501
        :rtype: list[AnyOfDAGGenericInputDAGStringInputDAGIntegerInputDAGNumberInputDAGBooleanInputDAGFolderInputDAGFileInputDAGPathInputDAGArrayInputDAGJSONObjectInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this DAG.

        Inputs for the DAG.  # noqa: E501

        :param inputs: The inputs of this DAG.  # noqa: E501
        :type inputs: list[AnyOfDAGGenericInputDAGStringInputDAGIntegerInputDAGNumberInputDAGBooleanInputDAGFolderInputDAGFileInputDAGPathInputDAGArrayInputDAGJSONObjectInput]
        """

        self._inputs = inputs

    @property
    def name(self):
        """Gets the name of this DAG.  # noqa: E501

        A unique name for this dag.  # noqa: E501

        :return: The name of this DAG.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DAG.

        A unique name for this dag.  # noqa: E501

        :param name: The name of this DAG.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def outputs(self):
        """Gets the outputs of this DAG.  # noqa: E501

        Outputs of the DAG that can be used by other DAGs.  # noqa: E501

        :return: The outputs of this DAG.  # noqa: E501
        :rtype: list[AnyOfDAGGenericOutputDAGStringOutputDAGIntegerOutputDAGNumberOutputDAGBooleanOutputDAGFolderOutputDAGFileOutputDAGPathOutputDAGArrayOutputDAGJSONObjectOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this DAG.

        Outputs of the DAG that can be used by other DAGs.  # noqa: E501

        :param outputs: The outputs of this DAG.  # noqa: E501
        :type outputs: list[AnyOfDAGGenericOutputDAGStringOutputDAGIntegerOutputDAGNumberOutputDAGBooleanOutputDAGFolderOutputDAGFileOutputDAGPathOutputDAGArrayOutputDAGJSONObjectOutput]
        """

        self._outputs = outputs

    @property
    def tasks(self):
        """Gets the tasks of this DAG.  # noqa: E501

        Tasks are a list of DAG steps  # noqa: E501

        :return: The tasks of this DAG.  # noqa: E501
        :rtype: list[DAGTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this DAG.

        Tasks are a list of DAG steps  # noqa: E501

        :param tasks: The tasks of this DAG.  # noqa: E501
        :type tasks: list[DAGTask]
        """
        if self.local_vars_configuration.client_side_validation and tasks is None:  # noqa: E501
            raise ValueError("Invalid value for `tasks`, must not be `None`")  # noqa: E501

        self._tasks = tasks

    @property
    def type(self):
        """Gets the type of this DAG.  # noqa: E501


        :return: The type of this DAG.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DAG.


        :param type: The type of this DAG.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^DAG$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^DAG$/`")  # noqa: E501

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
        if not isinstance(other, DAG):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DAG):
            return True

        return self.to_dict() != other.to_dict()
