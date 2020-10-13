# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class SimulationOutputSource(object):
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
        'output': 'str',
        'path': 'str',
        'simulation': 'str',
        'type': 'str'
    }

    attribute_map = {
        'output': 'output',
        'path': 'path',
        'simulation': 'simulation',
        'type': 'type'
    }

    def __init__(self, output=None, path=None, simulation=None, type='simulation', local_vars_configuration=None):  # noqa: E501
        """SimulationOutputSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._output = None
        self._path = None
        self._simulation = None
        self._type = None
        self.discriminator = None

        if output is not None:
            self.output = output
        if path is not None:
            self.path = path
        self.simulation = simulation
        if type is not None:
            self.type = type

    @property
    def output(self):
        """Gets the output of this SimulationOutputSource.  # noqa: E501

        Simulation output artifact name  # noqa: E501

        :return: The output of this SimulationOutputSource.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this SimulationOutputSource.

        Simulation output artifact name  # noqa: E501

        :param output: The output of this SimulationOutputSource.  # noqa: E501
        :type output: str
        """

        self._output = output

    @property
    def path(self):
        """Gets the path of this SimulationOutputSource.  # noqa: E501

        The path within the simulation outputs folder to a specified artifact  # noqa: E501

        :return: The path of this SimulationOutputSource.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SimulationOutputSource.

        The path within the simulation outputs folder to a specified artifact  # noqa: E501

        :param path: The path of this SimulationOutputSource.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def simulation(self):
        """Gets the simulation of this SimulationOutputSource.  # noqa: E501

        Simulation ID  # noqa: E501

        :return: The simulation of this SimulationOutputSource.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this SimulationOutputSource.

        Simulation ID  # noqa: E501

        :param simulation: The simulation of this SimulationOutputSource.  # noqa: E501
        :type simulation: str
        """
        if self.local_vars_configuration.client_side_validation and simulation is None:  # noqa: E501
            raise ValueError("Invalid value for `simulation`, must not be `None`")  # noqa: E501

        self._simulation = simulation

    @property
    def type(self):
        """Gets the type of this SimulationOutputSource.  # noqa: E501


        :return: The type of this SimulationOutputSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimulationOutputSource.


        :param type: The type of this SimulationOutputSource.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^simulation$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^simulation$/`")  # noqa: E501

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
        if not isinstance(other, SimulationOutputSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationOutputSource):
            return True

        return self.to_dict() != other.to_dict()
