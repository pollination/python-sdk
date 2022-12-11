# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.33.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class LicensePoolPublic(object):
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
        'accessors': 'list[Accessor]',
        'allowed_activations': 'int',
        'description': 'str',
        'id': 'str',
        'license_id': 'str',
        'owner': 'AccountPublic',
        'permissions': 'UserPermission',
        'product': 'str',
        'total_activations': 'int'
    }

    attribute_map = {
        'accessors': 'accessors',
        'allowed_activations': 'allowed_activations',
        'description': 'description',
        'id': 'id',
        'license_id': 'license_id',
        'owner': 'owner',
        'permissions': 'permissions',
        'product': 'product',
        'total_activations': 'total_activations'
    }

    def __init__(self, accessors=[], allowed_activations=None, description=None, id=None, license_id=None, owner=None, permissions=None, product=None, total_activations=None, local_vars_configuration=None):  # noqa: E501
        """LicensePoolPublic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accessors = None
        self._allowed_activations = None
        self._description = None
        self._id = None
        self._license_id = None
        self._owner = None
        self._permissions = None
        self._product = None
        self._total_activations = None
        self.discriminator = None

        if accessors is not None:
            self.accessors = accessors
        self.allowed_activations = allowed_activations
        if description is not None:
            self.description = description
        self.id = id
        self.license_id = license_id
        self.owner = owner
        self.permissions = permissions
        self.product = product
        self.total_activations = total_activations

    @property
    def accessors(self):
        """Gets the accessors of this LicensePoolPublic.  # noqa: E501

        The entities that can access the license though the pool  # noqa: E501

        :return: The accessors of this LicensePoolPublic.  # noqa: E501
        :rtype: list[Accessor]
        """
        return self._accessors

    @accessors.setter
    def accessors(self, accessors):
        """Sets the accessors of this LicensePoolPublic.

        The entities that can access the license though the pool  # noqa: E501

        :param accessors: The accessors of this LicensePoolPublic.  # noqa: E501
        :type accessors: list[Accessor]
        """

        self._accessors = accessors

    @property
    def allowed_activations(self):
        """Gets the allowed_activations of this LicensePoolPublic.  # noqa: E501

        The number of allowable activations for this license  # noqa: E501

        :return: The allowed_activations of this LicensePoolPublic.  # noqa: E501
        :rtype: int
        """
        return self._allowed_activations

    @allowed_activations.setter
    def allowed_activations(self, allowed_activations):
        """Sets the allowed_activations of this LicensePoolPublic.

        The number of allowable activations for this license  # noqa: E501

        :param allowed_activations: The allowed_activations of this LicensePoolPublic.  # noqa: E501
        :type allowed_activations: int
        """
        if self.local_vars_configuration.client_side_validation and allowed_activations is None:  # noqa: E501
            raise ValueError("Invalid value for `allowed_activations`, must not be `None`")  # noqa: E501

        self._allowed_activations = allowed_activations

    @property
    def description(self):
        """Gets the description of this LicensePoolPublic.  # noqa: E501

        The description of the pool  # noqa: E501

        :return: The description of this LicensePoolPublic.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LicensePoolPublic.

        The description of the pool  # noqa: E501

        :param description: The description of this LicensePoolPublic.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this LicensePoolPublic.  # noqa: E501

        The ID of the pool  # noqa: E501

        :return: The id of this LicensePoolPublic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LicensePoolPublic.

        The ID of the pool  # noqa: E501

        :param id: The id of this LicensePoolPublic.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def license_id(self):
        """Gets the license_id of this LicensePoolPublic.  # noqa: E501

        The ID of the license to which the pool provides access  # noqa: E501

        :return: The license_id of this LicensePoolPublic.  # noqa: E501
        :rtype: str
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        """Sets the license_id of this LicensePoolPublic.

        The ID of the license to which the pool provides access  # noqa: E501

        :param license_id: The license_id of this LicensePoolPublic.  # noqa: E501
        :type license_id: str
        """
        if self.local_vars_configuration.client_side_validation and license_id is None:  # noqa: E501
            raise ValueError("Invalid value for `license_id`, must not be `None`")  # noqa: E501

        self._license_id = license_id

    @property
    def owner(self):
        """Gets the owner of this LicensePoolPublic.  # noqa: E501

        The account that owns the license  # noqa: E501

        :return: The owner of this LicensePoolPublic.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this LicensePoolPublic.

        The account that owns the license  # noqa: E501

        :param owner: The owner of this LicensePoolPublic.  # noqa: E501
        :type owner: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def permissions(self):
        """Gets the permissions of this LicensePoolPublic.  # noqa: E501


        :return: The permissions of this LicensePoolPublic.  # noqa: E501
        :rtype: UserPermission
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this LicensePoolPublic.


        :param permissions: The permissions of this LicensePoolPublic.  # noqa: E501
        :type permissions: UserPermission
        """
        if self.local_vars_configuration.client_side_validation and permissions is None:  # noqa: E501
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def product(self):
        """Gets the product of this LicensePoolPublic.  # noqa: E501

        The pollination product to which this pool provides access  # noqa: E501

        :return: The product of this LicensePoolPublic.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this LicensePoolPublic.

        The pollination product to which this pool provides access  # noqa: E501

        :param product: The product of this LicensePoolPublic.  # noqa: E501
        :type product: str
        """
        if self.local_vars_configuration.client_side_validation and product is None:  # noqa: E501
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def total_activations(self):
        """Gets the total_activations of this LicensePoolPublic.  # noqa: E501

        The number of current activations for this license  # noqa: E501

        :return: The total_activations of this LicensePoolPublic.  # noqa: E501
        :rtype: int
        """
        return self._total_activations

    @total_activations.setter
    def total_activations(self, total_activations):
        """Sets the total_activations of this LicensePoolPublic.

        The number of current activations for this license  # noqa: E501

        :param total_activations: The total_activations of this LicensePoolPublic.  # noqa: E501
        :type total_activations: int
        """
        if self.local_vars_configuration.client_side_validation and total_activations is None:  # noqa: E501
            raise ValueError("Invalid value for `total_activations`, must not be `None`")  # noqa: E501

        self._total_activations = total_activations

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
        if not isinstance(other, LicensePoolPublic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicensePoolPublic):
            return True

        return self.to_dict() != other.to_dict()
