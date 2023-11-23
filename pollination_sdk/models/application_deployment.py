# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.45.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class ApplicationDeployment(object):
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
        'ready': 'bool',
        'url': 'str',
        'version': 'ApplicationVersion'
    }

    attribute_map = {
        'author': 'author',
        'ready': 'ready',
        'url': 'url',
        'version': 'version'
    }

    def __init__(self, author=None, ready=None, url=None, version=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationDeployment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._author = None
        self._ready = None
        self._url = None
        self._version = None
        self.discriminator = None

        self.author = author
        self.ready = ready
        self.url = url
        self.version = version

    @property
    def author(self):
        """Gets the author of this ApplicationDeployment.  # noqa: E501

        The user who deployed this app  # noqa: E501

        :return: The author of this ApplicationDeployment.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ApplicationDeployment.

        The user who deployed this app  # noqa: E501

        :param author: The author of this ApplicationDeployment.  # noqa: E501
        :type author: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and author is None:  # noqa: E501
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def ready(self):
        """Gets the ready of this ApplicationDeployment.  # noqa: E501

        Indicates whether the application deployment is ready.  # noqa: E501

        :return: The ready of this ApplicationDeployment.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this ApplicationDeployment.

        Indicates whether the application deployment is ready.  # noqa: E501

        :param ready: The ready of this ApplicationDeployment.  # noqa: E501
        :type ready: bool
        """
        if self.local_vars_configuration.client_side_validation and ready is None:  # noqa: E501
            raise ValueError("Invalid value for `ready`, must not be `None`")  # noqa: E501

        self._ready = ready

    @property
    def url(self):
        """Gets the url of this ApplicationDeployment.  # noqa: E501

        The URL of the application deployment.  # noqa: E501

        :return: The url of this ApplicationDeployment.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ApplicationDeployment.

        The URL of the application deployment.  # noqa: E501

        :param url: The url of this ApplicationDeployment.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def version(self):
        """Gets the version of this ApplicationDeployment.  # noqa: E501

        The version deployed  # noqa: E501

        :return: The version of this ApplicationDeployment.  # noqa: E501
        :rtype: ApplicationVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApplicationDeployment.

        The version deployed  # noqa: E501

        :param version: The version of this ApplicationDeployment.  # noqa: E501
        :type version: ApplicationVersion
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, ApplicationDeployment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationDeployment):
            return True

        return self.to_dict() != other.to_dict()
