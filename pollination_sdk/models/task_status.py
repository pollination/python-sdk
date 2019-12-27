# coding: utf-8

"""
    pollination.cloud

    Pollination Cloud API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class TaskStatus(object):
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
        'status': 'str',
        'message': 'str',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'template_ref': 'str',
        'operator': 'Operator',
        'command': 'str',
        'inputs': 'Arguments',
        'outputs': 'Arguments',
        'boundary_id': 'str',
        'children': 'list[str]',
        'outbound_tasks': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'template_ref': 'template_ref',
        'operator': 'operator',
        'command': 'command',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'boundary_id': 'boundary_id',
        'children': 'children',
        'outbound_tasks': 'outbound_tasks'
    }

    def __init__(self, status=None, message=None, started_at=None, finished_at=None, id=None, name=None, type=None, template_ref=None, operator=None, command=None, inputs=None, outputs=None, boundary_id=None, children=None, outbound_tasks=None, local_vars_configuration=None):  # noqa: E501
        """TaskStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._message = None
        self._started_at = None
        self._finished_at = None
        self._id = None
        self._name = None
        self._type = None
        self._template_ref = None
        self._operator = None
        self._command = None
        self._inputs = None
        self._outputs = None
        self._boundary_id = None
        self._children = None
        self._outbound_tasks = None
        self.discriminator = None

        self.status = status
        if message is not None:
            self.message = message
        self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        self.id = id
        self.name = name
        self.type = type
        self.template_ref = template_ref
        if operator is not None:
            self.operator = operator
        if command is not None:
            self.command = command
        self.inputs = inputs
        self.outputs = outputs
        if boundary_id is not None:
            self.boundary_id = boundary_id
        self.children = children
        self.outbound_tasks = outbound_tasks

    @property
    def status(self):
        """Gets the status of this TaskStatus.  # noqa: E501

        The status of this task. Can be \"Running\", \"Succeeded\", \"Failed\" or \"Error\"  # noqa: E501

        :return: The status of this TaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskStatus.

        The status of this task. Can be \"Running\", \"Succeeded\", \"Failed\" or \"Error\"  # noqa: E501

        :param status: The status of this TaskStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this TaskStatus.  # noqa: E501

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :return: The message of this TaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TaskStatus.

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :param message: The message of this TaskStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def started_at(self):
        """Gets the started_at of this TaskStatus.  # noqa: E501

        The time at which the task was started  # noqa: E501

        :return: The started_at of this TaskStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this TaskStatus.

        The time at which the task was started  # noqa: E501

        :param started_at: The started_at of this TaskStatus.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this TaskStatus.  # noqa: E501

        The time at which the task was completed  # noqa: E501

        :return: The finished_at of this TaskStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this TaskStatus.

        The time at which the task was completed  # noqa: E501

        :param finished_at: The finished_at of this TaskStatus.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this TaskStatus.  # noqa: E501

        The task unique ID  # noqa: E501

        :return: The id of this TaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskStatus.

        The task unique ID  # noqa: E501

        :param id: The id of this TaskStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskStatus.  # noqa: E501

        A human readable name for the task. Usually defined by the             DAG task name but can be extended if the task is part of a loop for example.             This name is unique within the boundary of the DAG/Workflow that generated it.  # noqa: E501

        :return: The name of this TaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskStatus.

        A human readable name for the task. Usually defined by the             DAG task name but can be extended if the task is part of a loop for example.             This name is unique within the boundary of the DAG/Workflow that generated it.  # noqa: E501

        :param name: The name of this TaskStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this TaskStatus.  # noqa: E501

        The type of task this status is for. Can be \"Function\", \"DAG\", \"Workflow\" or \"Loop\"  # noqa: E501

        :return: The type of this TaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskStatus.

        The type of task this status is for. Can be \"Function\", \"DAG\", \"Workflow\" or \"Loop\"  # noqa: E501

        :param type: The type of this TaskStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def template_ref(self):
        """Gets the template_ref of this TaskStatus.  # noqa: E501

        The name of the template that spawned this task  # noqa: E501

        :return: The template_ref of this TaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._template_ref

    @template_ref.setter
    def template_ref(self, template_ref):
        """Sets the template_ref of this TaskStatus.

        The name of the template that spawned this task  # noqa: E501

        :param template_ref: The template_ref of this TaskStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and template_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `template_ref`, must not be `None`")  # noqa: E501

        self._template_ref = template_ref

    @property
    def operator(self):
        """Gets the operator of this TaskStatus.  # noqa: E501

        The operator used to run this task. Only applies to Function tasks.  # noqa: E501

        :return: The operator of this TaskStatus.  # noqa: E501
        :rtype: Operator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this TaskStatus.

        The operator used to run this task. Only applies to Function tasks.  # noqa: E501

        :param operator: The operator of this TaskStatus.  # noqa: E501
        :type: Operator
        """

        self._operator = operator

    @property
    def command(self):
        """Gets the command of this TaskStatus.  # noqa: E501

        The command used to run this task. Only applies to Function tasks.  # noqa: E501

        :return: The command of this TaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this TaskStatus.

        The command used to run this task. Only applies to Function tasks.  # noqa: E501

        :param command: The command of this TaskStatus.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def inputs(self):
        """Gets the inputs of this TaskStatus.  # noqa: E501

        The inputs used by this task  # noqa: E501

        :return: The inputs of this TaskStatus.  # noqa: E501
        :rtype: Arguments
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this TaskStatus.

        The inputs used by this task  # noqa: E501

        :param inputs: The inputs of this TaskStatus.  # noqa: E501
        :type: Arguments
        """
        if self.local_vars_configuration.client_side_validation and inputs is None:  # noqa: E501
            raise ValueError("Invalid value for `inputs`, must not be `None`")  # noqa: E501

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this TaskStatus.  # noqa: E501

        The outputs produced by this task  # noqa: E501

        :return: The outputs of this TaskStatus.  # noqa: E501
        :rtype: Arguments
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this TaskStatus.

        The outputs produced by this task  # noqa: E501

        :param outputs: The outputs of this TaskStatus.  # noqa: E501
        :type: Arguments
        """
        if self.local_vars_configuration.client_side_validation and outputs is None:  # noqa: E501
            raise ValueError("Invalid value for `outputs`, must not be `None`")  # noqa: E501

        self._outputs = outputs

    @property
    def boundary_id(self):
        """Gets the boundary_id of this TaskStatus.  # noqa: E501

        This indicates the task ID of the associated template root             task in which this task belongs to. A DAG task will have the id of the             parent DAG for example.  # noqa: E501

        :return: The boundary_id of this TaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._boundary_id

    @boundary_id.setter
    def boundary_id(self, boundary_id):
        """Sets the boundary_id of this TaskStatus.

        This indicates the task ID of the associated template root             task in which this task belongs to. A DAG task will have the id of the             parent DAG for example.  # noqa: E501

        :param boundary_id: The boundary_id of this TaskStatus.  # noqa: E501
        :type: str
        """

        self._boundary_id = boundary_id

    @property
    def children(self):
        """Gets the children of this TaskStatus.  # noqa: E501

        A list of child task IDs  # noqa: E501

        :return: The children of this TaskStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this TaskStatus.

        A list of child task IDs  # noqa: E501

        :param children: The children of this TaskStatus.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and children is None:  # noqa: E501
            raise ValueError("Invalid value for `children`, must not be `None`")  # noqa: E501

        self._children = children

    @property
    def outbound_tasks(self):
        """Gets the outbound_tasks of this TaskStatus.  # noqa: E501

        A list of the last tasks to ran in the context of this             task. In the case of a DAG or a workflow this will be the last task that has             been executed. It will remain empty for functions.  # noqa: E501

        :return: The outbound_tasks of this TaskStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._outbound_tasks

    @outbound_tasks.setter
    def outbound_tasks(self, outbound_tasks):
        """Sets the outbound_tasks of this TaskStatus.

        A list of the last tasks to ran in the context of this             task. In the case of a DAG or a workflow this will be the last task that has             been executed. It will remain empty for functions.  # noqa: E501

        :param outbound_tasks: The outbound_tasks of this TaskStatus.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and outbound_tasks is None:  # noqa: E501
            raise ValueError("Invalid value for `outbound_tasks`, must not be `None`")  # noqa: E501

        self._outbound_tasks = outbound_tasks

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
        if not isinstance(other, TaskStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskStatus):
            return True

        return self.to_dict() != other.to_dict()
