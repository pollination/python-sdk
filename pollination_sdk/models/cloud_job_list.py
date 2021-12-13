# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: v0.20.0
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class CloudJobList(object):
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
        'next_page': 'int',
        'page': 'int',
        'page_count': 'int',
        'per_page': 'int',
        'resources': 'list[CloudJob]',
        'total_count': 'int'
    }

    attribute_map = {
        'next_page': 'next_page',
        'page': 'page',
        'page_count': 'page_count',
        'per_page': 'per_page',
        'resources': 'resources',
        'total_count': 'total_count'
    }

    def __init__(self, next_page=None, page=None, page_count=None, per_page=None, resources=None, total_count=None, local_vars_configuration=None):  # noqa: E501
        """CloudJobList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._next_page = None
        self._page = None
        self._page_count = None
        self._per_page = None
        self._resources = None
        self._total_count = None
        self.discriminator = None

        if next_page is not None:
            self.next_page = next_page
        self.page = page
        self.page_count = page_count
        self.per_page = per_page
        self.resources = resources
        self.total_count = total_count

    @property
    def next_page(self):
        """Gets the next_page of this CloudJobList.  # noqa: E501

        The next page, if this on is not the last  # noqa: E501

        :return: The next_page of this CloudJobList.  # noqa: E501
        :rtype: int
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this CloudJobList.

        The next page, if this on is not the last  # noqa: E501

        :param next_page: The next_page of this CloudJobList.  # noqa: E501
        :type next_page: int
        """

        self._next_page = next_page

    @property
    def page(self):
        """Gets the page of this CloudJobList.  # noqa: E501

        The current page the pagination request is on  # noqa: E501

        :return: The page of this CloudJobList.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this CloudJobList.

        The current page the pagination request is on  # noqa: E501

        :param page: The page of this CloudJobList.  # noqa: E501
        :type page: int
        """
        if self.local_vars_configuration.client_side_validation and page is None:  # noqa: E501
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def page_count(self):
        """Gets the page_count of this CloudJobList.  # noqa: E501

        The total number of pages  # noqa: E501

        :return: The page_count of this CloudJobList.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this CloudJobList.

        The total number of pages  # noqa: E501

        :param page_count: The page_count of this CloudJobList.  # noqa: E501
        :type page_count: int
        """
        if self.local_vars_configuration.client_side_validation and page_count is None:  # noqa: E501
            raise ValueError("Invalid value for `page_count`, must not be `None`")  # noqa: E501

        self._page_count = page_count

    @property
    def per_page(self):
        """Gets the per_page of this CloudJobList.  # noqa: E501

        The number of pages per pagination request  # noqa: E501

        :return: The per_page of this CloudJobList.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this CloudJobList.

        The number of pages per pagination request  # noqa: E501

        :param per_page: The per_page of this CloudJobList.  # noqa: E501
        :type per_page: int
        """
        if self.local_vars_configuration.client_side_validation and per_page is None:  # noqa: E501
            raise ValueError("Invalid value for `per_page`, must not be `None`")  # noqa: E501

        self._per_page = per_page

    @property
    def resources(self):
        """Gets the resources of this CloudJobList.  # noqa: E501


        :return: The resources of this CloudJobList.  # noqa: E501
        :rtype: list[CloudJob]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this CloudJobList.


        :param resources: The resources of this CloudJobList.  # noqa: E501
        :type resources: list[CloudJob]
        """
        if self.local_vars_configuration.client_side_validation and resources is None:  # noqa: E501
            raise ValueError("Invalid value for `resources`, must not be `None`")  # noqa: E501

        self._resources = resources

    @property
    def total_count(self):
        """Gets the total_count of this CloudJobList.  # noqa: E501

        The total number of resources matching the list request  # noqa: E501

        :return: The total_count of this CloudJobList.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this CloudJobList.

        The total number of resources matching the list request  # noqa: E501

        :param total_count: The total_count of this CloudJobList.  # noqa: E501
        :type total_count: int
        """
        if self.local_vars_configuration.client_side_validation and total_count is None:  # noqa: E501
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

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
        if not isinstance(other, CloudJobList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudJobList):
            return True

        return self.to_dict() != other.to_dict()
