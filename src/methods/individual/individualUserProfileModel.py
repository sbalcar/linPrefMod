#!/usr/bin/python3

from typing import List

from userProfileModel.userProfileModel import UserProfileModel #class

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class
from userProfileModel.user import User2D #class

from methods.individual.aIndividual import AIndividual #class

from geometry.point import Point #class

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class


class IndividualUserProfileModel(AIndividual):
  # upModel:UserProfileModel
  def __init__(self, upModel):
    if type(upModel) is not UserProfileModel:
        raise ValueError("Argument upModel isn't type UserProfileModel.")
    self._upModel:UserProfileModel = upModel

  def exportUserProfileModel(self, linPrefModelConf):
    # UserProfileModel
    return self._upModel


  # pointsDC:list<Point>, linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointsInDC(self, pointsDC:List[Point], linPrefModelConf:LinPrefModelConfiguration):
      #list<float>
      return self._upModel.preferenceOfPointsInDataCube(pointsDC, linPrefModelConf)

