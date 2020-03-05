0#!/usr/bin/python3

from generator import *

from geometry.lineSegment import LineSegment #class
from geometry.point import Point #class

class LineSegments:
  # lineSegments:LineSegment[]
  def __init__(self, lineSegments):
    if type(lineSegments) is not list:
        raise ValueError("Argument lineSegments isn't type list.")
    for lineSegmentI in lineSegments:
      if type(lineSegmentI) is not LineSegment:
         raise ValueError("Argument lineSegments don't contain LineSegment.")
    self.lineSegments = lineSegments

  # intervals:list<Tuple<float, float>>, functionValues:list<float>
  @staticmethod
  def createFromIntervals(intervals, functionValues):
    if len(intervals) != len(functionValues):
        raise ValueError("Argument functionValues don't dont have correct length.")

    # List<LineSegment>
    lineSegments = []
    # intervalI:Tuple<float, float>, fncValueI:float
    for intervalI, fncValueI in zip(intervals, functionValues):
        p1 = Point(intervalI[0], fncValueI)
        p2 = Point(intervalI[1], fncValueI)
        lineSegments.append(LineSegment(p1, p2))
    return LineSegments(lineSegments);

  # points:list<Point>
  @staticmethod
  def createPointToPoint(points):
    # List<LineSegment>
    lineSegments = [LineSegment(points[i], points[i+1]) for i in range(0, len(points)-1)]
    return LineSegments(lineSegments);

  def clone(self):
      lineSegmentsClone = []
      for lineSegmentI in self.lineSegments:
          lineSegmentsClone.append(lineSegmentI.clone())
      return LineSegments(lineSegmentsClone)

  def size(self):
    return len(self.lineSegments);

  def printLineSegments(self):
    print("LineSegments:")
    for lineSegmentI in self.lineSegments:
        lineSegmentI.printLineSegment();

  def toString(self):
    string = "("
    for lineSegmentI in self.lineSegments:
        string += lineSegmentI.toString() + ", "
    return string[:-2] + ")"

  # valueX:float[]
  def intersectionsWithTheAxisParallelToY(self, valueX):
      intersections = []
      for lineSegmentI in self.lineSegments:
         intersI = lineSegmentI.intersectionWithTheAxisParallelToY(valueX);
         intersections.append(intersI);
      return intersections;

  # valueY:float[]
  def intersectionsWithTheAxisParallelToX(self, valueY):
      intersections = []
      for lineSegmentI in self.lineSegments:
         intersI = lineSegmentI.intersectionWithTheAxisParallelToX(valueY);
         intersections.append(intersI);
      return intersections;

  def exportPoints(self):
      #points:Point[]
      points = []
      for lineSegmentI in self.lineSegments:
          points.append(lineSegmentI.point1)
          points.append(lineSegmentI.point2)
      #points:Point[]
      return points;

  # valueX:float
  def lineSegmentsWhichIntersectAxisParallelToY(self, valueX):
      for lineSegmentI in self.lineSegments:
          if lineSegmentI.intersectionWithTheAxisParallelToY(valueX) is not None:
              return lineSegmentI
      return None

  # valueX:float
  def lineSegmentsWhichDontIntersectAxisParallelToY(self, valueX):
      selectedLineSegments = []
      for lineSegmentI in self.lineSegments:
          if lineSegmentI.intersectionWithTheAxisParallelToY(valueX) is None:
              selectedLineSegments.append(lineSegmentI)
      return selectedLineSegments

  # point:Point
  def replacePointByPoint(self, point, pointNew):
      for lineSegmentI in self.lineSegments:
          if lineSegmentI.point1 == point:
              lineSegmentI.point1 = pointNew
          if lineSegmentI.point2 == point:
              lineSegmentI.point2 = pointNew
