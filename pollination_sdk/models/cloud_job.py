# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.46.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class CloudJob(object):
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
        'author': 'AccountPublic',
        'id': 'str',
        'owner': 'AccountPublic',
        'recipe': 'RecipeInterface',
        'resources_duration': 'ResourcesDuration',
        'spec': 'Job',
        'status': 'JobStatus'
    }

    attribute_map = {
        'author': 'author',
        'id': 'id',
        'owner': 'owner',
        'recipe': 'recipe',
        'resources_duration': 'resources_duration',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, author=None, id=None, owner=None, recipe=None, resources_duration=None, spec=None, status=None, local_vars_configuration=None):  # noqa: E501
        """CloudJob - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._author = None
        self._id = None
        self._owner = None
        self._recipe = None
        self._resources_duration = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if author is not None:
            self.author = author
        self.id = id
        if owner is not None:
            self.owner = owner
        if recipe is not None:
            self.recipe = recipe
        if resources_duration is not None:
            self.resources_duration = resources_duration
        self.spec = spec
        if status is not None:
            self.status = status

    @property
    def author(self):
        """Gets the author of this CloudJob.  # noqa: E501

        author  # noqa: E501

        :return: The author of this CloudJob.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this CloudJob.

        author  # noqa: E501

        :param author: The author of this CloudJob.  # noqa: E501
        :type author: AccountPublic
        """

        self._author = author

    @property
    def id(self):
        """Gets the id of this CloudJob.  # noqa: E501

        The unique ID for this run  # noqa: E501

        :return: The id of this CloudJob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudJob.

        The unique ID for this run  # noqa: E501

        :param id: The id of this CloudJob.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this CloudJob.  # noqa: E501

        owner  # noqa: E501

        :return: The owner of this CloudJob.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CloudJob.

        owner  # noqa: E501

        :param owner: The owner of this CloudJob.  # noqa: E501
        :type owner: AccountPublic
        """

        self._owner = owner

    @property
    def recipe(self):
        """Gets the recipe of this CloudJob.  # noqa: E501

        The recipe used to generate this   # noqa: E501

        :return: The recipe of this CloudJob.  # noqa: E501
        :rtype: RecipeInterface
        """
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        """Sets the recipe of this CloudJob.

        The recipe used to generate this   # noqa: E501

        :param recipe: The recipe of this CloudJob.  # noqa: E501
        :type recipe: RecipeInterface
        """

        self._recipe = recipe

    @property
    def resources_duration(self):
        """Gets the resources_duration of this CloudJob.  # noqa: E501

        CPU and Memory usage aggregated for all runs in this job  # noqa: E501

        :return: The resources_duration of this CloudJob.  # noqa: E501
        :rtype: ResourcesDuration
        """
        return self._resources_duration

    @resources_duration.setter
    def resources_duration(self, resources_duration):
        """Sets the resources_duration of this CloudJob.

        CPU and Memory usage aggregated for all runs in this job  # noqa: E501

        :param resources_duration: The resources_duration of this CloudJob.  # noqa: E501
        :type resources_duration: ResourcesDuration
        """

        self._resources_duration = resources_duration

    @property
    def spec(self):
        """Gets the spec of this CloudJob.  # noqa: E501

        The job specification  # noqa: E501

        :return: The spec of this CloudJob.  # noqa: E501
        :rtype: Job
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this CloudJob.

        The job specification  # noqa: E501

        :param spec: The spec of this CloudJob.  # noqa: E501
        :type spec: Job
        """
        if self.local_vars_configuration.client_side_validation and spec is None:  # noqa: E501
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

    @property
    def status(self):
        """Gets the status of this CloudJob.  # noqa: E501

        The status of the job  # noqa: E501

        :return: The status of this CloudJob.  # noqa: E501
        :rtype: JobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CloudJob.

        The status of the job  # noqa: E501

        :param status: The status of this CloudJob.  # noqa: E501
        :type status: JobStatus
        """

        self._status = status

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
        if not isinstance(other, CloudJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudJob):
            return True

        return self.to_dict() != other.to_dict()
