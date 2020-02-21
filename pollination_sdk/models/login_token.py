# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.2.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class LoginToken(object):
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
        'access_token': 'str',
        'id_token': 'str',
        'scope': 'str',
        'token_type': 'str',
        'expires_in': 'int'
    }

    attribute_map = {
        'access_token': 'access_token',
        'id_token': 'id_token',
        'scope': 'scope',
        'token_type': 'token_type',
        'expires_in': 'expires_in'
    }

    def __init__(self, access_token=None, id_token=None, scope=None, token_type=None, expires_in=None, local_vars_configuration=None):  # noqa: E501
        """LoginToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._id_token = None
        self._scope = None
        self._token_type = None
        self._expires_in = None
        self.discriminator = None

        self.access_token = access_token
        if id_token is not None:
            self.id_token = id_token
        if scope is not None:
            self.scope = scope
        self.token_type = token_type
        self.expires_in = expires_in

    @property
    def access_token(self):
        """Gets the access_token of this LoginToken.  # noqa: E501


        :return: The access_token of this LoginToken.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this LoginToken.


        :param access_token: The access_token of this LoginToken.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def id_token(self):
        """Gets the id_token of this LoginToken.  # noqa: E501


        :return: The id_token of this LoginToken.  # noqa: E501
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this LoginToken.


        :param id_token: The id_token of this LoginToken.  # noqa: E501
        :type: str
        """

        self._id_token = id_token

    @property
    def scope(self):
        """Gets the scope of this LoginToken.  # noqa: E501


        :return: The scope of this LoginToken.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this LoginToken.


        :param scope: The scope of this LoginToken.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def token_type(self):
        """Gets the token_type of this LoginToken.  # noqa: E501


        :return: The token_type of this LoginToken.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this LoginToken.


        :param token_type: The token_type of this LoginToken.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token_type is None:  # noqa: E501
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501

        self._token_type = token_type

    @property
    def expires_in(self):
        """Gets the expires_in of this LoginToken.  # noqa: E501


        :return: The expires_in of this LoginToken.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this LoginToken.


        :param expires_in: The expires_in of this LoginToken.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expires_in is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

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
        if not isinstance(other, LoginToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoginToken):
            return True

        return self.to_dict() != other.to_dict()