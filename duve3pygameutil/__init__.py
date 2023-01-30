# SPDX-FileCopyrightText: 2023-present Duve3 <Duv3tabest@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Union
from math import sqrt

from .timer import Timer
from .constants import *
from .findAngle import findAngle, rotate
from .fontHelper import createFont


class Shape:
    def __init__(self, pointList):
        self.points = pointList


class Triangle(Shape):
    def __init__(self, pointList, sideLengths):
        super().__init__(pointList)
        self._sideLen = sideLengths
        self.angles = []
        self.recalculateAngles(sideLengths=self._sideLen)

    def recalculateAngles(self, *, sideLengths=None):
        if sideLengths is None:
            self._sideLen = self.recalculateSideLengths()
        self.angles = []
        for i in range(3):
            if i == 0:
                cSide = "left"
            elif i == 1:
                cSide = "right"
            else:
                cSide = "top"
            self.angles.append(findAngle(self._sideLen, cSide))

    def recalculateSideLengths(self):
        bottomSideLength = sqrt((self.points[1][0]-self.points[2][0]) ** 2 + (self.points[1][1]-self.points[2][1]) ** 2)
        leftSideLength = sqrt((self.points[0][0]-self.points[2][0]) ** 2 + (self.points[0][1]-self.points[2][1]) ** 2)
        rightSideLength = sqrt((self.points[0][0]-self.points[1][0]) ** 2 + (self.points[0][1]-self.points[1][1]) ** 2)
        return [rightSideLength, leftSideLength, bottomSideLength]


def createTriangle(TopPoint: Union[Union[tuple[int, int], tuple[float, float]], Union[list[int], list[float]]], leftSideLength: Union[float, int], rightSideLength: Union[float, int]):  # NOQA:E501
    """
    Creates a triangle using a top point and 2 side lengths.
    :param TopPoint: The top point of the triangle.
    :param leftSideLength: The length of the left side of the triangle
    :param rightSideLength: The length of the right side of the triangle
    :return: A Triangle object which contains a .points variable which has all the points of a triangle.
    """
    bottomLeftPoint = [TopPoint[0] - leftSideLength/2, TopPoint[1] + leftSideLength/2]
    bottomRightPoint = [TopPoint[0] - rightSideLength/2, TopPoint[1] - rightSideLength/2]
    bottomLeftPoint = rotate(TopPoint, bottomLeftPoint, -90)
    bottomRightPoint = rotate(TopPoint, bottomRightPoint, -90)
    bottomSideLength = sqrt((bottomRightPoint[0]-bottomLeftPoint[0])**2 + (bottomRightPoint[1]-bottomLeftPoint[1])**2)
    return Triangle([TopPoint, bottomRightPoint, bottomLeftPoint], [rightSideLength, leftSideLength, bottomSideLength])
