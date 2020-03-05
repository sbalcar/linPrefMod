#!/usr/bin/python3

from userProfileModel.userProfileModel import UserProfileModel #class
from userProfileModel.userProfileModelND import UserProfileModelND #class

from userProfileModel.model.prefFnc.prefFnc import PrefFnc #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class
from userProfileModel.model.aggrFnc.aggrFncND import AggrFncND #class

from geometry.point import Point #class


class UserND:
  # uid:int, iCoordinates:float[], weights:float[]
  def __init__(self, uid, iCoordinates, weights):
    if type(uid) is not int:
       raise ValueError("Argument uid isn't type int.")
    if type(iCoordinates) is not list:
       raise ValueError("Argument iCoordinates isn't type list.")
    for iCoordinateI in iCoordinates:
       if type(iCoordinateI) is not float:
          raise ValueError("Argument iCoordinates don't contain float.")
    if type(weights) is not list:
       raise ValueError("Argument weights isn't type list.")
    for weightI in weights:
       if type(weightI) is not float:
          raise ValueError("Argument weights don't contain float.")
    self.uid = uid
    self.iCoordinates = iCoordinates
    self.weights = weights

  def dimension(self):
    # int
    return len(self.iCoordinates);

  def exportAsList(self):
    result = [self.uid]
    for iCoordinateI in self.iCoordinates:
       result.append(iCoordinateI);
    for weightI in self.weights:
       result.append(weightI);
    # result:list
    return result;   

  def exportAsUserProfileModelND(self):
    # prefFncs:list<PrefFnc>
    prefFncs = [PrefFnc() for i in range(3)]
    # aggregation:AggrFncND
    aggrFnc = AggrFncND(self.weights)
    # UserProfileModelND
    return UserProfileModelND(prefFncs, aggrFnc)

  def printUser(self):
    print("User: ", self.exportAsList())


class User2D:
  # uid:int, ix:float, iy:float, wx:float
  def __init__(self, uid, ix, iy, wx):
    self.uid = int(uid)
    self.ix = float(ix)
    self.iy = float(iy)
    self.wx = float(wx)

  def printUser(self):
    print("User uid:", self.uid, " ix:", self.ix,  " iy:", self.iy, " wx:", self.wx)

  # linPrefModelConf:LinPrefModelConfiguration
  def exportUserProfileTriangularModel(self, linPrefModelConf):
    # prefFncX:PrefFncX
    prefFncX = self.exportPrefFncXTriangularModel(linPrefModelConf);
    # prefFncY:PrefFncY
    prefFncY = self.exportPrefFncYTriangularModel(linPrefModelConf);
    # aggregation:AggrFnc
    aggrFnc = self.exportAggrFnc();

    # UserProfileModel
    return UserProfileModel(prefFncX, prefFncY, aggrFnc);

  # linPrefModelConf:LinPrefModelConfiguration
  def exportUserProfileRefractedModel(self, linPrefModelConf):
    up3Model = self.exportUserProfileTriangularModel(linPrefModelConf);
    up3Model.prefFncX = up3Model.prefFncX.exportRefractedPrefFncX()
    up3Model.prefFncY = up3Model.prefFncY.exportRefractedPrefFncY()

    # up3Model:UserProfileRefractedModel
    return up3Model;


  # linPrefModelConf:LinPrefModelConfiguration
  def exportUserProfileNewModel(self, linPrefModelConf):
    # prefFncX:PrefFncX
    prefFncX = self.exportPrefFncXNewModel(linPrefModelConf);
    # prefFncY:PrefFncY
    prefFncY = self.exportPrefFncYNewModel(linPrefModelConf);
    # aggregation:AggrFnc
    aggrFnc = self.exportAggrFnc();

    # UserProfileModel
    return UserProfileModel(prefFncX, prefFncY, aggrFnc);



  # linPrefModelConf:LinPrefModelConfiguration
  def exportPrefFncXTriangularModel(self, linPrefModelConf):
    return PrefFncX([Point(0, 0), Point(self.ix, 1), Point(linPrefModelConf.SIZE_X_DATA_CUBE, 0)])

  # linPrefModelConf:LinPrefModelConfiguration
  def exportPrefFncYTriangularModel(self, linPrefModelConf):
    return PrefFncY([Point(0, 0), Point(1, self.iy), Point(0, linPrefModelConf.SIZE_Y_DATA_CUBE)])

  # linPrefModelConf:LinPrefModelConfiguration
  def exportPrefFncXNewModel(self, linPrefModelConf):
    return PrefFncX([Point(0, 0), Point(self.ix, 1), Point(self.ix +0.1, 1), Point(linPrefModelConf.SIZE_X_DATA_CUBE, 0)])

  # linPrefModelConf:LinPrefModelConfiguration
  def exportPrefFncYNewModel(self, linPrefModelConf):
    return PrefFncY([Point(0, 0), Point(1, self.iy), Point(1, self.iy +0.1), Point(0, linPrefModelConf.SIZE_Y_DATA_CUBE)])


  def exportAggrFnc(self):
    # aggregation:AggrFnc
    #aggregation = AggrFnc([self.wx, 1 - self.wx])
    aggrFnc = AggrFnc([1- self.wx, self.wx])
    
    # aggregation:AggrFnc
    return aggrFnc
