# coding: utf-8

"""
    pollination.cloud

    Pollination Cloud API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class S3Location(object):
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
        'type': 'str',
        'name': 'str',
        'root': 'str',
        'endpoint': 'str',
        'bucket': 'str',
        'credentials_path': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'root': 'root',
        'endpoint': 'endpoint',
        'bucket': 'bucket',
        'credentials_path': 'credentials_path'
    }

    def __init__(self, type=None, name=None, root='/', endpoint=None, bucket=None, credentials_path=None, local_vars_configuration=None):  # noqa: E501
        """S3Location - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._root = None
        self._endpoint = None
        self._bucket = None
        self._credentials_path = None
        self.discriminator = None

        self.type = type
        self.name = name
        if root is not None:
            self.root = root
        self.endpoint = endpoint
        self.bucket = bucket
        self.credentials_path = credentials_path

    @property
    def type(self):
        """Gets the type of this S3Location.  # noqa: E501


        :return: The type of this S3Location.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this S3Location.


        :param type: The type of this S3Location.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^s3$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^s3$/`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this S3Location.  # noqa: E501

        Name is a unique identifier for this particular Artifact Location  # noqa: E501

        :return: The name of this S3Location.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this S3Location.

        Name is a unique identifier for this particular Artifact Location  # noqa: E501

        :param name: The name of this S3Location.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def root(self):
        """Gets the root of this S3Location.  # noqa: E501

        The path inside the bucket to source artifacts from.  # noqa: E501

        :return: The root of this S3Location.  # noqa: E501
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this S3Location.

        The path inside the bucket to source artifacts from.  # noqa: E501

        :param root: The root of this S3Location.  # noqa: E501
        :type: str
        """

        self._root = root

    @property
    def endpoint(self):
        """Gets the endpoint of this S3Location.  # noqa: E501

        The HTTP endpoint to reach the S3 bucket.  # noqa: E501

        :return: The endpoint of this S3Location.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this S3Location.

        The HTTP endpoint to reach the S3 bucket.  # noqa: E501

        :param endpoint: The endpoint of this S3Location.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501

        self._endpoint = endpoint

    @property
    def bucket(self):
        """Gets the bucket of this S3Location.  # noqa: E501

        The name of the S3 bucket on the host server.  # noqa: E501

        :return: The bucket of this S3Location.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this S3Location.

        The name of the S3 bucket on the host server.  # noqa: E501

        :param bucket: The bucket of this S3Location.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bucket is None:  # noqa: E501
            raise ValueError("Invalid value for `bucket`, must not be `None`")  # noqa: E501

        self._bucket = bucket

    @property
    def credentials_path(self):
        """Gets the credentials_path of this S3Location.  # noqa: E501

        Path to the file holding the AccessKey and SecretAccessKey to authenticate to the bucket  # noqa: E501

        :return: The credentials_path of this S3Location.  # noqa: E501
        :rtype: str
        """
        return self._credentials_path

    @credentials_path.setter
    def credentials_path(self, credentials_path):
        """Sets the credentials_path of this S3Location.

        Path to the file holding the AccessKey and SecretAccessKey to authenticate to the bucket  # noqa: E501

        :param credentials_path: The credentials_path of this S3Location.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and credentials_path is None:  # noqa: E501
            raise ValueError("Invalid value for `credentials_path`, must not be `None`")  # noqa: E501

        self._credentials_path = credentials_path

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
        if not isinstance(other, S3Location):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, S3Location):
            return True

        return self.to_dict() != other.to_dict()
