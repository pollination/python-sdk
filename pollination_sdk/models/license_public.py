# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class LicensePublic(object):
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
        'allowed_activations': 'int',
        'created_at': 'datetime',
        'id': 'str',
        'key': 'str',
        'lease_duration': 'int',
        'metadata': 'list[Metadata]',
        'notes': 'str',
        'product_id': 'str',
        'revoked': 'bool',
        'server_sync_grace_period': 'int',
        'server_sync_interval': 'int',
        'suspended': 'bool',
        'total_activations': 'int',
        'total_deactivations': 'int',
        'type': 'LicenseType',
        'updated_at': 'datetime',
        'validity': 'int'
    }

    attribute_map = {
        'allowed_activations': 'allowed_activations',
        'created_at': 'created_at',
        'id': 'id',
        'key': 'key',
        'lease_duration': 'lease_duration',
        'metadata': 'metadata',
        'notes': 'notes',
        'product_id': 'product_id',
        'revoked': 'revoked',
        'server_sync_grace_period': 'server_sync_grace_period',
        'server_sync_interval': 'server_sync_interval',
        'suspended': 'suspended',
        'total_activations': 'total_activations',
        'total_deactivations': 'total_deactivations',
        'type': 'type',
        'updated_at': 'updated_at',
        'validity': 'validity'
    }

    def __init__(self, allowed_activations=None, created_at=None, id=None, key=None, lease_duration=None, metadata=None, notes=None, product_id=None, revoked=None, server_sync_grace_period=None, server_sync_interval=None, suspended=None, total_activations=None, total_deactivations=None, type=None, updated_at=None, validity=None, local_vars_configuration=None):  # noqa: E501
        """LicensePublic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allowed_activations = None
        self._created_at = None
        self._id = None
        self._key = None
        self._lease_duration = None
        self._metadata = None
        self._notes = None
        self._product_id = None
        self._revoked = None
        self._server_sync_grace_period = None
        self._server_sync_interval = None
        self._suspended = None
        self._total_activations = None
        self._total_deactivations = None
        self._type = None
        self._updated_at = None
        self._validity = None
        self.discriminator = None

        self.allowed_activations = allowed_activations
        self.created_at = created_at
        self.id = id
        self.key = key
        self.lease_duration = lease_duration
        self.metadata = metadata
        if notes is not None:
            self.notes = notes
        self.product_id = product_id
        self.revoked = revoked
        self.server_sync_grace_period = server_sync_grace_period
        self.server_sync_interval = server_sync_interval
        self.suspended = suspended
        self.total_activations = total_activations
        self.total_deactivations = total_deactivations
        self.type = type
        self.updated_at = updated_at
        self.validity = validity

    @property
    def allowed_activations(self):
        """Gets the allowed_activations of this LicensePublic.  # noqa: E501


        :return: The allowed_activations of this LicensePublic.  # noqa: E501
        :rtype: int
        """
        return self._allowed_activations

    @allowed_activations.setter
    def allowed_activations(self, allowed_activations):
        """Sets the allowed_activations of this LicensePublic.


        :param allowed_activations: The allowed_activations of this LicensePublic.  # noqa: E501
        :type allowed_activations: int
        """
        if self.local_vars_configuration.client_side_validation and allowed_activations is None:  # noqa: E501
            raise ValueError("Invalid value for `allowed_activations`, must not be `None`")  # noqa: E501

        self._allowed_activations = allowed_activations

    @property
    def created_at(self):
        """Gets the created_at of this LicensePublic.  # noqa: E501


        :return: The created_at of this LicensePublic.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LicensePublic.


        :param created_at: The created_at of this LicensePublic.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this LicensePublic.  # noqa: E501


        :return: The id of this LicensePublic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LicensePublic.


        :param id: The id of this LicensePublic.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def key(self):
        """Gets the key of this LicensePublic.  # noqa: E501

        The key used to activate this license. Treat this like a password.  # noqa: E501

        :return: The key of this LicensePublic.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LicensePublic.

        The key used to activate this license. Treat this like a password.  # noqa: E501

        :param key: The key of this LicensePublic.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def lease_duration(self):
        """Gets the lease_duration of this LicensePublic.  # noqa: E501


        :return: The lease_duration of this LicensePublic.  # noqa: E501
        :rtype: int
        """
        return self._lease_duration

    @lease_duration.setter
    def lease_duration(self, lease_duration):
        """Sets the lease_duration of this LicensePublic.


        :param lease_duration: The lease_duration of this LicensePublic.  # noqa: E501
        :type lease_duration: int
        """
        if self.local_vars_configuration.client_side_validation and lease_duration is None:  # noqa: E501
            raise ValueError("Invalid value for `lease_duration`, must not be `None`")  # noqa: E501

        self._lease_duration = lease_duration

    @property
    def metadata(self):
        """Gets the metadata of this LicensePublic.  # noqa: E501


        :return: The metadata of this LicensePublic.  # noqa: E501
        :rtype: list[Metadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this LicensePublic.


        :param metadata: The metadata of this LicensePublic.  # noqa: E501
        :type metadata: list[Metadata]
        """
        if self.local_vars_configuration.client_side_validation and metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def notes(self):
        """Gets the notes of this LicensePublic.  # noqa: E501


        :return: The notes of this LicensePublic.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this LicensePublic.


        :param notes: The notes of this LicensePublic.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def product_id(self):
        """Gets the product_id of this LicensePublic.  # noqa: E501


        :return: The product_id of this LicensePublic.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this LicensePublic.


        :param product_id: The product_id of this LicensePublic.  # noqa: E501
        :type product_id: str
        """
        if self.local_vars_configuration.client_side_validation and product_id is None:  # noqa: E501
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def revoked(self):
        """Gets the revoked of this LicensePublic.  # noqa: E501


        :return: The revoked of this LicensePublic.  # noqa: E501
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this LicensePublic.


        :param revoked: The revoked of this LicensePublic.  # noqa: E501
        :type revoked: bool
        """
        if self.local_vars_configuration.client_side_validation and revoked is None:  # noqa: E501
            raise ValueError("Invalid value for `revoked`, must not be `None`")  # noqa: E501

        self._revoked = revoked

    @property
    def server_sync_grace_period(self):
        """Gets the server_sync_grace_period of this LicensePublic.  # noqa: E501


        :return: The server_sync_grace_period of this LicensePublic.  # noqa: E501
        :rtype: int
        """
        return self._server_sync_grace_period

    @server_sync_grace_period.setter
    def server_sync_grace_period(self, server_sync_grace_period):
        """Sets the server_sync_grace_period of this LicensePublic.


        :param server_sync_grace_period: The server_sync_grace_period of this LicensePublic.  # noqa: E501
        :type server_sync_grace_period: int
        """
        if self.local_vars_configuration.client_side_validation and server_sync_grace_period is None:  # noqa: E501
            raise ValueError("Invalid value for `server_sync_grace_period`, must not be `None`")  # noqa: E501

        self._server_sync_grace_period = server_sync_grace_period

    @property
    def server_sync_interval(self):
        """Gets the server_sync_interval of this LicensePublic.  # noqa: E501


        :return: The server_sync_interval of this LicensePublic.  # noqa: E501
        :rtype: int
        """
        return self._server_sync_interval

    @server_sync_interval.setter
    def server_sync_interval(self, server_sync_interval):
        """Sets the server_sync_interval of this LicensePublic.


        :param server_sync_interval: The server_sync_interval of this LicensePublic.  # noqa: E501
        :type server_sync_interval: int
        """
        if self.local_vars_configuration.client_side_validation and server_sync_interval is None:  # noqa: E501
            raise ValueError("Invalid value for `server_sync_interval`, must not be `None`")  # noqa: E501

        self._server_sync_interval = server_sync_interval

    @property
    def suspended(self):
        """Gets the suspended of this LicensePublic.  # noqa: E501


        :return: The suspended of this LicensePublic.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this LicensePublic.


        :param suspended: The suspended of this LicensePublic.  # noqa: E501
        :type suspended: bool
        """
        if self.local_vars_configuration.client_side_validation and suspended is None:  # noqa: E501
            raise ValueError("Invalid value for `suspended`, must not be `None`")  # noqa: E501

        self._suspended = suspended

    @property
    def total_activations(self):
        """Gets the total_activations of this LicensePublic.  # noqa: E501


        :return: The total_activations of this LicensePublic.  # noqa: E501
        :rtype: int
        """
        return self._total_activations

    @total_activations.setter
    def total_activations(self, total_activations):
        """Sets the total_activations of this LicensePublic.


        :param total_activations: The total_activations of this LicensePublic.  # noqa: E501
        :type total_activations: int
        """
        if self.local_vars_configuration.client_side_validation and total_activations is None:  # noqa: E501
            raise ValueError("Invalid value for `total_activations`, must not be `None`")  # noqa: E501

        self._total_activations = total_activations

    @property
    def total_deactivations(self):
        """Gets the total_deactivations of this LicensePublic.  # noqa: E501


        :return: The total_deactivations of this LicensePublic.  # noqa: E501
        :rtype: int
        """
        return self._total_deactivations

    @total_deactivations.setter
    def total_deactivations(self, total_deactivations):
        """Sets the total_deactivations of this LicensePublic.


        :param total_deactivations: The total_deactivations of this LicensePublic.  # noqa: E501
        :type total_deactivations: int
        """
        if self.local_vars_configuration.client_side_validation and total_deactivations is None:  # noqa: E501
            raise ValueError("Invalid value for `total_deactivations`, must not be `None`")  # noqa: E501

        self._total_deactivations = total_deactivations

    @property
    def type(self):
        """Gets the type of this LicensePublic.  # noqa: E501


        :return: The type of this LicensePublic.  # noqa: E501
        :rtype: LicenseType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LicensePublic.


        :param type: The type of this LicensePublic.  # noqa: E501
        :type type: LicenseType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this LicensePublic.  # noqa: E501


        :return: The updated_at of this LicensePublic.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LicensePublic.


        :param updated_at: The updated_at of this LicensePublic.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def validity(self):
        """Gets the validity of this LicensePublic.  # noqa: E501


        :return: The validity of this LicensePublic.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this LicensePublic.


        :param validity: The validity of this LicensePublic.  # noqa: E501
        :type validity: int
        """
        if self.local_vars_configuration.client_side_validation and validity is None:  # noqa: E501
            raise ValueError("Invalid value for `validity`, must not be `None`")  # noqa: E501

        self._validity = validity

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
        if not isinstance(other, LicensePublic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicensePublic):
            return True

        return self.to_dict() != other.to_dict()
