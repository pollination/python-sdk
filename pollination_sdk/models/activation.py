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


class Activation(object):
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
        'app_version': 'str',
        'created_at': 'datetime',
        'hostname': 'str',
        'id': 'str',
        'last_synced_at': 'datetime',
        'lease_expires_at': 'datetime',
        'license_id': 'str',
        'location': 'Location',
        'metadata': 'list[Metadata]',
        'offline': 'bool',
        'os': 'str',
        'os_version': 'str',
        'updated_at': 'datetime',
        'user': 'AccountPublic'
    }

    attribute_map = {
        'app_version': 'app_version',
        'created_at': 'created_at',
        'hostname': 'hostname',
        'id': 'id',
        'last_synced_at': 'last_synced_at',
        'lease_expires_at': 'lease_expires_at',
        'license_id': 'license_id',
        'location': 'location',
        'metadata': 'metadata',
        'offline': 'offline',
        'os': 'os',
        'os_version': 'os_version',
        'updated_at': 'updated_at',
        'user': 'user'
    }

    def __init__(self, app_version=None, created_at=None, hostname=None, id=None, last_synced_at=None, lease_expires_at=None, license_id=None, location=None, metadata=[], offline=None, os=None, os_version=None, updated_at=None, user=None, local_vars_configuration=None):  # noqa: E501
        """Activation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_version = None
        self._created_at = None
        self._hostname = None
        self._id = None
        self._last_synced_at = None
        self._lease_expires_at = None
        self._license_id = None
        self._location = None
        self._metadata = None
        self._offline = None
        self._os = None
        self._os_version = None
        self._updated_at = None
        self._user = None
        self.discriminator = None

        if app_version is not None:
            self.app_version = app_version
        self.created_at = created_at
        if hostname is not None:
            self.hostname = hostname
        self.id = id
        self.last_synced_at = last_synced_at
        if lease_expires_at is not None:
            self.lease_expires_at = lease_expires_at
        if license_id is not None:
            self.license_id = license_id
        self.location = location
        if metadata is not None:
            self.metadata = metadata
        self.offline = offline
        if os is not None:
            self.os = os
        if os_version is not None:
            self.os_version = os_version
        self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def app_version(self):
        """Gets the app_version of this Activation.  # noqa: E501


        :return: The app_version of this Activation.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this Activation.


        :param app_version: The app_version of this Activation.  # noqa: E501
        :type app_version: str
        """

        self._app_version = app_version

    @property
    def created_at(self):
        """Gets the created_at of this Activation.  # noqa: E501


        :return: The created_at of this Activation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Activation.


        :param created_at: The created_at of this Activation.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def hostname(self):
        """Gets the hostname of this Activation.  # noqa: E501


        :return: The hostname of this Activation.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Activation.


        :param hostname: The hostname of this Activation.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this Activation.  # noqa: E501


        :return: The id of this Activation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Activation.


        :param id: The id of this Activation.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_synced_at(self):
        """Gets the last_synced_at of this Activation.  # noqa: E501


        :return: The last_synced_at of this Activation.  # noqa: E501
        :rtype: datetime
        """
        return self._last_synced_at

    @last_synced_at.setter
    def last_synced_at(self, last_synced_at):
        """Sets the last_synced_at of this Activation.


        :param last_synced_at: The last_synced_at of this Activation.  # noqa: E501
        :type last_synced_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_synced_at is None:  # noqa: E501
            raise ValueError("Invalid value for `last_synced_at`, must not be `None`")  # noqa: E501

        self._last_synced_at = last_synced_at

    @property
    def lease_expires_at(self):
        """Gets the lease_expires_at of this Activation.  # noqa: E501


        :return: The lease_expires_at of this Activation.  # noqa: E501
        :rtype: datetime
        """
        return self._lease_expires_at

    @lease_expires_at.setter
    def lease_expires_at(self, lease_expires_at):
        """Sets the lease_expires_at of this Activation.


        :param lease_expires_at: The lease_expires_at of this Activation.  # noqa: E501
        :type lease_expires_at: datetime
        """

        self._lease_expires_at = lease_expires_at

    @property
    def license_id(self):
        """Gets the license_id of this Activation.  # noqa: E501


        :return: The license_id of this Activation.  # noqa: E501
        :rtype: str
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        """Sets the license_id of this Activation.


        :param license_id: The license_id of this Activation.  # noqa: E501
        :type license_id: str
        """

        self._license_id = license_id

    @property
    def location(self):
        """Gets the location of this Activation.  # noqa: E501


        :return: The location of this Activation.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Activation.


        :param location: The location of this Activation.  # noqa: E501
        :type location: Location
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def metadata(self):
        """Gets the metadata of this Activation.  # noqa: E501


        :return: The metadata of this Activation.  # noqa: E501
        :rtype: list[Metadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Activation.


        :param metadata: The metadata of this Activation.  # noqa: E501
        :type metadata: list[Metadata]
        """

        self._metadata = metadata

    @property
    def offline(self):
        """Gets the offline of this Activation.  # noqa: E501


        :return: The offline of this Activation.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this Activation.


        :param offline: The offline of this Activation.  # noqa: E501
        :type offline: bool
        """
        if self.local_vars_configuration.client_side_validation and offline is None:  # noqa: E501
            raise ValueError("Invalid value for `offline`, must not be `None`")  # noqa: E501

        self._offline = offline

    @property
    def os(self):
        """Gets the os of this Activation.  # noqa: E501


        :return: The os of this Activation.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this Activation.


        :param os: The os of this Activation.  # noqa: E501
        :type os: str
        """

        self._os = os

    @property
    def os_version(self):
        """Gets the os_version of this Activation.  # noqa: E501


        :return: The os_version of this Activation.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this Activation.


        :param os_version: The os_version of this Activation.  # noqa: E501
        :type os_version: str
        """

        self._os_version = os_version

    @property
    def updated_at(self):
        """Gets the updated_at of this Activation.  # noqa: E501


        :return: The updated_at of this Activation.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Activation.


        :param updated_at: The updated_at of this Activation.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this Activation.  # noqa: E501

        The user associated with the activation  # noqa: E501

        :return: The user of this Activation.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Activation.

        The user associated with the activation  # noqa: E501

        :param user: The user of this Activation.  # noqa: E501
        :type user: AccountPublic
        """

        self._user = user

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
        if not isinstance(other, Activation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Activation):
            return True

        return self.to_dict() != other.to_dict()
