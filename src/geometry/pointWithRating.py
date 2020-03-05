#!/usr/bin/python3

from generator import *

from collections import namedtuple #pair

from geometry.point import Point #class

import sys

class PointWithRating:
  # point:Point, rating:float
  def __init__(self, point, rating):
    if type(point) is not Point:
       raise ValueError("Argument point isn't type Point.")
    self.point = point
    self.rating = rating

  def clone(self):
      return PointWithRating(self.point.clone(), self.rating);

  def __eq__(self, other):
    if other is not PointWithRating:
        return False;
    return self.x == other.x and self.y == other.y and self.rating == other.rating

  def __hash__(self):
    return hash(('x', self.x,
                 'y', self.y,
                 'rating', self.rating))
    
  def printPointWithRating(self):
      print("PointWithRating: ", self.point.x, " ", self.point.y, " Rating: ", self.rating)

