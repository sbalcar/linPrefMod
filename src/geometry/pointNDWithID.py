#!/usr/bin/python3

from generator import *

from collections import namedtuple #pair

from geometry.point import Point #class
from geometry.pointND import PointND #class
from geometry.pointWithID import PointWithID #class

import sys

class PointNDWithID:
  # point:PointND, pointID:String
  def __init__(self, pointND, pointID):
    if type(pointND) is not PointND:
       raise ValueError("Argument point isn't type PointND.")
    self.pointID = pointID
    self.point = pointND

  def clone(self):
      return PointNDWithID(self.point.clone(), self.pointID);

  def __eq__(self, other):
    if other is not PointNDWithID:
        return False;
    return self.coordinates == other.coordinates and self.pointID == other.pointID

  def __hash__(self):
     values = [str(cI) + ", " for cI in exportValues()]
     string = str(self.pointID)
     valueToHash = string.join(values)[:-2]
     return hash(valueToHash)

  def dimension(self):
     return self.point.dimension();

  # dimensionX:int, dimensionY:int
  def exportPointWithID(self, dimensionX, dimensionY):
     point = self.point.exportAsPoint(dimensionX, dimensionY)
     return PointWithID(point, self.pointID)

  def exportAsList(self):
    # float[]
    return [self.pointID] + self.point.exportValues();

  def printPointWithID(self):
      print("PointWithID: ", self.pointID, " ", self.exportAsList())

