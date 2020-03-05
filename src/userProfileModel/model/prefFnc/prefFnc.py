#!/usr/bin/python3

from generator import *
from collections import OrderedDict

from geometry.lineSegment import LineSegment #class
from geometry.lineSegments import LineSegments #class


class PrefFnc:
  # lineSegments:LineSegments
  def __init__(self, lineSegments):
     if type(lineSegments) is not LineSegments:
        raise ValueError("Argument lineSegments isn't type LineSegments.")
     self.lineSegments = lineSegments

  # lineSegments:LineSegment[]
  def constructor(self, lineSegments):
    self.lineSegments = LineSegments(lineSegments);

  def toString(self):
    return self.lineSegments.toString()

  def numberOfIntervals(self):
    return self.lineSegments.size();

  def exportIntervals(self):
    #lineSegments:LineSegments
    return self.lineSegments

  def exportAsPairOfXYCoordinates(self):
    #points:Point[]
    points = self.lineSegments.exportPoints();
    points = list(OrderedDict.fromkeys(points))

    pointsX = [points[i].x for i in range(0, len(points))]
    pointsY = [points[i].y for i in range(0, len(points))]

    # Pair(double[], double[])
    return Pair(pointsX, pointsY)

  # pointX:float
  def functionalValue(self, pointX):
    # intersections:float[]
    intersections = self.lineSegments.intersectionsWithTheAxisParallelToY(pointX);
    # intersectionsValid:float[]
    intersectionsValid = [intersI for intersI in intersections if intersI != None]
    if len(intersectionsValid) == 0:
        return None
    # float
    return intersectionsValid[0];

  # functionalValue:float
  def inverseValue(self, functionalValue):
    # intersections:float[]
    intersections = self.lineSegments.intersectionsWithTheAxisParallelToX(functionalValue);
    # intersections:float[]
    return intersections;


