# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.37.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Organization(object):
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
        'account_name': 'str',
        'contact_email': 'str',
        'description': 'str',
        'id': 'str',
        'member_count': 'int',
        'name': 'str',
        'owner': 'AccountPublic',
        'picture_url': 'str',
        'role': 'OrganizationRoleEnum',
        'team_count': 'int'
    }

    attribute_map = {
        'account_name': 'account_name',
        'contact_email': 'contact_email',
        'description': 'description',
        'id': 'id',
        'member_count': 'member_count',
        'name': 'name',
        'owner': 'owner',
        'picture_url': 'picture_url',
        'role': 'role',
        'team_count': 'team_count'
    }

    def __init__(self, account_name=None, contact_email=None, description=None, id=None, member_count=0, name=None, owner=None, picture_url=None, role=None, team_count=0, local_vars_configuration=None):  # noqa: E501
        """Organization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_name = None
        self._contact_email = None
        self._description = None
        self._id = None
        self._member_count = None
        self._name = None
        self._owner = None
        self._picture_url = None
        self._role = None
        self._team_count = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if contact_email is not None:
            self.contact_email = contact_email
        if description is not None:
            self.description = description
        self.id = id
        if member_count is not None:
            self.member_count = member_count
        if name is not None:
            self.name = name
        self.owner = owner
        if picture_url is not None:
            self.picture_url = picture_url
        if role is not None:
            self.role = role
        if team_count is not None:
            self.team_count = team_count

    @property
    def account_name(self):
        """Gets the account_name of this Organization.  # noqa: E501

        The unique name of the org in small case without spaces  # noqa: E501

        :return: The account_name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this Organization.

        The unique name of the org in small case without spaces  # noqa: E501

        :param account_name: The account_name of this Organization.  # noqa: E501
        :type account_name: str
        """

        self._account_name = account_name

    @property
    def contact_email(self):
        """Gets the contact_email of this Organization.  # noqa: E501

        The contact email for the Organization  # noqa: E501

        :return: The contact_email of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this Organization.

        The contact email for the Organization  # noqa: E501

        :param contact_email: The contact_email of this Organization.  # noqa: E501
        :type contact_email: str
        """

        self._contact_email = contact_email

    @property
    def description(self):
        """Gets the description of this Organization.  # noqa: E501

        A description of the org  # noqa: E501

        :return: The description of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Organization.

        A description of the org  # noqa: E501

        :param description: The description of this Organization.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Organization.  # noqa: E501

        The org ID  # noqa: E501

        :return: The id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.

        The org ID  # noqa: E501

        :param id: The id of this Organization.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def member_count(self):
        """Gets the member_count of this Organization.  # noqa: E501

        The number of members that are part of this org  # noqa: E501

        :return: The member_count of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this Organization.

        The number of members that are part of this org  # noqa: E501

        :param member_count: The member_count of this Organization.  # noqa: E501
        :type member_count: int
        """

        self._member_count = member_count

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501

        The display name for this org  # noqa: E501

        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.

        The display name for this org  # noqa: E501

        :param name: The name of this Organization.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this Organization.  # noqa: E501

        The account the organization represents  # noqa: E501

        :return: The owner of this Organization.  # noqa: E501
        :rtype: AccountPublic
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Organization.

        The account the organization represents  # noqa: E501

        :param owner: The owner of this Organization.  # noqa: E501
        :type owner: AccountPublic
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def picture_url(self):
        """Gets the picture_url of this Organization.  # noqa: E501

        URL to the picture associated with this org  # noqa: E501

        :return: The picture_url of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._picture_url

    @picture_url.setter
    def picture_url(self, picture_url):
        """Sets the picture_url of this Organization.

        URL to the picture associated with this org  # noqa: E501

        :param picture_url: The picture_url of this Organization.  # noqa: E501
        :type picture_url: str
        """

        self._picture_url = picture_url

    @property
    def role(self):
        """Gets the role of this Organization.  # noqa: E501

        The role the user has within the organization  # noqa: E501

        :return: The role of this Organization.  # noqa: E501
        :rtype: OrganizationRoleEnum
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Organization.

        The role the user has within the organization  # noqa: E501

        :param role: The role of this Organization.  # noqa: E501
        :type role: OrganizationRoleEnum
        """

        self._role = role

    @property
    def team_count(self):
        """Gets the team_count of this Organization.  # noqa: E501

        The number of teams that are part of this org  # noqa: E501

        :return: The team_count of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._team_count

    @team_count.setter
    def team_count(self, team_count):
        """Sets the team_count of this Organization.

        The number of teams that are part of this org  # noqa: E501

        :param team_count: The team_count of this Organization.  # noqa: E501
        :type team_count: int
        """

        self._team_count = team_count

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
        if not isinstance(other, Organization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Organization):
            return True

        return self.to_dict() != other.to_dict()
