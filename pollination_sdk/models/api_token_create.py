# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class APITokenCreate(object):
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
        'claims': 'dict(str, str)',
        'name': 'str',
        'token_id': 'str'
    }

    attribute_map = {
        'claims': 'claims',
        'name': 'name',
        'token_id': 'token_id'
    }

    def __init__(self, claims=None, name=None, token_id=None, local_vars_configuration=None):  # noqa: E501
        """APITokenCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._claims = None
        self._name = None
        self._token_id = None
        self.discriminator = None

        if claims is not None:
            self.claims = claims
        self.name = name
        self.token_id = token_id

    @property
    def claims(self):
        """Gets the claims of this APITokenCreate.  # noqa: E501

        Key value pairs of auth claims the API token is entitled to  # noqa: E501

        :return: The claims of this APITokenCreate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._claims

    @claims.setter
    def claims(self, claims):
        """Sets the claims of this APITokenCreate.

        Key value pairs of auth claims the API token is entitled to  # noqa: E501

        :param claims: The claims of this APITokenCreate.  # noqa: E501
        :type claims: dict(str, str)
        """

        self._claims = claims

    @property
    def name(self):
        """Gets the name of this APITokenCreate.  # noqa: E501

        The user friendly name of the API token  # noqa: E501

        :return: The name of this APITokenCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this APITokenCreate.

        The user friendly name of the API token  # noqa: E501

        :param name: The name of this APITokenCreate.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def token_id(self):
        """Gets the token_id of this APITokenCreate.  # noqa: E501

        The unique ID of this API token  # noqa: E501

        :return: The token_id of this APITokenCreate.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this APITokenCreate.

        The unique ID of this API token  # noqa: E501

        :param token_id: The token_id of this APITokenCreate.  # noqa: E501
        :type token_id: str
        """
        if self.local_vars_configuration.client_side_validation and token_id is None:  # noqa: E501
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

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
        if not isinstance(other, APITokenCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APITokenCreate):
            return True

        return self.to_dict() != other.to_dict()
