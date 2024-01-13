# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class S3(object):
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
        'annotations': 'dict(str, str)',
        'bucket': 'str',
        'credentials_path': 'str',
        'endpoint': 'str',
        'key': 'str',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'bucket': 'bucket',
        'credentials_path': 'credentials_path',
        'endpoint': 'endpoint',
        'key': 'key',
        'type': 'type'
    }

    def __init__(self, annotations=None, bucket=None, credentials_path=None, endpoint=None, key=None, type='S3', local_vars_configuration=None):  # noqa: E501
        """S3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._bucket = None
        self._credentials_path = None
        self._endpoint = None
        self._key = None
        self._type = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        self.bucket = bucket
        if credentials_path is not None:
            self.credentials_path = credentials_path
        self.endpoint = endpoint
        self.key = key
        if type is not None:
            self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this S3.  # noqa: E501

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :return: The annotations of this S3.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this S3.

        An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries.  # noqa: E501

        :param annotations: The annotations of this S3.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def bucket(self):
        """Gets the bucket of this S3.  # noqa: E501

        The name of the S3 bucket on the host server.  # noqa: E501

        :return: The bucket of this S3.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this S3.

        The name of the S3 bucket on the host server.  # noqa: E501

        :param bucket: The bucket of this S3.  # noqa: E501
        :type bucket: str
        """
        if self.local_vars_configuration.client_side_validation and bucket is None:  # noqa: E501
            raise ValueError("Invalid value for `bucket`, must not be `None`")  # noqa: E501

        self._bucket = bucket

    @property
    def credentials_path(self):
        """Gets the credentials_path of this S3.  # noqa: E501

        Path to the file holding the AccessKey and SecretAccessKey to authenticate to the bucket. Assumes public bucket access if none are specified.  # noqa: E501

        :return: The credentials_path of this S3.  # noqa: E501
        :rtype: str
        """
        return self._credentials_path

    @credentials_path.setter
    def credentials_path(self, credentials_path):
        """Sets the credentials_path of this S3.

        Path to the file holding the AccessKey and SecretAccessKey to authenticate to the bucket. Assumes public bucket access if none are specified.  # noqa: E501

        :param credentials_path: The credentials_path of this S3.  # noqa: E501
        :type credentials_path: str
        """

        self._credentials_path = credentials_path

    @property
    def endpoint(self):
        """Gets the endpoint of this S3.  # noqa: E501

        The HTTP endpoint to reach the S3 bucket.  # noqa: E501

        :return: The endpoint of this S3.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this S3.

        The HTTP endpoint to reach the S3 bucket.  # noqa: E501

        :param endpoint: The endpoint of this S3.  # noqa: E501
        :type endpoint: str
        """
        if self.local_vars_configuration.client_side_validation and endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501

        self._endpoint = endpoint

    @property
    def key(self):
        """Gets the key of this S3.  # noqa: E501

        The path inside the bucket to source artifacts from.  # noqa: E501

        :return: The key of this S3.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this S3.

        The path inside the bucket to source artifacts from.  # noqa: E501

        :param key: The key of this S3.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def type(self):
        """Gets the type of this S3.  # noqa: E501


        :return: The type of this S3.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this S3.


        :param type: The type of this S3.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^S3$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^S3$/`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, S3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, S3):
            return True

        return self.to_dict() != other.to_dict()
