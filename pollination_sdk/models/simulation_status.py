# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.2.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class SimulationStatus(object):
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
        'tasks': 'dict(str, TaskStatus)',
        'owner_id': 'str',
        'project_id': 'str',
        'workflow': 'Workflow',
        'inputs': 'Arguments'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'id': 'id',
        'tasks': 'tasks',
        'owner_id': 'owner_id',
        'project_id': 'project_id',
        'workflow': 'workflow',
        'inputs': 'inputs'
    }

    def __init__(self, status=None, message=None, started_at=None, finished_at=None, id=None, tasks=None, owner_id=None, project_id=None, workflow=None, inputs=None, local_vars_configuration=None):  # noqa: E501
        """SimulationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._message = None
        self._started_at = None
        self._finished_at = None
        self._id = None
        self._tasks = None
        self._owner_id = None
        self._project_id = None
        self._workflow = None
        self._inputs = None
        self.discriminator = None

        self.status = status
        if message is not None:
            self.message = message
        self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        self.id = id
        if tasks is not None:
            self.tasks = tasks
        self.owner_id = owner_id
        self.project_id = project_id
        if workflow is not None:
            self.workflow = workflow
        if inputs is not None:
            self.inputs = inputs

    @property
    def status(self):
        """Gets the status of this SimulationStatus.  # noqa: E501

        The status of this task. Can be \"Running\", \"Succeeded\", \"Failed\" or \"Error\"  # noqa: E501

        :return: The status of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SimulationStatus.

        The status of this task. Can be \"Running\", \"Succeeded\", \"Failed\" or \"Error\"  # noqa: E501

        :param status: The status of this SimulationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this SimulationStatus.  # noqa: E501

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :return: The message of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SimulationStatus.

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :param message: The message of this SimulationStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def started_at(self):
        """Gets the started_at of this SimulationStatus.  # noqa: E501

        The time at which the task was started  # noqa: E501

        :return: The started_at of this SimulationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this SimulationStatus.

        The time at which the task was started  # noqa: E501

        :param started_at: The started_at of this SimulationStatus.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this SimulationStatus.  # noqa: E501

        The time at which the task was completed  # noqa: E501

        :return: The finished_at of this SimulationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this SimulationStatus.

        The time at which the task was completed  # noqa: E501

        :param finished_at: The finished_at of this SimulationStatus.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this SimulationStatus.  # noqa: E501

        The ID of the individual workflow run.  # noqa: E501

        :return: The id of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimulationStatus.

        The ID of the individual workflow run.  # noqa: E501

        :param id: The id of this SimulationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def tasks(self):
        """Gets the tasks of this SimulationStatus.  # noqa: E501


        :return: The tasks of this SimulationStatus.  # noqa: E501
        :rtype: dict(str, TaskStatus)
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this SimulationStatus.


        :param tasks: The tasks of this SimulationStatus.  # noqa: E501
        :type: dict(str, TaskStatus)
        """

        self._tasks = tasks

    @property
    def owner_id(self):
        """Gets the owner_id of this SimulationStatus.  # noqa: E501

        ID of the account the simulation is running for.  # noqa: E501

        :return: The owner_id of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this SimulationStatus.

        ID of the account the simulation is running for.  # noqa: E501

        :param owner_id: The owner_id of this SimulationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner_id is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def project_id(self):
        """Gets the project_id of this SimulationStatus.  # noqa: E501

        ID of the project the simulation belongs to  # noqa: E501

        :return: The project_id of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SimulationStatus.

        ID of the project the simulation belongs to  # noqa: E501

        :param project_id: The project_id of this SimulationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and project_id is None:  # noqa: E501
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def workflow(self):
        """Gets the workflow of this SimulationStatus.  # noqa: E501

        A queenbee workflow payload  # noqa: E501

        :return: The workflow of this SimulationStatus.  # noqa: E501
        :rtype: Workflow
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this SimulationStatus.

        A queenbee workflow payload  # noqa: E501

        :param workflow: The workflow of this SimulationStatus.  # noqa: E501
        :type: Workflow
        """

        self._workflow = workflow

    @property
    def inputs(self):
        """Gets the inputs of this SimulationStatus.  # noqa: E501

        Simulation inputs  # noqa: E501

        :return: The inputs of this SimulationStatus.  # noqa: E501
        :rtype: Arguments
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this SimulationStatus.

        Simulation inputs  # noqa: E501

        :param inputs: The inputs of this SimulationStatus.  # noqa: E501
        :type: Arguments
        """

        self._inputs = inputs

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
        if not isinstance(other, SimulationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationStatus):
            return True

        return self.to_dict() != other.to_dict()