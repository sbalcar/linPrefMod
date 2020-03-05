#!/usr/bin/python3

import random

from geometry.point import Point #class

from userProfileModel.model.prefFnc.model.aPrefFncModel import APrefFncModel #class

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class


class PrefFncTriangularModel(APrefFncModel): 
  # iCoordinates:float
  def __init__(self, iCoordinate):
     if type(iCoordinate) is not float:
        raise ValueError("Argument iCoordinate isn't type float.")
     self.iCoordinate = iCoordinate;

  def toString(self):
     return "PrefFncTriangularModel(" + str(self.iCoordinate) + ")"

  def generate(args):
     iCoordinate = random.random()
     return PrefFncTriangularModel(iCoordinate)


  # linPrefModelConf:LinPrefModelConfiguration
  def exportAsPrefFncX(self, linPrefModelConf):
    # points:List<Point>
    points = [Point(0, 0), Point(self.iCoordinate, 1), Point(linPrefModelConf.SIZE_X_DATA_CUBE, 0)]
    # PrefFnc
    return PrefFncX(points)


  # linPrefModelConf:LinPrefModelConfiguration
  def exportAsPrefFncY(self, linPrefModelConf):
    # points:List<Point>
    points = [Point(0, 0), Point(1, self.iCoordinate), Point(0, linPrefModelConf.SIZE_Y_DATA_CUBE)]
    # PrefFnc
    return PrefFncY(points)

