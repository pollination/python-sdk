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


class WorkflowStatus(object):
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
        'entrypoint': 'str',
        'tasks': 'dict(str, TaskStatus)'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'id': 'id',
        'entrypoint': 'entrypoint',
        'tasks': 'tasks'
    }

    def __init__(self, status=None, message=None, started_at=None, finished_at=None, id=None, entrypoint=None, tasks=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._message = None
        self._started_at = None
        self._finished_at = None
        self._id = None
        self._entrypoint = None
        self._tasks = None
        self.discriminator = None

        self.status = status
        if message is not None:
            self.message = message
        self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        self.id = id
        if entrypoint is not None:
            self.entrypoint = entrypoint
        if tasks is not None:
            self.tasks = tasks

    @property
    def status(self):
        """Gets the status of this WorkflowStatus.  # noqa: E501

        The status of this task. Can be \"Running\", \"Succeeded\", \"Failed\" or \"Error\"  # noqa: E501

        :return: The status of this WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkflowStatus.

        The status of this task. Can be \"Running\", \"Succeeded\", \"Failed\" or \"Error\"  # noqa: E501

        :param status: The status of this WorkflowStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this WorkflowStatus.  # noqa: E501

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :return: The message of this WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this WorkflowStatus.

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :param message: The message of this WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def started_at(self):
        """Gets the started_at of this WorkflowStatus.  # noqa: E501

        The time at which the task was started  # noqa: E501

        :return: The started_at of this WorkflowStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this WorkflowStatus.

        The time at which the task was started  # noqa: E501

        :param started_at: The started_at of this WorkflowStatus.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this WorkflowStatus.  # noqa: E501

        The time at which the task was completed  # noqa: E501

        :return: The finished_at of this WorkflowStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this WorkflowStatus.

        The time at which the task was completed  # noqa: E501

        :param finished_at: The finished_at of this WorkflowStatus.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this WorkflowStatus.  # noqa: E501

        The ID of the individual workflow run.  # noqa: E501

        :return: The id of this WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkflowStatus.

        The ID of the individual workflow run.  # noqa: E501

        :param id: The id of this WorkflowStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def entrypoint(self):
        """Gets the entrypoint of this WorkflowStatus.  # noqa: E501

        The ID of the first task in the workflow  # noqa: E501

        :return: The entrypoint of this WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this WorkflowStatus.

        The ID of the first task in the workflow  # noqa: E501

        :param entrypoint: The entrypoint of this WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._entrypoint = entrypoint

    @property
    def tasks(self):
        """Gets the tasks of this WorkflowStatus.  # noqa: E501


        :return: The tasks of this WorkflowStatus.  # noqa: E501
        :rtype: dict(str, TaskStatus)
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this WorkflowStatus.


        :param tasks: The tasks of this WorkflowStatus.  # noqa: E501
        :type: dict(str, TaskStatus)
        """

        self._tasks = tasks

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
        if not isinstance(other, WorkflowStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowStatus):
            return True

        return self.to_dict() != other.to_dict()
