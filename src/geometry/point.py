#!/usr/bin/python3

import math
from generator import *

from collections import namedtuple #pair

#from graphicalModel import * #class Pair

import sys

class Point:
  # x:float, y:float
  def __init__(self, x, y):
      if type(x) is not float and type(x) is not int:
          raise ValueError("Argument x isn't type float/int.")
      if type(y) is not float and type(y) is not int:
          raise ValueError("Argument y isn't type float/int.")
      self.x = round(x, 5)
      self.y = round(y, 5)

  # values:list<float>
  @staticmethod
  def create(values):
      if type(values) is not list:
          raise ValueError("Argument values isn't type list.")
      if len(values) != 2:
          raise ValueError("Argument values dont't have dimension 2.")
      return Point(values[0], values[1])

  def clone(self):
      return Point(self.x, self.y);

  def __eq__(self, other):
    if other == None:
        return False;
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash(('x', self.x,
                 'y', self.y))
    
  def exportValues(self):
    return [self.x, self.y];

  def dimension(self):
    return 2;

  # point:Point
  def distance(self, point):
      xd = abs(self.x - point.x)
      yd = abs(self.y - point.y)

      return math.sqrt(xd*xd + yd*yd)

      # point1:Point, point2:Point
  def isBetweenPointsInTheDirectionsXY(self, point1, point2):
    return self.isBetweenPointsInTheDirectionX(point1, point2
            ) and self.isBetweenPointsInTheDirectionY(point1, point2);

  # point1:Point, point2:Point
  def isBetweenPointsInTheDirectionX(self, point1, point2):
    if (point1.x <= self.x and self.x <= point2.x):
        return True;
    if (point2.x <= self.x and self.x <= point1.x):
        return True;
    return False;

  # point1:Point, point2:Point
  def isBetweenPointsInTheDirectionY(self, point1, point2):
    if (point1.y <= self.y and self.y <= point2.y):
        return True;
    if (point2.y <= self.y and self.y <= point1.y):
        return True;
    return False;

  def printPoint(self):
      print("Point: ", self.x, " ", self.y)

