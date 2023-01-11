# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.36.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class RunStatus(object):
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
        'entrypoint': 'str',
        'finished_at': 'datetime',
        'id': 'str',
        'inputs': 'list[AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput]',
        'job_id': 'str',
        'message': 'str',
        'outputs': 'list[AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput]',
        'source': 'str',
        'started_at': 'datetime',
        'status': 'RunStatusEnum',
        'steps': 'dict(str, StepStatus)',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'api_version': 'api_version',
        'entrypoint': 'entrypoint',
        'finished_at': 'finished_at',
        'id': 'id',
        'inputs': 'inputs',
        'job_id': 'job_id',
        'message': 'message',
        'outputs': 'outputs',
        'source': 'source',
        'started_at': 'started_at',
        'status': 'status',
        'steps': 'steps',
        'type': 'type'
    }

    def __init__(self, annotations=None, api_version='v1beta1', entrypoint=None, finished_at=None, id=None, inputs=None, job_id=None, message=None, outputs=None, source=None, started_at=None, status=None, steps=None, type='RunStatus', local_vars_configuration=None):  # noqa: E501
        """RunStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._api_version = None
        self._entrypoint = None
        self._finished_at = None
        self._id = None
        self._inputs = None
        self._job_id = None
        self._message = None
        self._outputs = None
        self._source = None
        self._started_at = None
        self._status = None
        self._steps = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if api_version is not None:
            self.api_version = api_version
        if entrypoint is not None:
            self.entrypoint = entrypoint
        if finished_at is not None:
            self.finished_at = finished_at
        self.id = id
        self.inputs = inputs
        self.job_id = job_id
        if message is not None:
            self.message = message
        self.outputs = outputs
        if source is not None:
            self.source = source
        self.started_at = started_at
        if status is not None:
            self.status = status
        if steps is not None:
            self.steps = steps
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this RunStatus.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this RunStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this RunStatus.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this RunStatus.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def api_version(self):
        """Gets the api_version of this RunStatus.  # noqa: E501


        :return: The api_version of this RunStatus.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this RunStatus.


        :param api_version: The api_version of this RunStatus.  # noqa: E501
        :type api_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_version is not None and not re.search(r'^v1beta1$', api_version)):  # noqa: E501
            raise ValueError(r"Invalid value for `api_version`, must be a follow pattern or equal to `/^v1beta1$/`")  # noqa: E501

        self._api_version = api_version

    @property
    def entrypoint(self):
        """Gets the entrypoint of this RunStatus.  # noqa: E501

        The ID of the first step in the run.  # noqa: E501

        :return: The entrypoint of this RunStatus.  # noqa: E501
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this RunStatus.

        The ID of the first step in the run.  # noqa: E501

        :param entrypoint: The entrypoint of this RunStatus.  # noqa: E501
        :type entrypoint: str
        """

        self._entrypoint = entrypoint

    @property
    def finished_at(self):
        """Gets the finished_at of this RunStatus.  # noqa: E501

        The time at which the task was completed  # noqa: E501

        :return: The finished_at of this RunStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this RunStatus.

        The time at which the task was completed  # noqa: E501

        :param finished_at: The finished_at of this RunStatus.  # noqa: E501
        :type finished_at: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this RunStatus.  # noqa: E501

        The ID of the individual run.  # noqa: E501

        :return: The id of this RunStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunStatus.

        The ID of the individual run.  # noqa: E501

        :param id: The id of this RunStatus.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def inputs(self):
        """Gets the inputs of this RunStatus.  # noqa: E501

        The inputs used for this run.  # noqa: E501

        :return: The inputs of this RunStatus.  # noqa: E501
        :rtype: list[AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this RunStatus.

        The inputs used for this run.  # noqa: E501

        :param inputs: The inputs of this RunStatus.  # noqa: E501
        :type inputs: list[AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput]
        """
        if self.local_vars_configuration.client_side_validation and inputs is None:  # noqa: E501
            raise ValueError("Invalid value for `inputs`, must not be `None`")  # noqa: E501

        self._inputs = inputs

    @property
    def job_id(self):
        """Gets the job_id of this RunStatus.  # noqa: E501

        The ID of the job that generated this run.  # noqa: E501

        :return: The job_id of this RunStatus.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RunStatus.

        The ID of the job that generated this run.  # noqa: E501

        :param job_id: The job_id of this RunStatus.  # noqa: E501
        :type job_id: str
        """
        if self.local_vars_configuration.client_side_validation and job_id is None:  # noqa: E501
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def message(self):
        """Gets the message of this RunStatus.  # noqa: E501

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :return: The message of this RunStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RunStatus.

        Any message produced by the task. Usually error/debugging hints.  # noqa: E501

        :param message: The message of this RunStatus.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def outputs(self):
        """Gets the outputs of this RunStatus.  # noqa: E501

        The outputs produced by this run.  # noqa: E501

        :return: The outputs of this RunStatus.  # noqa: E501
        :rtype: list[AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this RunStatus.

        The outputs produced by this run.  # noqa: E501

        :param outputs: The outputs of this RunStatus.  # noqa: E501
        :type outputs: list[AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput]
        """
        if self.local_vars_configuration.client_side_validation and outputs is None:  # noqa: E501
            raise ValueError("Invalid value for `outputs`, must not be `None`")  # noqa: E501

        self._outputs = outputs

    @property
    def source(self):
        """Gets the source of this RunStatus.  # noqa: E501

        Source url for the status object. It can be a recipe or a function.  # noqa: E501

        :return: The source of this RunStatus.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RunStatus.

        Source url for the status object. It can be a recipe or a function.  # noqa: E501

        :param source: The source of this RunStatus.  # noqa: E501
        :type source: str
        """

        self._source = source

    @property
    def started_at(self):
        """Gets the started_at of this RunStatus.  # noqa: E501

        The time at which the task was started  # noqa: E501

        :return: The started_at of this RunStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this RunStatus.

        The time at which the task was started  # noqa: E501

        :param started_at: The started_at of this RunStatus.  # noqa: E501
        :type started_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this RunStatus.  # noqa: E501

        The status of this run.  # noqa: E501

        :return: The status of this RunStatus.  # noqa: E501
        :rtype: RunStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RunStatus.

        The status of this run.  # noqa: E501

        :param status: The status of this RunStatus.  # noqa: E501
        :type status: RunStatusEnum
        """

        self._status = status

    @property
    def steps(self):
        """Gets the steps of this RunStatus.  # noqa: E501


        :return: The steps of this RunStatus.  # noqa: E501
        :rtype: dict(str, StepStatus)
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this RunStatus.


        :param steps: The steps of this RunStatus.  # noqa: E501
        :type steps: dict(str, StepStatus)
        """

        self._steps = steps

    @property
    def type(self):
        """Gets the type of this RunStatus.  # noqa: E501


        :return: The type of this RunStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RunStatus.


        :param type: The type of this RunStatus.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^RunStatus$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^RunStatus$/`")  # noqa: E501

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
        if not isinstance(other, RunStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunStatus):
            return True

        return self.to_dict() != other.to_dict()
