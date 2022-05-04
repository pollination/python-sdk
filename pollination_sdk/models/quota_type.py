# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.30.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class QuotaType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    STORAGE = "storage"
    COMPUTE_HOURS = "compute_hours"
    PARALLEL_WORKFLOW_CONTAINERS = "parallel_workflow_containers"
    PRIVATE_REPOSITORIES = "private_repositories"
    PRIVATE_PROJECTS = "private_projects"
    TEAMS = "teams"
    MEMBERS = "members"
    CPU_LIMIT = "cpu_limit"
    MEMORY_LIMIT = "memory_limit"
    RHINO_PLUGIN_LICENSE = "rhino_plugin_license"
    REVIT_PLUGIN_LICENSE = "revit_plugin_license"
    APPLICATION_CPU = "application_cpu"
    APPLICATION_MEMORY = "application_memory"

    allowable_values = [STORAGE, COMPUTE_HOURS, PARALLEL_WORKFLOW_CONTAINERS, PRIVATE_REPOSITORIES, PRIVATE_PROJECTS, TEAMS, MEMBERS, CPU_LIMIT, MEMORY_LIMIT, RHINO_PLUGIN_LICENSE, REVIT_PLUGIN_LICENSE, APPLICATION_CPU, APPLICATION_MEMORY]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """QuotaType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, QuotaType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuotaType):
            return True

        return self.to_dict() != other.to_dict()
