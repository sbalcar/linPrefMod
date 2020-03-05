#!/usr/bin/python3

import random

from geometry.point import Point #class

from userProfileModel.model.prefFnc.model.aPrefFncModel import APrefFncModel #class

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class


class PrefFncTroughModel(APrefFncModel):
  # iCoordinates:float
  def __init__(self, iCoordinate, bottom):
     if type(iCoordinate) is not float:
        raise ValueError("Argument iCoordinate isn't type float.")
     self.iCoordinate = iCoordinate;
     if type(bottom) is not float:
        raise ValueError("Argument bottom isn't type float.")
     self.bottom = bottom

  def toString(self):
     return str(self.iCoordinate)

  def generate():
     iCoordinate = random.random()
     return PrefFncTroughModel(iCoordinate);

  # linPrefModelConf:LinPrefModelConfiguration
  def exportAsPrefFncX(self, linPrefModelConf):
      return PrefFncX([Point(0, 0), Point(self.iCoordinate -self.bottom/2, 1), Point(self.iCoordinate +self.bottom/2, 1), Point(linPrefModelConf.SIZE_X_DATA_CUBE, 0)])

  # linPrefModelConf:LinPrefModelConfiguration
  def exportAsPrefFncY(self, linPrefModelConf):
      return PrefFncY([Point(0, 0), Point(1, self.iCoordinate -self.bottom/2), Point(1, self.iCoordinate +self.bottom/2), Point(0, linPrefModelConf.SIZE_Y_DATA_CUBE)])
