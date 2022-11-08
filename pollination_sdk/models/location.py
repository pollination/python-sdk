# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.32.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Location(object):
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
        'city': 'str',
        'country_code': 'str',
        'country_name': 'str',
        'ip_address': 'str',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'city': 'city',
        'country_code': 'country_code',
        'country_name': 'country_name',
        'ip_address': 'ip_address',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, city=None, country_code=None, country_name=None, ip_address=None, latitude=None, longitude=None, local_vars_configuration=None):  # noqa: E501
        """Location - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._city = None
        self._country_code = None
        self._country_name = None
        self._ip_address = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None

        if city is not None:
            self.city = city
        if country_code is not None:
            self.country_code = country_code
        if country_name is not None:
            self.country_name = country_name
        if ip_address is not None:
            self.ip_address = ip_address
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def city(self):
        """Gets the city of this Location.  # noqa: E501


        :return: The city of this Location.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Location.


        :param city: The city of this Location.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def country_code(self):
        """Gets the country_code of this Location.  # noqa: E501


        :return: The country_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Location.


        :param country_code: The country_code of this Location.  # noqa: E501
        :type country_code: str
        """

        self._country_code = country_code

    @property
    def country_name(self):
        """Gets the country_name of this Location.  # noqa: E501


        :return: The country_name of this Location.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this Location.


        :param country_name: The country_name of this Location.  # noqa: E501
        :type country_name: str
        """

        self._country_name = country_name

    @property
    def ip_address(self):
        """Gets the ip_address of this Location.  # noqa: E501


        :return: The ip_address of this Location.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this Location.


        :param ip_address: The ip_address of this Location.  # noqa: E501
        :type ip_address: str
        """

        self._ip_address = ip_address

    @property
    def latitude(self):
        """Gets the latitude of this Location.  # noqa: E501


        :return: The latitude of this Location.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Location.


        :param latitude: The latitude of this Location.  # noqa: E501
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Location.  # noqa: E501


        :return: The longitude of this Location.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Location.


        :param longitude: The longitude of this Location.  # noqa: E501
        :type longitude: float
        """

        self._longitude = longitude

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
        if not isinstance(other, Location):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Location):
            return True

        return self.to_dict() != other.to_dict()
