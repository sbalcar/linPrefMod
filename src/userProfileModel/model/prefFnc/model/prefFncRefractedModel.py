#!/usr/bin/python3

from typing import List

import random
from generator import *

from geometry.point import Point #class

from geometry.lineSegment import LineSegment #class
from geometry.lineSegments import LineSegments #class

from userProfileModel.model.prefFnc.model.aPrefFncModel import APrefFncModel #class

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class


class PrefFncRefractedModel(APrefFncModel):
  # iCoordinates:float
  def __init__(self, iCoordinate):
     if type(iCoordinate) is not float:
        raise ValueError("Argument iCoordinate isn't type float.")
     self.iCoordinate = iCoordinate;

  def toString(self):
     return "PrefFncRefractedModel(" + str(self.iCoordinate) + ")"

  def generate(args):
     iCoordinate = random.random()

     return PrefFncRefractedModel(iCoordinate)

  # linPrefModelConf:LinPrefModelConfiguration
  def exportAsPrefFncX(self, linPrefModelConf):

     # points:List<Point>
     points = [Point(0, 0), Point(self.iCoordinate, 1), Point(linPrefModelConf.SIZE_X_DATA_CUBE, 0)]

     # lineSegments:LineSegments
     lineSegments = LineSegments([LineSegment(points[i].clone(), points[i+1].clone()) for i in range(0, len(points)-1)])

     # +30 in domain of a function -> +10 in range
     # +50 in domain of a function -> +80 in range
     # +20 in domain of a function -> +10 in range
     segmentation = [Pair(30, 10), Pair(50, 80), Pair(20, 10)]
     # refractedPrefFnc:LineSegment[]
     refractedPrefFnc:List[LineSegment] = []
     for lineSegmI in lineSegments.lineSegments:
        # s:LineSegment[]
        s = []
        if lineSegmI.isDecreasingOnY():
          s = lineSegmI.exportSegmentation(segmentation)
        else:
          s = lineSegmI.exportSegmentation(segmentation[::-1])
        refractedPrefFnc = refractedPrefFnc + s

     return PrefFncX.createFromLineSegments(refractedPrefFnc)

  # linPrefModelConf:LinPrefModelConfiguration
  def exportAsPrefFncY(self, linPrefModelConf):

      # points:List<Point>
      points = [Point(0, 0), Point(1, self.iCoordinate), Point(0, linPrefModelConf.SIZE_Y_DATA_CUBE)]

      # lineSegments:LineSegments
      lineSegments = LineSegments([LineSegment(points[i], points[i + 1]) for i in range(0, len(points) - 1)])

      # +30 in domain of a function -> +10 in range
      # +50 in domain of a function -> +80 in range
      # +20 in domain of a function -> +10 in range
      segmentation = [Pair(10, 30), Pair(80, 50), Pair(10, 20)]
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

      return PrefFncY.createFromLineSegments(refractedPrefFnc)

