# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class CreativeportfoliocreateBadgePosition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'angle': 'int',
        'position_x': 'float',
        'position_y': 'float'
    }

    attribute_map = {
        'angle': 'angle',
        'position_x': 'position_x',
        'position_y': 'position_y'
    }

    def __init__(self, angle=None, position_x=None, position_y=None):  # noqa: E501
        """CreativeportfoliocreateBadgePosition - a model defined in Swagger"""  # noqa: E501
        self._angle = None
        self._position_x = None
        self._position_y = None
        self.discriminator = None
        if angle is not None:
            self.angle = angle
        if position_x is not None:
            self.position_x = position_x
        if position_y is not None:
            self.position_y = position_y

    @property
    def angle(self):
        """Gets the angle of this CreativeportfoliocreateBadgePosition.  # noqa: E501


        :return: The angle of this CreativeportfoliocreateBadgePosition.  # noqa: E501
        :rtype: int
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this CreativeportfoliocreateBadgePosition.


        :param angle: The angle of this CreativeportfoliocreateBadgePosition.  # noqa: E501
        :type: int
        """

        self._angle = angle

    @property
    def position_x(self):
        """Gets the position_x of this CreativeportfoliocreateBadgePosition.  # noqa: E501


        :return: The position_x of this CreativeportfoliocreateBadgePosition.  # noqa: E501
        :rtype: float
        """
        return self._position_x

    @position_x.setter
    def position_x(self, position_x):
        """Sets the position_x of this CreativeportfoliocreateBadgePosition.


        :param position_x: The position_x of this CreativeportfoliocreateBadgePosition.  # noqa: E501
        :type: float
        """

        self._position_x = position_x

    @property
    def position_y(self):
        """Gets the position_y of this CreativeportfoliocreateBadgePosition.  # noqa: E501


        :return: The position_y of this CreativeportfoliocreateBadgePosition.  # noqa: E501
        :rtype: float
        """
        return self._position_y

    @position_y.setter
    def position_y(self, position_y):
        """Sets the position_y of this CreativeportfoliocreateBadgePosition.


        :param position_y: The position_y of this CreativeportfoliocreateBadgePosition.  # noqa: E501
        :type: float
        """

        self._position_y = position_y

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CreativeportfoliocreateBadgePosition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreativeportfoliocreateBadgePosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
