#!/usr/bin/python3

from generator import *
from collections import OrderedDict

from geometry.lineSegment import LineSegment #class
from geometry.lineSegments import LineSegments #class


class PrefFncX:
  # points:Point[]
  def __init__(self, points):
      if type(points) is not list :
          raise ValueError("Argument points isn't type list.")
      for pointI in points:
          if type(pointI) is not Point:
              raise ValueError("Argument points don't contain Point.")
      self.lineSegments = LineSegments([LineSegment(points[i], points[i+1]) for i in range(0, len(points)-1)])

  # lineSegments:LineSegment[]
  def createFromLineSegments(lineSegments):
      if type(lineSegments) is not list:
          raise ValueError("Argument lineSegments isn't type list.")
      for lineSegmentI in lineSegments:
          if type(lineSegmentI) is not LineSegment:
              raise ValueError("Argument lineSegmentI don't contain LineSegment.")
      p = PrefFncX([])
      p.lineSegments = LineSegments(lineSegments)
      return p

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

    pointsX=[points[i].x for i in range(0, len(points))]
    pointsY=[points[i].y for i in range(0, len(points))]

    # Pair(double[], double[])
    return Pair(pointsX, pointsY)

  def exportRefractedPrefFncX(self):
    lineSegments = self.exportIntervals();
    # +30 in domain of a function -> +10 in range
    # +50 in domain of a function -> +80 in range
    # +20 in domain of a function -> +10 in range
    segmentation = [Pair(30, 10), Pair(50, 80), Pair(20, 10)]
    # refractedPrefFnc:LineSegment[]
    refractedPrefFnc = []
    for lineSegmI in lineSegments.lineSegments:
        # s:LineSegment[]
        s = []
        if lineSegmI.isDecreasingOnY():
          s = lineSegmI.exportSegmentation(segmentation)
        else:
          s = lineSegmI.exportSegmentation(segmentation[::-1])
        refractedPrefFnc = refractedPrefFnc + s

    return PrefFncX.createFromLineSegments(refractedPrefFnc)

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


class PrefFncY:
 # points:Point[]
  def __init__(self, points):
      if type(points) is not list:
          raise ValueError("Argument points isn't type list.")
      for pointI in points:
          if type(pointI) is not Point:
              raise ValueError("Argument points don't contain Point.")
      self.lineSegments = LineSegments([LineSegment(points[i], points[i+1]) for i in range(0, len(points)-1)])

  # lineSegments:LineSegment[]
  def createFromLineSegments(lineSegments):
      if type(lineSegments) is not list:
          raise ValueError("Argument lineSegments isn't type list.")
      for lineSegmentI in lineSegments:
          if type(lineSegmentI) is not LineSegment:
              raise ValueError("Argument lineSegmentI don't contain LineSegment.")
      p = PrefFncY([])
      p.lineSegments = LineSegments(lineSegments)
      return p

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

      pointsX=[points[i].x for i in range(0, len(points))]
      pointsY=[points[i].y for i in range(0, len(points))]

      # Pair(double[], double[])
      return Pair(pointsX, pointsY)

  def exportRefractedPrefFncY(self):
    lineSegments = self.exportIntervals();
    # +30 in domain of a function -> +10 in range
    # +50 in domain of a function -> +80 in range
    # +20 in domain of a function -> +10 in range
    segmentation = [Pair(10, 30), Pair(80, 50), Pair(10, 20)]
    # refractedPrefFnc:LineSegment[]
    refractedPrefFnc = []
    for lineSegmI in lineSegments.lineSegments:
        # s:LineSegment[]
        s = []
        if lineSegmI.isDecreasingOnX():
          s = lineSegmI.exportSegmentation(segmentation)
        else:
          s = lineSegmI.exportSegmentation(segmentation[::-1])
        refractedPrefFnc = refractedPrefFnc + s

    return PrefFncY.createFromLineSegments(refractedPrefFnc)

 # pointX:float
  def functionalValue(self, pointY):
    # intersections:float[]
    intersections = self.lineSegments.intersectionsWithTheAxisParallelToX(pointY);
    # intersectionsValid:float[]
    intersectionsValid = [intersI for intersI in intersections if intersI != None]
    if len(intersectionsValid) == 0:
        return None
    # float
    return intersectionsValid[0];

  # functionalValue:float
  def inverseValue(self, functionalValue):
    # intersections:float[]
    intersections = self.lineSegments.intersectionsWithTheAxisParallelToY(functionalValue);
    # intersections:float[]
    return intersections;

