#!/usr/bin/python3

from geometry.point import Point # class

from geometry.geometry import getIntersection # function
from geometry.points import Points # function

from shapely.geometry import Polygon

# points:Point[]
def countPolygonSurfaceArea_(points):
    p = Points(points)

    #countIntersection();

    n = len(points)
    X = p[0]
    Y = p[1]

    area = 0.0

    j = n - 1
    for i in range(0, n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i
    
    # float
    return abs(area / 2.0)

# points:Point[]
def countPolygonSurfaceArea(points):
    #for pI in points:
    #    pI.printPoint();

    pointsPair = Polygon([(pI.x, pI.y) for pI in points]);
   
    if not pointsPair.is_valid:
        print("ble")

    surface = pointsPair.area;

    # surface:float
    return surface


# points1:Point[], points2:Point[]
def countIntersection(points1, points2):
    #for pointI in points1:
    #    pointI.printPoint()
    
    #for pointI in points2:
    #    pointI.printPoint()

    pointsPair1 = Polygon([(pI.x, pI.y) for pI in points1]);
    pointsPair2 = Polygon([(pI.x, pI.y) for pI in points2]);

    if not pointsPair1.is_valid:
        print("ble")
    if not pointsPair2.is_valid:
        print("ble")

    pointsPair3 = pointsPair1.intersection(pointsPair2);
    surface = pointsPair3.area;

    # surface:float
    return surface
