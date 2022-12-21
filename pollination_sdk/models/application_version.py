# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.35.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class ApplicationVersion(object):
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
        'build_status': 'BuildStatus',
        'created_at': 'datetime',
        'id': 'str',
        'release_notes': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'author': 'author',
        'build_status': 'build_status',
        'created_at': 'created_at',
        'id': 'id',
        'release_notes': 'release_notes',
        'tag': 'tag'
    }

    def __init__(self, author=None, build_status=None, created_at=None, id=None, release_notes='', tag=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._author = None
        self._build_status = None
        self._created_at = None
        self._id = None
        self._release_notes = None
        self._tag = None
        self.discriminator = None

        self.author = author
        self.build_status = build_status
        if created_at is not None:
            self.created_at = created_at
        self.id = id
        if release_notes is not None:
            self.release_notes = release_notes
        self.tag = tag

    @property
    def author(self):
        """Gets the author of this ApplicationVersion.  # noqa: E501

        The author that created the application version  # noqa: E501

        :return: The author of this ApplicationVersion.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ApplicationVersion.

        The author that created the application version  # noqa: E501

        :param author: The author of this ApplicationVersion.  # noqa: E501
        :type author: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and author is None:  # noqa: E501
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def build_status(self):
        """Gets the build_status of this ApplicationVersion.  # noqa: E501

        The status of the application version build  # noqa: E501

        :return: The build_status of this ApplicationVersion.  # noqa: E501
        :rtype: BuildStatus
        """
        return self._build_status

    @build_status.setter
    def build_status(self, build_status):
        """Sets the build_status of this ApplicationVersion.

        The status of the application version build  # noqa: E501

        :param build_status: The build_status of this ApplicationVersion.  # noqa: E501
        :type build_status: BuildStatus
        """
        if self.local_vars_configuration.client_side_validation and build_status is None:  # noqa: E501
            raise ValueError("Invalid value for `build_status`, must not be `None`")  # noqa: E501

        self._build_status = build_status

    @property
    def created_at(self):
        """Gets the created_at of this ApplicationVersion.  # noqa: E501

        The time the application version was created  # noqa: E501

        :return: The created_at of this ApplicationVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApplicationVersion.

        The time the application version was created  # noqa: E501

        :param created_at: The created_at of this ApplicationVersion.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this ApplicationVersion.  # noqa: E501

        The application version ID  # noqa: E501

        :return: The id of this ApplicationVersion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationVersion.

        The application version ID  # noqa: E501

        :param id: The id of this ApplicationVersion.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def release_notes(self):
        """Gets the release_notes of this ApplicationVersion.  # noqa: E501

        The release notes for the application version  # noqa: E501

        :return: The release_notes of this ApplicationVersion.  # noqa: E501
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this ApplicationVersion.

        The release notes for the application version  # noqa: E501

        :param release_notes: The release_notes of this ApplicationVersion.  # noqa: E501
        :type release_notes: str
        """

        self._release_notes = release_notes

    @property
    def tag(self):
        """Gets the tag of this ApplicationVersion.  # noqa: E501

        The tag for this version of the application  # noqa: E501

        :return: The tag of this ApplicationVersion.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ApplicationVersion.

        The tag for this version of the application  # noqa: E501

        :param tag: The tag of this ApplicationVersion.  # noqa: E501
        :type tag: str
        """
        if self.local_vars_configuration.client_side_validation and tag is None:  # noqa: E501
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

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
        if not isinstance(other, ApplicationVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationVersion):
            return True

        return self.to_dict() != other.to_dict()
