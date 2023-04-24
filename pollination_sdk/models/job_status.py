# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.38.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class JobStatus(object):
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
        'api_version': 'str',
        'finished_at': 'datetime',
        'id': 'str',
        'message': 'str',
        'runs_cancelled': 'int',
        'runs_completed': 'int',
        'runs_failed': 'int',
        'runs_pending': 'int',
        'runs_running': 'int',
        'source': 'str',
        'started_at': 'datetime',
        'status': 'JobStatusEnum',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'api_version': 'api_version',
        'finished_at': 'finished_at',
        'id': 'id',
        'message': 'message',
        'runs_cancelled': 'runs_cancelled',
        'runs_completed': 'runs_completed',
        'runs_failed': 'runs_failed',
        'runs_pending': 'runs_pending',
        'runs_running': 'runs_running',
        'source': 'source',
        'started_at': 'started_at',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, annotations=None, api_version='v1beta1', finished_at=None, id=None, message=None, runs_cancelled=0, runs_completed=0, runs_failed=0, runs_pending=0, runs_running=0, source=None, started_at=None, status=None, type='JobStatus', local_vars_configuration=None):  # noqa: E501
        """JobStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._api_version = None
        self._finished_at = None
        self._id = None
        self._message = None
        self._runs_cancelled = None
        self._runs_completed = None
        self._runs_failed = None
        self._runs_pending = None
        self._runs_running = None
        self._source = None
        self._started_at = None
        self._status = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if api_version is not None:
            self.api_version = api_version
        if finished_at is not None:
            self.finished_at = finished_at
        self.id = id
        if message is not None:
            self.message = message
        if runs_cancelled is not None:
            self.runs_cancelled = runs_cancelled
        if runs_completed is not None:
            self.runs_completed = runs_completed
        if runs_failed is not None:
            self.runs_failed = runs_failed
        if runs_pending is not None:
            self.runs_pending = runs_pending
        if runs_running is not None:
            self.runs_running = runs_running
        if source is not None:
            self.source = source
        self.started_at = started_at
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this JobStatus.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this JobStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this JobStatus.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this JobStatus.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def api_version(self):
        """Gets the api_version of this JobStatus.  # noqa: E501


        :return: The api_version of this JobStatus.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this JobStatus.


        :param api_version: The api_version of this JobStatus.  # noqa: E501
        :type api_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_version is not None and not re.search(r'^v1beta1$', api_version)):  # noqa: E501
            raise ValueError(r"Invalid value for `api_version`, must be a follow pattern or equal to `/^v1beta1$/`")  # noqa: E501

        self._api_version = api_version

    @property
    def finished_at(self):
        """Gets the finished_at of this JobStatus.  # noqa: E501

        The time at which the task was completed  # noqa: E501

        :return: The finished_at of this JobStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this JobStatus.

        The time at which the task was completed  # noqa: E501

        :param finished_at: The finished_at of this JobStatus.  # noqa: E501
        :type finished_at: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this JobStatus.  # noqa: E501

        The ID of the individual job.  # noqa: E501

        :return: The id of this JobStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobStatus.

        The ID of the individual job.  # noqa: E501

        :param id: The id of this JobStatus.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def message(self):
        """Gets the message of this JobStatus.  # noqa: E501

        Any message produced by the job. Usually error/debugging hints.  # noqa: E501

        :return: The message of this JobStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobStatus.

        Any message produced by the job. Usually error/debugging hints.  # noqa: E501

        :param message: The message of this JobStatus.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def runs_cancelled(self):
        """Gets the runs_cancelled of this JobStatus.  # noqa: E501

        The count of runs that have been cancelled  # noqa: E501

        :return: The runs_cancelled of this JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._runs_cancelled

    @runs_cancelled.setter
    def runs_cancelled(self, runs_cancelled):
        """Sets the runs_cancelled of this JobStatus.

        The count of runs that have been cancelled  # noqa: E501

        :param runs_cancelled: The runs_cancelled of this JobStatus.  # noqa: E501
        :type runs_cancelled: int
        """

        self._runs_cancelled = runs_cancelled

    @property
    def runs_completed(self):
        """Gets the runs_completed of this JobStatus.  # noqa: E501

        The count of runs that have completed  # noqa: E501

        :return: The runs_completed of this JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._runs_completed

    @runs_completed.setter
    def runs_completed(self, runs_completed):
        """Sets the runs_completed of this JobStatus.

        The count of runs that have completed  # noqa: E501

        :param runs_completed: The runs_completed of this JobStatus.  # noqa: E501
        :type runs_completed: int
        """

        self._runs_completed = runs_completed

    @property
    def runs_failed(self):
        """Gets the runs_failed of this JobStatus.  # noqa: E501

        The count of runs that have failed  # noqa: E501

        :return: The runs_failed of this JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._runs_failed

    @runs_failed.setter
    def runs_failed(self, runs_failed):
        """Sets the runs_failed of this JobStatus.

        The count of runs that have failed  # noqa: E501

        :param runs_failed: The runs_failed of this JobStatus.  # noqa: E501
        :type runs_failed: int
        """

        self._runs_failed = runs_failed

    @property
    def runs_pending(self):
        """Gets the runs_pending of this JobStatus.  # noqa: E501

        The count of runs that are pending  # noqa: E501

        :return: The runs_pending of this JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._runs_pending

    @runs_pending.setter
    def runs_pending(self, runs_pending):
        """Sets the runs_pending of this JobStatus.

        The count of runs that are pending  # noqa: E501

        :param runs_pending: The runs_pending of this JobStatus.  # noqa: E501
        :type runs_pending: int
        """

        self._runs_pending = runs_pending

    @property
    def runs_running(self):
        """Gets the runs_running of this JobStatus.  # noqa: E501

        The count of runs that are running  # noqa: E501

        :return: The runs_running of this JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._runs_running

    @runs_running.setter
    def runs_running(self, runs_running):
        """Sets the runs_running of this JobStatus.

        The count of runs that are running  # noqa: E501

        :param runs_running: The runs_running of this JobStatus.  # noqa: E501
        :type runs_running: int
        """

        self._runs_running = runs_running

    @property
    def source(self):
        """Gets the source of this JobStatus.  # noqa: E501

        Source url for the status object. It can be a recipe or a function.  # noqa: E501

        :return: The source of this JobStatus.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this JobStatus.

        Source url for the status object. It can be a recipe or a function.  # noqa: E501

        :param source: The source of this JobStatus.  # noqa: E501
        :type source: str
        """

        self._source = source

    @property
    def started_at(self):
        """Gets the started_at of this JobStatus.  # noqa: E501

        The time at which the job was started  # noqa: E501

        :return: The started_at of this JobStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this JobStatus.

        The time at which the job was started  # noqa: E501

        :param started_at: The started_at of this JobStatus.  # noqa: E501
        :type started_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this JobStatus.  # noqa: E501

        The status of this job.  # noqa: E501

        :return: The status of this JobStatus.  # noqa: E501
        :rtype: JobStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobStatus.

        The status of this job.  # noqa: E501

        :param status: The status of this JobStatus.  # noqa: E501
        :type status: JobStatusEnum
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this JobStatus.  # noqa: E501


        :return: The type of this JobStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobStatus.


        :param type: The type of this JobStatus.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^JobStatus$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^JobStatus$/`")  # noqa: E501

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
        if not isinstance(other, JobStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobStatus):
            return True

        return self.to_dict() != other.to_dict()
