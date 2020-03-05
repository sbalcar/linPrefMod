#!/usr/bin/python3

from generator import *
import random

from collections import namedtuple #pair

import sys

class PointND:
  # coordinates:float[]
  def __init__(self, coordinates):
     if type(coordinates) is not list:
        raise ValueError("Argument iCoordinates isn't type list.")
     for coordinateI in coordinates:
       if type(coordinateI) is not float:
          raise ValueError("Argument iCoordinates don't contain float.")
     self.coordinates = coordinates

  def clone(self):
     return PointND(List(self.coordinates));

  def __eq__(self, other):
     if other != PointND:
        return False;
     return self.coordinates == other.coordinates

  def __hash__(self):
     values = [str(cI) + ", " for cI in exportValues()]
     string = ""
     valueToHash = string.join(values)[:-2]
     return hash(valueToHash)

  # dimension:int
  def generate(dimension):
     # coordinates:float
     coordinates = []
     for dimensionI in range(dimension):
       coordinates.append(random.random())
     return PointND(coordinates);

  # numberOfNeighbours:int, radiusOfCircle:float
  def generateNeighbours(self, numberOfNeighbours, radiusOfCircle):
      # PointND[]
      return [self.generateNeighbour(radiusOfCircle) for i in range(numberOfNeighbours)]

  # radiusOfCircle:float
  def generateNeighbour(self, radiusOfCircle):
     # PointND
     point = PointND([c + random.uniform(-radiusOfCircle/2, radiusOfCircle/2) for c in self.coordinates])
     point.__corect();
     return point;

  def __corect(self):
    for coorIndex in range(len(self.coordinates)):
       if self.coordinates[coorIndex] < 0:
           self.coordinates[coorIndex] *= -1
       if self.coordinates[coorIndex] > 1:
           self.coordinates[coorIndex] = 2 - self.coordinates[coorIndex]

  # dimensionX:int, dimensionY:int
  def exportAsPoint(self, dimensionX, dimensionY):
     return Point(self.coordinates[dimensionX], self.coordinates[dimensionY])

  def exportValues(self):
     # float[]
     return self.coordinates

  def dimension(self):
     return len(self.coordinates);

  def printPoint(self):
     print("Point: ", self.coordinates)


