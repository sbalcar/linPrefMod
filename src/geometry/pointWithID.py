#!/usr/bin/python3

from generator import *

from collections import namedtuple #pair

from geometry.point import Point #class

import sys

class PointWithID:
  # point:Point, pointID:String
  def __init__(self, point, pointID):
    if type(point) is not Point:
       raise ValueError("Argument point isn't type Point.")
    self.point = point
    self.pointID = pointID

  def clone(self):
      return PointWithID(self.point.clone(), self.pointID);

  def __eq__(self, other):
    if other is not PointWithID:
        return False;
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash(('x', self.x,
                 'y', self.y))
 
  def printPointWithID(self):
      print("PointWithID: ", self.point.x, " ", self.point.y, " ", self.pointID)

