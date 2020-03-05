#!/usr/bin/python3

from userProfileModel.model.prefFnc.prefFncs import PrefFncX
from userProfileModel.model.prefFnc.prefFncs import PrefFncY
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class
from userProfileModel.model.aggrFnc.aggrFncND import AggrFncND

from userProfileModel.model.prefFnc.model.aPrefFncModel import APrefFncModel #class
from userProfileModel.userProfileModelND import UserProfileModelND #class
from userProfileModel.userProfileModel import UserProfileModel #class

from generator import *


class UserProfileModelDefinition:

  # userID:int, prefFncs:List<APrefFncModel>, aggregation:AggrFncND
  def __init__(self, userID, prefFncModels, aggrFnc):
    if type(userID) is not int:
       raise ValueError("Argument userID isn't type int.")
    if type(prefFncModels) is not list:
       raise ValueError("Argument prefFncModels isn't type list.")
    for prefFncModelI in prefFncModels:
       if not isinstance(prefFncModelI, APrefFncModel):
          raise ValueError("Argument prefFncs don't contain type APrefFncModel.")
    if type(aggrFnc) is not AggrFncND:
       raise ValueError("Argument aggregation isn't type AggrFncND.")
    self.userID = userID
    self.prefFncModels = prefFncModels
    self.aggrFnc = aggrFnc

  def dimension(self):
    # int
    return len(self.prefFncModels);

  def exportAsStr(self):
    return str(self.exportAsList())

  def exportAsList(self):
    # strModels:List<str>
    strModels = [prefFncModelI.toString() for prefFncModelI in self.prefFncModels]
    # strWeights:List<str>
    strWeights = [ str(wI) for wI in self.aggrFnc.weights]

    # result:List<str>
    result = [self.userID]
    result.extend(strModels)
    result.extend(strWeights)
    return result;

  def exportUserProfileModelND(self):
    # prefFncs:PrefFnc[]
    prefFncs = [prefFncModelI.exportPrefFnc(None) for prefFncModelI in self.prefFncModels]
    # aggregation:AggrFncND
    aggrFnc = self.aggrFnc

    # UserProfileModelND
    return UserProfileModelND(prefFncs, aggrFnc)

  # dimensionX:int, dimensionY:int
  def exportUserProfileModel(self, dimensionX, dimensionY):
    # prefFncModelX:APrefFncModel
    prefFncModelX = self.prefFncModels[dimensionX]
    prefFncModelY = self.prefFncModels[dimensionY]
    # prefFncX:List<Point>
    prefFncX = prefFncModelX.exportPrefFnc(None).lineSegments.exportPoints()
    prefFncY = [Point(p.y, p.x) for p in prefFncModelY.exportPrefFnc(None).lineSegments.exportPoints()]
    w1 = self.aggrFnc.weights[dimensionX]
    w2 = self.aggrFnc.weights[dimensionY]
    aggrFnc = AggrFnc([0.5, 0.5])
    return UserProfileModel(PrefFncX(prefFncX), PrefFncY(prefFncY), aggrFnc)


