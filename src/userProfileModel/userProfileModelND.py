#!/usr/bin/python3

from userProfileModel.model.prefFnc.prefFnc import PrefFnc
#from userProfileModel.prefFncs import PrefFncX
#from userProfileModel.prefFncs import PrefFncY

import userProfileModel.model.aggrFnc.aggrFncND

from geometry.pointND import PointND #class
#from geometry.point import Point #class

#from graphic.morphism import transformToIntervals #function

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class



class UserProfileModelND:
  # prefFncs:PrefFnc[], aggregation:AggrFncND
  def __init__(self, prefFncs, aggrFnc):
    if type(prefFncs) is not list:
       raise ValueError("Argument prefFncs isn't type list.")
    for prefFncI in prefFncs:
       if type(prefFncI) is not PrefFnc:
          raise ValueError("Argument prefFncs don't contain type PrefFnc.")
    if type(aggrFnc) is not userProfileModel.model.aggrFnc.aggrFncND.AggrFncND:
       raise ValueError("Argument aggregation isn't type AggrFncND.")
    self.prefFncs = prefFncs
    self.aggrFnc = aggrFnc

  def print(self):
    print("UserProfileModel:")
    chars = [chr(x) for x in range(65, 123)][:len(self.prefFncs)]
    for charAndPrefFncI in zip(chars, self.prefFncs):
      print(" prefFnc" + charAndPrefFncI[0] + ": " + charAndPrefFncI[1].toString())
    print(" aggrFn: "   + self.aggrFnc.toString())

  def exportAsStr(self):
    return "UserProfileModel"

  # pointsInDataCube:PointND[], linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointsInDataCube(self, pointsInDataCube, linPrefModelConf):
     if type(pointsInDataCube) is not list:
       raise ValueError("Argument pointsDataCube isn't type list.")
     for pointI in pointsInDataCube:
       if type(pointI) is not PointND:
          raise ValueError("Argument pointI don't contain type PointND.")
     if type(linPrefModelConf) is not LinPrefModelConfiguration:
       raise ValueError("Argument linPrefModelConf isn't type LinPrefModelConfiguration.")

     # preferences:float[]
     preferences = []
     for pointDataCubeI in pointsInDataCube:
         preferenceI = self.preferenceOfPointInDataCube(pointDataCubeI, linPrefModelConf);
         preferences.append(preferenceI)
     # preferences:float[]
     return preferences;

  # pointDataCube:PointND, linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointInDataCube(self, pointDataCube, linPrefModelConf):
     if type(pointDataCube) is not PointND:
       raise ValueError("Argument pointDataCube isn't type PointND.")
     if type(linPrefModelConf) is not LinPrefModelConfiguration:
       raise ValueError("Argument linPrefModelConf isn't type LinPrefModelConfiguration.")

     pointPrefCube = self.pointDataCubeToPointPrefCube(pointDataCube)
     preference = self.preferenceOfPointInPrefCube(pointPrefCube, linPrefModelConf)
     # preference:float
     return preference;


  # pointsDataCube:PointND[]
  def pointsDataCubeToPointsPrefCube(self, pointsDataCube):
    if type(pointsDataCube) is not list:
       raise ValueError("Argument pointsDataCube isn't type list.")
    for pointI in pointsDataCube:
       if type(pointI) is not PointND:
          raise ValueError("Argument pointI don't contain type PointND.")
    # pointsPrefCube:PointND[]
    pointsPrefCube = [];
    for pointDataCubeI in pointsDataCube:
      pointPrefCubeI = self.pointDataCubeToPointPrefCube(pointDataCubeI);
      pointsPrefCube.append(pointPrefCubeI);
    # pointsPrefCube:PointND[]
    return pointsPrefCube

  # pointDataCube:PointND
  def pointDataCubeToPointPrefCube(self, pointDataCube):
    if type(pointDataCube) is not PointND:
       raise ValueError("Argument pointDataCube isn't type PointND.")

#    if pointDataCube.x == 1:
#     pointDataCube.x = 0.99999
#    if pointDataCube.y == 1:
#     pointDataCube.y = 0.99999

    # values:float[]
    values = pointDataCube.exportValues()

    # fncValues:float[]
    fncValues = []
    # indexI:int
    for indexI in range(len(values)):
      # prefFncI:PrefFnc
      prefFncI = self.prefFncs[indexI];
      # fncValueI:float
      fncValueI = prefFncI.functionalValue(values[indexI])
      #print("fncValueI: " + str(fncValueI))
      fncValues.append(fncValueI)

    #PointND
    return PointND(fncValues);


  # pointsInPrefCube:PointND[], linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointsInPrefCube(self, pointsInPrefCube, linPrefModelConf):
     if type(pointsDataCube) is not list:
       raise ValueError("Argument pointsInPrefCube isn't type list.")
     for pointI in pointsInPrefCube:
       if type(pointI) is not PointND:
          raise ValueError("Argument pointI don't contain type PointND.")
     if type(linPrefModelConf) is not LinPrefModelConfiguration:
       raise ValueError("Argument linPrefModelConf isn't type LinPrefModelConfiguration.")

     # preferences:float[]
     preferences = []
     for pointPrefCubeI in pointsInPrefCube:
         preferenceI = self.preferenceOfPointInPrefCube(pointPrefCubeI, linPrefModelConf);
         preferences.append(preferenceI)
     # preferences:float[]
     return preferences;

  # pointPrefCube:PointND[], linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointInPrefCube(self, pointPrefCube, linPrefModelConf):
     if type(pointPrefCube) is not PointND:
       raise ValueError("Argument pointsInPrefCube isn't type list.")
     if type(linPrefModelConf) is not LinPrefModelConfiguration:
       raise ValueError("Argument linPrefModelConf isn't type LinPrefModelConfiguration.")

     return self.aggrFnc.preferenceOfPointInPC(pointPrefCube) #, linPrefModelConf)



