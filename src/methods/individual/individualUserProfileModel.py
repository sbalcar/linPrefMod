#!/usr/bin/python3

from userProfileModel.userProfileModel import UserProfileModel #class

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class
from userProfileModel.user import User2D #class

from methods.individual.aIndividual import AIndividual #class

from geometry.point import Point #class


class IndividualUserProfileModel(AIndividual):
  # upModel:UserProfileModel
  def __init__(self, upModel):
    if type(upModel) is not UserProfileModel:
        raise ValueError("Argument upModel isn't type UserProfileModel.")
    self.upModel = upModel

  def exportUserProfileModel(self, linPrefModelConf):
    # UserProfileModel
    return self.upModel


  # pointsDC:list<Point>, linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointsInDC(self, pointsDC, linPrefModelConf):
      #list<float>
      return self.upModel.preferenceOfPointsInDataCube(pointsDC, linPrefModelConf)

