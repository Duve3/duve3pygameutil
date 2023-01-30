from typing import Union
from math import acos, cos, sin, radians
import math


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    angle = radians(angle)
    ox, oy = origin
    px, py = point

    sinA = sin(angle)
    cosA = cos(angle)

    qx = ox + cosA * (px - ox) - sinA * (py - oy)
    qy = oy + sinA * (px - ox) + cosA * (py - oy)
    return qx, qy


def findAngle(sideLengths: Union[list[int], list[float]], side: str):
    assert len(sideLengths) >= 3, "SIDELENGTHS MUST BE ATLEAST 3 NUMS"
    if side == 'left':
        leftSide = sideLengths[0] ** 2
        bPlusC = sideLengths[1] ** 2 + sideLengths[2] ** 2
        rightSide = 2 * sideLengths[1] * sideLengths[2]
        if bPlusC >= 0:
            leftSide -= bPlusC
        else:
            leftSide += bPlusC

        leftSide /= rightSide

        final = math.degrees(acos(leftSide)) - 60

    elif side == 'right':
        leftSide = sideLengths[2] ** 2
        bPlusC = sideLengths[0] ** 2 + sideLengths[1] ** 2
        rightSide = 2 * sideLengths[0] * sideLengths[1]
        if bPlusC >= 0:
            leftSide -= bPlusC
        else:
            leftSide += bPlusC

        leftSide /= rightSide

        final = math.degrees(acos(leftSide)) - 60
    else:
        leftSide = sideLengths[1] ** 2
        bPlusC = sideLengths[0] ** 2 + sideLengths[2] ** 2
        rightSide = 2 * sideLengths[0] * sideLengths[2]
        if bPlusC >= 0:
            leftSide -= bPlusC
        else:
            leftSide += bPlusC

        leftSide /= rightSide

        final = math.degrees(acos(leftSide)) - 60

    return round(final, 3)
