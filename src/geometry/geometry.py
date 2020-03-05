#!/usr/bin/python3

import numpy as np

import math

from geometry.point import Point # class


# line1:Pair(Point, Point), line2:Pair(Point, Point)
def getIntersection(line1, line2):
    a1 = [line1.first.x, line1.first.y, 1]
    a2 = [line1.second.x, line1.second.y, 1]
    b1 = [line2.first.x, line2.first.y, 1]
    b2 = [line2.second.x, line2.second.y, 1]
    lineA = np.cross(a1, a2)
    lineB = np.cross(b1, b2)
    x, y, z = np.cross(lineA, lineB)
    if z == 0:  # parallel lines
        return Point(float('inf'), float('inf'))
    return Point(x/z, y/z)

# line:Pair(Point, Point)
def getSizeOfLine(line):
    point1 = line.first;
    point2 = line.second;
    size = math.sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2))
    # float
    return size;
