# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.25.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class StepStatus(object):
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
        'boundary_id': 'str',
        'children_ids': 'list[str]',
        'command': 'str',
        'finished_at': 'datetime',
        'id': 'str',
        'inputs': 'list[AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput]',
        'message': 'str',
        'name': 'str',
        'outbound_steps': 'list[str]',
        'outputs': 'list[AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput]',
        'source': 'str',
        'started_at': 'datetime',
        'status': 'StepStatusEnum',
        'status_type': 'StatusType',
        'template_ref': 'str',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'boundary_id': 'boundary_id',
        'children_ids': 'children_ids',
        'command': 'command',
        'finished_at': 'finished_at',
        'id': 'id',
        'inputs': 'inputs',
        'message': 'message',
        'name': 'name',
        'outbound_steps': 'outbound_steps',
        'outputs': 'outputs',
        'source': 'source',
        'started_at': 'started_at',
        'status': 'status',
        'status_type': 'status_type',
        'template_ref': 'template_ref',
        'type': 'type'
    }

    def __init__(self, annotations=None, boundary_id=None, children_ids=None, command=None, finished_at=None, id=None, inputs=None, message=None, name=None, outbound_steps=None, outputs=None, source=None, started_at=None, status=None, status_type=None, template_ref=None, type='StepStatus', local_vars_configuration=None):  # noqa: E501
        """StepStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._boundary_id = None
        self._children_ids = None
        self._command = None
        self._finished_at = None
        self._id = None
        self._inputs = None
        self._message = None
        self._name = None
        self._outbound_steps = None
        self._outputs = None
        self._source = None
        self._started_at = None
        self._status = None
        self._status_type = None
        self._template_ref = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if boundary_id is not None:
            self.boundary_id = boundary_id
        self.children_ids = children_ids
        if command is not None:
            self.command = command
        if finished_at is not None:
            self.finished_at = finished_at
        self.id = id
        self.inputs = inputs
        if message is not None:
            self.message = message
        self.name = name
        self.outbound_steps = outbound_steps
        self.outputs = outputs
        if source is not None:
            self.source = source
        self.started_at = started_at
        if status is not None:
            self.status = status
        self.status_type = status_type
        self.template_ref = template_ref
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this StepStatus.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this StepStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this StepStatus.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this StepStatus.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def boundary_id(self):
        """Gets the boundary_id of this StepStatus.  # noqa: E501

        This indicates the step ID of the associated template root             step in which this step belongs to. A DAG step will have the id of the             parent DAG for example.  # noqa: E501

        :return: The boundary_id of this StepStatus.  # noqa: E501
        :rtype: str
        """
        return self._boundary_id

    @boundary_id.setter
    def boundary_id(self, boundary_id):
        """Sets the boundary_id of this StepStatus.

        This indicates the step ID of the associated template root             step in which this step belongs to. A DAG step will have the id of the             parent DAG for example.  # noqa: E501

        :param boundary_id: The boundary_id of this StepStatus.  # noqa: E501
        :type boundary_id: str
        """

        self._boundary_id = boundary_id

    @property
    def children_ids(self):
        """Gets the children_ids of this StepStatus.  # noqa: E501

        A list of child step IDs  # noqa: E501

        :return: The children_ids of this StepStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._children_ids

    @children_ids.setter
    def children_ids(self, children_ids):
        """Sets the children_ids of this StepStatus.

        A list of child step IDs  # noqa: E501

        :param children_ids: The children_ids of this StepStatus.  # noqa: E501
        :type children_ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and children_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `children_ids`, must not be `None`")  # noqa: E501

        self._children_ids = children_ids

    @property
    def command(self):
        """Gets the command of this StepStatus.  # noqa: E501

        The command used to run this step. Only applies to Function steps.  # noqa: E501

        :return: The command of this StepStatus.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this StepStatus.

        The command used to run this step. Only applies to Function steps.  # noqa: E501

        :param command: The command of this StepStatus.  # noqa: E501
        :type command: str
        """

        self._command = command

    @property
    def finished_at(self):
        """Gets the finished_at of this StepStatus.  # noqa: E501

        The time at which the task was completed  # noqa: E501

        :return: The finished_at of this StepStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this StepStatus.

        The time at which the task was completed  # noqa: E501

        :param finished_at: The finished_at of this StepStatus.  # noqa: E501
        :type finished_at: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this StepStatus.  # noqa: E501

        The step unique ID  # noqa: E501

        :return: The id of this StepStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StepStatus.

        The step unique ID  # noqa: E501

        :param id: The id of this StepStatus.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def inputs(self):
        """Gets the inputs of this StepStatus.  # noqa: E501

        The inputs used by this step.  # noqa: E501

        :return: The inputs of this StepStatus.  # noqa: E501
        :rtype: list[AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this StepStatus.

        The inputs used by this step.  # noqa: E501

        :param inputs: The inputs of this StepStatus.  # noqa: E501
        :type inputs: list[AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput]
        """
        if self.local_vars_configuration.client_side_validation and inputs is None:  # noqa: E501
            raise ValueError("Invalid value for `inputs`, must not be `None`")  # noqa: E501

        self._inputs = inputs

    @property
    def message(self):
        """Gets the message of this StepStatus.  # noqa: E501

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :return: The message of this StepStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this StepStatus.

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :param message: The message of this StepStatus.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this StepStatus.  # noqa: E501

        A human readable name for the step. Usually defined by the DAG task name but can be extended if the step is part of a loop for example. This name is unique within the boundary of the DAG/Job that generated it.  # noqa: E501

        :return: The name of this StepStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StepStatus.

        A human readable name for the step. Usually defined by the DAG task name but can be extended if the step is part of a loop for example. This name is unique within the boundary of the DAG/Job that generated it.  # noqa: E501

        :param name: The name of this StepStatus.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def outbound_steps(self):
        """Gets the outbound_steps of this StepStatus.  # noqa: E501

        A list of the last step to ran in the context of this step. In the case of a DAG or a job this will be the last step that has been executed. It will remain empty for functions.  # noqa: E501

        :return: The outbound_steps of this StepStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._outbound_steps

    @outbound_steps.setter
    def outbound_steps(self, outbound_steps):
        """Sets the outbound_steps of this StepStatus.

        A list of the last step to ran in the context of this step. In the case of a DAG or a job this will be the last step that has been executed. It will remain empty for functions.  # noqa: E501

        :param outbound_steps: The outbound_steps of this StepStatus.  # noqa: E501
        :type outbound_steps: list[str]
        """
        if self.local_vars_configuration.client_side_validation and outbound_steps is None:  # noqa: E501
            raise ValueError("Invalid value for `outbound_steps`, must not be `None`")  # noqa: E501

        self._outbound_steps = outbound_steps

    @property
    def outputs(self):
        """Gets the outputs of this StepStatus.  # noqa: E501

        The outputs produced by this step.  # noqa: E501

        :return: The outputs of this StepStatus.  # noqa: E501
        :rtype: list[AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this StepStatus.

        The outputs produced by this step.  # noqa: E501

        :param outputs: The outputs of this StepStatus.  # noqa: E501
        :type outputs: list[AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput]
        """
        if self.local_vars_configuration.client_side_validation and outputs is None:  # noqa: E501
            raise ValueError("Invalid value for `outputs`, must not be `None`")  # noqa: E501

        self._outputs = outputs

    @property
    def source(self):
        """Gets the source of this StepStatus.  # noqa: E501

        Source url for the status object. It can be a recipe or a function.  # noqa: E501

        :return: The source of this StepStatus.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this StepStatus.

        Source url for the status object. It can be a recipe or a function.  # noqa: E501

        :param source: The source of this StepStatus.  # noqa: E501
        :type source: str
        """

        self._source = source

    @property
    def started_at(self):
        """Gets the started_at of this StepStatus.  # noqa: E501

        The time at which the task was started  # noqa: E501

        :return: The started_at of this StepStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this StepStatus.

        The time at which the task was started  # noqa: E501

        :param started_at: The started_at of this StepStatus.  # noqa: E501
        :type started_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this StepStatus.  # noqa: E501

        The status of this step.  # noqa: E501

        :return: The status of this StepStatus.  # noqa: E501
        :rtype: StepStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StepStatus.

        The status of this step.  # noqa: E501

        :param status: The status of this StepStatus.  # noqa: E501
        :type status: StepStatusEnum
        """

        self._status = status

    @property
    def status_type(self):
        """Gets the status_type of this StepStatus.  # noqa: E501

        The type of step this status is for. Can be \"Function\", \"DAG\" or \"Loop\"  # noqa: E501

        :return: The status_type of this StepStatus.  # noqa: E501
        :rtype: StatusType
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        """Sets the status_type of this StepStatus.

        The type of step this status is for. Can be \"Function\", \"DAG\" or \"Loop\"  # noqa: E501

        :param status_type: The status_type of this StepStatus.  # noqa: E501
        :type status_type: StatusType
        """
        if self.local_vars_configuration.client_side_validation and status_type is None:  # noqa: E501
            raise ValueError("Invalid value for `status_type`, must not be `None`")  # noqa: E501

        self._status_type = status_type

    @property
    def template_ref(self):
        """Gets the template_ref of this StepStatus.  # noqa: E501

        The name of the template that spawned this step  # noqa: E501

        :return: The template_ref of this StepStatus.  # noqa: E501
        :rtype: str
        """
        return self._template_ref

    @template_ref.setter
    def template_ref(self, template_ref):
        """Sets the template_ref of this StepStatus.

        The name of the template that spawned this step  # noqa: E501

        :param template_ref: The template_ref of this StepStatus.  # noqa: E501
        :type template_ref: str
        """
        if self.local_vars_configuration.client_side_validation and template_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `template_ref`, must not be `None`")  # noqa: E501

        self._template_ref = template_ref

    @property
    def type(self):
        """Gets the type of this StepStatus.  # noqa: E501


        :return: The type of this StepStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StepStatus.


        :param type: The type of this StepStatus.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^StepStatus$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^StepStatus$/`")  # noqa: E501

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
        if not isinstance(other, StepStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StepStatus):
            return True

        return self.to_dict() != other.to_dict()
