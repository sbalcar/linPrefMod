#!/usr/bin/python3

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class

from geometry.point import Point #class
from geometry.points import Points #class

from userProfileModel.model.prefFnc.model.aPrefFncModel import APrefFncModel #class


class PrefFncPointSequenceModel(APrefFncModel):
  # points:Point[]
  def __init__(self, points):
     #print("PrefFncPointSequenceModel: " + Points(points).exportAsString())
     if type(points) is not list:
        raise ValueError("Argument points isn't type list.")
     for pointI in points:
         if type(pointI) is not Point:
             raise ValueError("Argument points dont't contains Point.")
     self.points = points;

  def toString(self):
      pointsC = Points(self.points)
      return "PrefFncPointSequenceModel(" + pointsC.exportAsString() + ")"

  def generate(args):
     #iCoordinate = random.random()
     #return PrefFncPointSequenceModel(iCoordinate);
     return None

  # linPrefModelConf:LinPrefModelConfiguration
  def exportAsPrefFncX(self, linPrefModelConf):
    # PrefFncX
    return PrefFncX(self.points)


  # linPrefModelConf:LinPrefModelConfiguration
  def exportAsPrefFncY(self, linPrefModelConf):
      # pointsRevers:Point[]
      pointsRevers = [Point(p.y, p.x) for p in self.points]
      # PrefFncX
      return PrefFncY(pointsRevers)
