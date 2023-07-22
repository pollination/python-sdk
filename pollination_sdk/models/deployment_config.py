# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.42.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class DeploymentConfig(object):
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
        'cpu_limit': 'int',
        'entrypoint_file': 'str',
        'login_required': 'bool',
        'memory_limit': 'int',
        'scale_to_zero': 'bool'
    }

    attribute_map = {
        'cpu_limit': 'cpu_limit',
        'entrypoint_file': 'entrypoint_file',
        'login_required': 'login_required',
        'memory_limit': 'memory_limit',
        'scale_to_zero': 'scale_to_zero'
    }

    def __init__(self, cpu_limit=1, entrypoint_file='app.py', login_required=True, memory_limit=2000, scale_to_zero=True, local_vars_configuration=None):  # noqa: E501
        """DeploymentConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu_limit = None
        self._entrypoint_file = None
        self._login_required = None
        self._memory_limit = None
        self._scale_to_zero = None
        self.discriminator = None

        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if entrypoint_file is not None:
            self.entrypoint_file = entrypoint_file
        if login_required is not None:
            self.login_required = login_required
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if scale_to_zero is not None:
            self.scale_to_zero = scale_to_zero

    @property
    def cpu_limit(self):
        """Gets the cpu_limit of this DeploymentConfig.  # noqa: E501

        The maximum number of CPU cores that can be used by the application.  # noqa: E501

        :return: The cpu_limit of this DeploymentConfig.  # noqa: E501
        :rtype: int
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        """Sets the cpu_limit of this DeploymentConfig.

        The maximum number of CPU cores that can be used by the application.  # noqa: E501

        :param cpu_limit: The cpu_limit of this DeploymentConfig.  # noqa: E501
        :type cpu_limit: int
        """

        self._cpu_limit = cpu_limit

    @property
    def entrypoint_file(self):
        """Gets the entrypoint_file of this DeploymentConfig.  # noqa: E501

        The Streamlit python file to use as an entrypoint to the app  # noqa: E501

        :return: The entrypoint_file of this DeploymentConfig.  # noqa: E501
        :rtype: str
        """
        return self._entrypoint_file

    @entrypoint_file.setter
    def entrypoint_file(self, entrypoint_file):
        """Sets the entrypoint_file of this DeploymentConfig.

        The Streamlit python file to use as an entrypoint to the app  # noqa: E501

        :param entrypoint_file: The entrypoint_file of this DeploymentConfig.  # noqa: E501
        :type entrypoint_file: str
        """

        self._entrypoint_file = entrypoint_file

    @property
    def login_required(self):
        """Gets the login_required of this DeploymentConfig.  # noqa: E501

        Whether the application requires login.  # noqa: E501

        :return: The login_required of this DeploymentConfig.  # noqa: E501
        :rtype: bool
        """
        return self._login_required

    @login_required.setter
    def login_required(self, login_required):
        """Sets the login_required of this DeploymentConfig.

        Whether the application requires login.  # noqa: E501

        :param login_required: The login_required of this DeploymentConfig.  # noqa: E501
        :type login_required: bool
        """

        self._login_required = login_required

    @property
    def memory_limit(self):
        """Gets the memory_limit of this DeploymentConfig.  # noqa: E501

        The maximum amount of memory that can be used by the application.  # noqa: E501

        :return: The memory_limit of this DeploymentConfig.  # noqa: E501
        :rtype: int
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        """Sets the memory_limit of this DeploymentConfig.

        The maximum amount of memory that can be used by the application.  # noqa: E501

        :param memory_limit: The memory_limit of this DeploymentConfig.  # noqa: E501
        :type memory_limit: int
        """

        self._memory_limit = memory_limit

    @property
    def scale_to_zero(self):
        """Gets the scale_to_zero of this DeploymentConfig.  # noqa: E501

        A boolean toggle to scale deployments down to zero replicas when not used.  # noqa: E501

        :return: The scale_to_zero of this DeploymentConfig.  # noqa: E501
        :rtype: bool
        """
        return self._scale_to_zero

    @scale_to_zero.setter
    def scale_to_zero(self, scale_to_zero):
        """Sets the scale_to_zero of this DeploymentConfig.

        A boolean toggle to scale deployments down to zero replicas when not used.  # noqa: E501

        :param scale_to_zero: The scale_to_zero of this DeploymentConfig.  # noqa: E501
        :type scale_to_zero: bool
        """

        self._scale_to_zero = scale_to_zero

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
        if not isinstance(other, DeploymentConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentConfig):
            return True

        return self.to_dict() != other.to_dict()
