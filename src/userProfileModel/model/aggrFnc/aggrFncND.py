#!/usr/bin/python3

from geometry.pointND import PointND #class


class AggrFncND:
  # weights:float[]
  def __init__(self, weights):
     if type(weights) is not list:
        raise ValueError("Argument weights isn't type list.")
     for weightI in weights:
       if type(weightI) is not float:
          raise ValueError("Argument weights don't contain float.")
     self.weights = weights;

  def toString(self):
     return str(self.weights)

  # pointsInPrefCube:PointND[]
  def preferenceOfPointsInPrefCube(self, pointsInPrefCube):
     if type(pointsInPrefCube) is not list:
        print(type(pointsInPrefCube))
        raise ValueError("Argument pointsInPrefCube isn't type list.")
     for pointI in pointsInPrefCube:
       if type(pointI) is not PointND:
          raise ValueError("Argument pointsInPrefCube don't contain PointND.")

     return [self.preferenceOfPointInPrefCube(pointI) for pointI in pointsInPrefCube]

  # prefPoint:PointND
  def preferenceOfPointInPrefCube(self, prefPoint):
     if type(prefPoint) is not PointND:
        raise ValueError("Argument prefPoint isn't type PointND.")
     if (len(self.weights) != prefPoint.dimension()):
        raise ValueError("Argument prefPoint has wrong dimension.")
     
     pref = 0
     for i in range(len(self.weights)):
       pref += self.weights[i] * prefPoint.exportValues()[i]

     return round(pref, 3)


