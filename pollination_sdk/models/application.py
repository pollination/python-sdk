# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.44.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Application(object):
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
        'deployment_config': 'DeploymentConfig',
        'description': 'str',
        'id': 'str',
        'image': 'str',
        'is_paid': 'bool',
        'keywords': 'list[str]',
        'license': 'str',
        'name': 'str',
        'owner': 'AccountPublic',
        'permissions': 'UserPermission',
        'public': 'bool',
        'sdk': 'SDKEnum',
        'slug': 'str',
        'source': 'str'
    }

    attribute_map = {
        'deployment_config': 'deployment_config',
        'description': 'description',
        'id': 'id',
        'image': 'image',
        'is_paid': 'is_paid',
        'keywords': 'keywords',
        'license': 'license',
        'name': 'name',
        'owner': 'owner',
        'permissions': 'permissions',
        'public': 'public',
        'sdk': 'sdk',
        'slug': 'slug',
        'source': 'source'
    }

    def __init__(self, deployment_config=None, description='', id=None, image='https://picsum.photos/400', is_paid=False, keywords=[], license=None, name=None, owner=None, permissions=None, public=True, sdk=None, slug=None, source=None, local_vars_configuration=None):  # noqa: E501
        """Application - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deployment_config = None
        self._description = None
        self._id = None
        self._image = None
        self._is_paid = None
        self._keywords = None
        self._license = None
        self._name = None
        self._owner = None
        self._permissions = None
        self._public = None
        self._sdk = None
        self._slug = None
        self._source = None
        self.discriminator = None

        if deployment_config is not None:
            self.deployment_config = deployment_config
        if description is not None:
            self.description = description
        self.id = id
        if image is not None:
            self.image = image
        if is_paid is not None:
            self.is_paid = is_paid
        if keywords is not None:
            self.keywords = keywords
        if license is not None:
            self.license = license
        self.name = name
        self.owner = owner
        self.permissions = permissions
        if public is not None:
            self.public = public
        if sdk is not None:
            self.sdk = sdk
        self.slug = slug
        if source is not None:
            self.source = source

    @property
    def deployment_config(self):
        """Gets the deployment_config of this Application.  # noqa: E501

        The deployment configuration for the application  # noqa: E501

        :return: The deployment_config of this Application.  # noqa: E501
        :rtype: DeploymentConfig
        """
        return self._deployment_config

    @deployment_config.setter
    def deployment_config(self, deployment_config):
        """Sets the deployment_config of this Application.

        The deployment configuration for the application  # noqa: E501

        :param deployment_config: The deployment_config of this Application.  # noqa: E501
        :type deployment_config: DeploymentConfig
        """

        self._deployment_config = deployment_config

    @property
    def description(self):
        """Gets the description of this Application.  # noqa: E501

        A description of the application  # noqa: E501

        :return: The description of this Application.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Application.

        A description of the application  # noqa: E501

        :param description: The description of this Application.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Application.  # noqa: E501

        The application ID  # noqa: E501

        :return: The id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.

        The application ID  # noqa: E501

        :param id: The id of this Application.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def image(self):
        """Gets the image of this Application.  # noqa: E501

        An image associated with the application  # noqa: E501

        :return: The image of this Application.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Application.

        An image associated with the application  # noqa: E501

        :param image: The image of this Application.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def is_paid(self):
        """Gets the is_paid of this Application.  # noqa: E501

        Whether or not the application is paid  # noqa: E501

        :return: The is_paid of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._is_paid

    @is_paid.setter
    def is_paid(self, is_paid):
        """Sets the is_paid of this Application.

        Whether or not the application is paid  # noqa: E501

        :param is_paid: The is_paid of this Application.  # noqa: E501
        :type is_paid: bool
        """

        self._is_paid = is_paid

    @property
    def keywords(self):
        """Gets the keywords of this Application.  # noqa: E501

        A list of keywords associated with the application  # noqa: E501

        :return: The keywords of this Application.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Application.

        A list of keywords associated with the application  # noqa: E501

        :param keywords: The keywords of this Application.  # noqa: E501
        :type keywords: list[str]
        """

        self._keywords = keywords

    @property
    def license(self):
        """Gets the license of this Application.  # noqa: E501

        The license of the application  # noqa: E501

        :return: The license of this Application.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Application.

        The license of the application  # noqa: E501

        :param license: The license of this Application.  # noqa: E501
        :type license: str
        """

        self._license = license

    @property
    def name(self):
        """Gets the name of this Application.  # noqa: E501

        The name of the application. Must be unique to a given owner  # noqa: E501

        :return: The name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.

        The name of the application. Must be unique to a given owner  # noqa: E501

        :param name: The name of this Application.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this Application.  # noqa: E501

        The application owner  # noqa: E501

        :return: The owner of this Application.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Application.

        The application owner  # noqa: E501

        :param owner: The owner of this Application.  # noqa: E501
        :type owner: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def permissions(self):
        """Gets the permissions of this Application.  # noqa: E501


        :return: The permissions of this Application.  # noqa: E501
        :rtype: UserPermission
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Application.


        :param permissions: The permissions of this Application.  # noqa: E501
        :type permissions: UserPermission
        """
        if self.local_vars_configuration.client_side_validation and permissions is None:  # noqa: E501
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def public(self):
        """Gets the public of this Application.  # noqa: E501

        Whether or not a application is publicly viewable  # noqa: E501

        :return: The public of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this Application.

        Whether or not a application is publicly viewable  # noqa: E501

        :param public: The public of this Application.  # noqa: E501
        :type public: bool
        """

        self._public = public

    @property
    def sdk(self):
        """Gets the sdk of this Application.  # noqa: E501

        The SDK used to build the application  # noqa: E501

        :return: The sdk of this Application.  # noqa: E501
        :rtype: SDKEnum
        """
        return self._sdk

    @sdk.setter
    def sdk(self, sdk):
        """Sets the sdk of this Application.

        The SDK used to build the application  # noqa: E501

        :param sdk: The sdk of this Application.  # noqa: E501
        :type sdk: SDKEnum
        """

        self._sdk = sdk

    @property
    def slug(self):
        """Gets the slug of this Application.  # noqa: E501

        The application name in slug format  # noqa: E501

        :return: The slug of this Application.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Application.

        The application name in slug format  # noqa: E501

        :param slug: The slug of this Application.  # noqa: E501
        :type slug: str
        """
        if self.local_vars_configuration.client_side_validation and slug is None:  # noqa: E501
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

    @property
    def source(self):
        """Gets the source of this Application.  # noqa: E501

        A link to the source code of the application  # noqa: E501

        :return: The source of this Application.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Application.

        A link to the source code of the application  # noqa: E501

        :param source: The source of this Application.  # noqa: E501
        :type source: str
        """

        self._source = source

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
        if not isinstance(other, Application):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Application):
            return True

        return self.to_dict() != other.to_dict()
