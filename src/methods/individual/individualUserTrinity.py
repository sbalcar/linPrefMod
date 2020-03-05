#!/usr/bin/python3

from userProfileModel.userProfileModel import UserProfileModel #class

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class
from userProfileModel.user import User2D #class

from methods.individual.aIndividual import AIndividual #class

from geometry.point import Point #class

from methods.individual.aIndividual import AIndividual #class

from userProfileModel.userProfileModel import UserProfileModel #class
from userProfileModel.model.prefFnc.model.prefFncTriangularModel import PrefFncTriangularModel #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class


class IndividualUserTrinity(AIndividual):
  # ix:float, iy:float, wx:float
  def __init__(self, ix, iy, wx):
#      if type(ix) is not float and type(ix) is not int:
#          print(type(ix))
#          raise ValueError("Argument ix isn't type float/int.")
#      if type(iy) is not float and type(iy) is not int:
#          raise ValueError("Argument iy isn't type float/int.")
#      if type(wx) is not float and type(wx) is not int:
#          raise ValueError("Argument wx isn't type float/int.")
      self.ix = float(ix)
      self.iy = float(iy)
      self.wx = float(wx)

  def printIndividualUser(self):
      print("IndividualUser ix:", self.ix,  " iy:", self.iy, " wx:", self.wx)

  def exportUserProfileModel(self, linPrefModelConf):
      # prefFncX:PrefFncX
      prefFncX = PrefFncTriangularModel(self.ix).exportAsPrefFncX(linPrefModelConf)
      # prefFncY:PrefFncY
      prefFncY = PrefFncTriangularModel(self.iy).exportAsPrefFncY(linPrefModelConf)
      # aggregation:AggrFnc
      aggrFnc = AggrFnc([self.wx, 1 - self.wx])

      # UserProfileModel
      return UserProfileModel(prefFncX, prefFncY, aggrFnc)

  # pointsDC:list<Point>, linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointsInDC(self, pointsDC, linPrefModelConf):
      # uProfileTriangularModel:UserProfileModel
      uProfileTriangularModel = self.exportUserProfileModel(linPrefModelConf)

      #list<float>
      return uProfileTriangularModel.preferenceOfPointsInDataCube(pointsDC, linPrefModelConf)