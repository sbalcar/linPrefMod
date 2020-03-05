#!/usr/bin/python3

import random

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class

from geometry.point import Point #class

from geometry.lineSegments import LineSegments #class
from geometry.lineSegment import LineSegment #class

from userProfileModel.model.prefFnc.model.aPrefFncModel import APrefFncModel #class


class PrefFncCategoricalModel(APrefFncModel):
  # intervals:list<Tuple<float, float>, functionValues:list<float>
  def __init__(self, intervals, functionValues):
     if type(intervals) is not list:
        raise ValueError("Argument intervals isn't type list.")
     for intervalI in intervals:
        if type(intervalI) is not tuple:
           raise ValueError("Argument intervalI isn't type tuple.")
     if type(functionValues) is not list:
        raise ValueError("Argument functionValues isn't type list.")
     for functionValueI in functionValues:
        if type(functionValueI) is not float:
           raise ValueError("Argument functionValueI isn't type float.")
     # intervals:list<Tuple<float, float>>
     self.intervals = intervals;
     # functionValues:list<float>
     self.functionValues = functionValues;

  def toString(self):
     return "PrefFncCategoricalModel(" + str(self.intervals) + ", " + str(self.functionValues) + ")"

  # numberOfCategories:int
  def generate(numberOfCategories):
     if type(numberOfCategories) is not int:
        raise ValueError("Argument numberOfCategories isn't type int.")

     # intervals:float[]
     intervals_ = [random.random() for i in range(numberOfCategories -1)]
     intervals_.sort()
     
     # intervals:list<Tuple<float, float>>
     intervals = [(startIntervalI, endIntervalI) for startIntervalI, endIntervalI in zip([0]+intervals_, intervals_ + [1])]

     # functionValues:float[]
     functionValues = [random.random() for i in range(numberOfCategories)]

     return PrefFncCategoricalModel(intervals, functionValues);

  # linPrefModelConf:LinPrefModelConfiguration
  def exportAsPrefFncX(self, linPrefModelConf):
    # lineSegments:LineSegments
    lineSegments = LineSegments.createFromIntervals(self.intervals, self.functionValues)
    # PrefFncX
    return PrefFncX.createFromLineSegments(lineSegments.lineSegments)


  def exportAsPrefFncY(self, linPrefModelConf):
      # lineSegments:LineSegments
      lineSegments = LineSegments.createFromIntervals(self.intervals, self.functionValues)
      lineSegments = LineSegments([LineSegment(Point(s.point1.y, s.point1.x), Point(s.point2.y, s.point2.x)) for s in lineSegments.lineSegments])
      # pointsRevers:Point[]
      #pointsRevers = [Point(p.y, p.x) for p in lineSegments.exportPoints()]
      # PrefFncY
      #return PrefFncY(pointsRevers)
      return PrefFncY.createFromLineSegments(lineSegments.lineSegments)
