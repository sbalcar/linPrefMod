#!/usr/bin/python3

from generator import *

from geometry.point import Point # class

from geometry.geometry import getIntersection #function


def getMorphismOfDataPointToPrefPoint(point, prefFncX, prefFncY):
    pointPrefCubeX=getMorphismOfDataPointToPrefFncX(point, prefFncX)
    pointPrefCubeY=getMorphismOfDataPointToPrefFncY(point, prefFncY)

    return Point(pointPrefCubeY.x, pointPrefCubeX.y);


# point:Point(double, double), prefFncX:Point[]
def getMorphismOfDataPointToPrefFncX(point, prefFncX):
    pointX=point.x
    # intervalsX:Pair(Point, Point)[]
    intervalsX=prefFncX.exportAsIntervals()

    # intervalX:Pair(Point, Point)
    for intervalX in intervalsX:
      point1=intervalX.first
      point2=intervalX.second
      if point.isBetweenPointsInTheDirectionX(point1, point2):
         return getIntersection(Pair(point1, point2), Pair(point, Point(point.x, point.y+1)))
    return Point(float('inf'), float('inf'))


# point:Point, prefFncY:Point[]
def getMorphismOfDataPointToPrefFncY(point, prefFncY):
    pointY=point.y
    #intervalsY:Pair(Point, Point)[]
    intervalsY=prefFncY.exportAsIntervals()
    
    # intervalY:Pair(Point, Point)
    for intervalY in intervalsY:
      point1=intervalY.first
      point2=intervalY.second
      if point.isBetweenPointsInTheDirectionY(point1, point2):
         return getIntersection(Pair(point1, point2), Pair(point, Point(point.x+1, point.y)))
    return Point(float('inf'), float('inf'))

# prefPoint:Point, prefFncX:Point[]
def getMorphismOfPrefPointToPrefFncX(prefPoint, prefFncX):
    # intervalsX:Pair(Point, Point)[]
    intervalsX=prefFncX.exportAsIntervals()

    # intersections:Point[]
    intersections = [];
    # intervalY:Pair(Point, Point)
    for intervalX in intervalsX:
      intersectionI = getMorphismOfPrefPointToIntervalOfPrefFncX(prefPoint, intervalX)
      intersections.append(intersectionI);

    # intersections:Point[]
    return intersections

# prefPoint:Point, prefFncY:Point[]
def getMorphismOfPrefPointToPrefFncY(prefPoint, prefFncY):
    # intervalsY:Pair(Point, Point)[]
    intervalsY=prefFncY.exportAsIntervals()

    # intersections:Point[]
    intersections = [];
    # intervalY:Pair(Point, Point)
    for intervalY in intervalsY:
      intersectionI = getMorphismOfPrefPointToIntervalOfPrefFncY(prefPoint, intervalY)
      intersections.append(intersectionI);

    # intersections:Point[]
    return intersections

# prefPoint:Point, intervalOfrefFncX:Pair(Point, Point)
def getMorphismOfPrefPointToIntervalOfPrefFncX(prefPoint, intervalOfrefFncX):
    pointY = prefPoint.y
    point1 = intervalOfrefFncX.first
    point2 = intervalOfrefFncX.second

    # intersection:Point
    intersection = None
    if prefPoint.isBetweenPointsInTheDirectionY(point1, point2):
        # intersection:Point
        intersection = getIntersection(Pair(point1, point2), Pair(prefPoint, Point(prefPoint.x+1, prefPoint.y)))

    # intersection:Point
    return intersection;

# prefPoint:Point, intervalOfrefFncY:Pair(Point, Point)
def getMorphismOfPrefPointToIntervalOfPrefFncY(prefPoint, intervalOfrefFncY):
    pointX = prefPoint.x
    point1 = intervalOfrefFncY.first
    point2 = intervalOfrefFncY.second

    # intersection:Point
    intersection = None;
    if prefPoint.isBetweenPointsInTheDirectionX(point1, point2):
        # intersection:Point
        intersection = getIntersection(Pair(point1, point2), Pair(prefPoint, Point(prefPoint.x, prefPoint.y+1)))

    # intersection:Point
    return intersection



# slope:double, point:Point, beginPrefCubeX:float, beginPrefCubeY:float, endPrefCubeX:float, endPrefCubeY:float
def getMorphismAggregationFncToPrefCube(slope, point, beginPrefCubeX, beginPrefCubeY, endPrefCubeX, endPrefCubeY):
    tangBeta = -slope;

    aX1 = beginPrefCubeX + point.x
    bX1 = aX1 * tangBeta;

    bY1 = endPrefCubeY - point.y;
    aY1 = bY1 / tangBeta;

    aX2 = endPrefCubeX - point.x;
    bX2 = tangBeta * aX2;

    bY2 = point.y - beginPrefCubeY;
    aY2 = bY2 / tangBeta;

    pX1 = Point(beginPrefCubeX, point.y + bX1)
    pY1 = Point(point.x - aY1, endPrefCubeY)
    pX2 = Point(endPrefCubeX, point.y - bX2)
    pY2 = Point(point.x + aY2, beginPrefCubeY)
    # Point[]
    return [pX1, pY1, pX2, pY2];

# points:Point[], beginPrefCubeX:float, beginPrefCubeY:float, endPrefCubeX:float, endPrefCubeY:float
def getMorphismToPrefCube(points, beginPrefCubeX, beginPrefCubeY, endPrefCubeX, endPrefCubeY):
    point1 = Point(beginPrefCubeX, beginPrefCubeY)
    point2 = Point(endPrefCubeX, endPrefCubeY)
    selPoints = []
    for pointI in points:
        if pointI.isBetweenPointsInTheDirectionsXY(point1, point2):
            if pointI not in selPoints:
                selPoints.append(pointI)
    # selPoints:Point[]
    return selPoints;

# prefCubePoint:Point, prefFncX:Point[], prefFncY:Point[]
def getMorphismOfPrefCubePointToDataCubePoint(prefCubePoint, prefFncX, prefFncY):
    pointsOnPrefFncX = getMorphismOfPrefPointToPrefFncX(prefCubePoint, prefFncX);
    pointsOnPrefFncY = getMorphismOfPrefPointToPrefFncY(prefCubePoint, prefFncY);

    points = []
    for pointOnPrefFncXI in pointsOnPrefFncX:
        for pointOnPrefFncYI in pointsOnPrefFncY:
            pointI = Point(pointOnPrefFncXI.x, pointOnPrefFncYI.y);
            if pointI not in points:
                points.append(pointI);
    # points:Point[]
    return points;

