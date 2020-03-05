#!/usr/bin/python3

from userProfileModel.model.prefFnc.prefFncs import PrefFncX
from userProfileModel.model.prefFnc.prefFncs import PrefFncY
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class

from userProfileModel.algorithm.algorithmContourLine import AlgorithmContourLine #class

from geometry.lineSegment import LineSegment #class
from geometry.point import Point #class
from geometry.pointWithID import PointWithID #class

from morphism.morphism import getMorphismOfPrefCubePointToDataCubePoint #function

from generator import *


class UserProfileModel:
  # prefFncX:PrefFncX, prefFncY:PrefFncY, aggregation:AggrFnc
  def __init__(self, prefFncX, prefFncY, aggrFnc):
    if type(prefFncX) is not PrefFncX:
       raise ValueError("Argument prefFncX isn't type PrefFncX.")
    if type(prefFncY) is not PrefFncY:
       raise ValueError("Argument prefFncY isn't type PrefFncY.")
    if type(aggrFnc) is not AggrFnc:
       raise ValueError("Argument aggregation isn't type AggrFnc.")
    self.prefFncX = prefFncX
    self.prefFncY = prefFncY
    self.aggrFnc = aggrFnc

  def print(self):
    print("UserProfileModel:")
    print(" prefFncX: " + self.prefFncX.toString())
    print(" prefFncY: " + self.prefFncY.toString())
    print(" aggrFn: "   + self.aggrFnc.toString())

  # pointsDataCube:list<PointWithID>
  def pointsWithIdDCToPointsWithIdPC(self, pointsWithIdDC):
    if type(pointsWithIdDC) is not list:
       raise ValueError("Argument pointsDataCube isn't type list.")
    for pI in pointsWithIdDC:
        if type(pI) is not PointWithID:
            raise ValueError("Argument pointsDataCube don't contain PointWithID.")
    # labels:list<str>
    labels = [pointWithIdI.pointID for pointWithIdI in pointsWithIdDC]
    # pointsDC:list<Point>
    pointsDC = [pointWithIdI.point for pointWithIdI in pointsWithIdDC]

    # pointsPC:list<Point>
    pointsPC = self.pointsDataCubeToPointsPrefCube(pointsDC)
    # list<PointWithID>
    return [PointWithID(pointsPC[i], labels[i]) for i in range(len(pointsPC))]

  # pointsDataCube:list<Point>
  def pointsDataCubeToPointsPrefCube(self, pointsDataCube):
    if type(pointsDataCube) is not list:
       raise ValueError("Argument pointsDataCube isn't type list.")
    for pI in pointsDataCube:
        if type(pI) is not Point:
            raise ValueError("Argument pointsDataCube don't contain Point.")

    pointsPrefCube = [];
    for pointDataCubeI in pointsDataCube:
      pointPrefCubeI = self.pointDataCubeToPointPrefCube(pointDataCubeI);
      pointsPrefCube.append(pointPrefCubeI);
    # pointsPrefCube:list<Point>
    return pointsPrefCube

  # pointDataCube:Point
  def pointDataCubeToPointPrefCube(self, pointDataCube):
    if pointDataCube.x == 1:
     pointDataCube.x = 0.99999
    if pointDataCube.y == 1:
     pointDataCube.y = 0.99999

    #pointPrefCubeI = getMorphismOfDataPointToPrefPoint(pointDataCube, self.prefFncX, self.prefFncY)
    y = self.prefFncX.functionalValue(pointDataCube.x)
    x = self.prefFncY.functionalValue(pointDataCube.y)
    pointPrefCubeI = Point(x,y)
    #Point
    return pointPrefCubeI;

  # pointsInDataCube:Point[], linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointsInDataCube(self, pointsInDataCube, linPrefModelConf):
     preferences = []
     for pointDataCubeI in pointsInDataCube:
         preferenceI = self.preferenceOfPointInDataCube(pointDataCubeI, linPrefModelConf)
         preferences.append(preferenceI)
     # preferences:float[]
     return preferences;

  # pointDataCube:Point, linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointInDataCube(self, pointDataCube, linPrefModelConf):
     pointPrefCube = self.pointDataCubeToPointPrefCube(pointDataCube)
     preference = self.preferenceOfPointInPrefCube(pointPrefCube, linPrefModelConf)
     # preference:float
     return preference


  # pointsInPrefCube:Point[], linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointsInPrefCube(self, pointsInPrefCube, linPrefModelConf):
     preferences = []
     for pointPrefCubeI in pointsInPrefCube:
         preferenceI = self.preferenceOfPointInPrefCube(pointPrefCubeI, linPrefModelConf)
         preferences.append(preferenceI)
     # preferences:float[]
     return preferences

  # pointPrefCube:Point[], linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointInPrefCube(self, pointPrefCube, linPrefModelConf):
     return self.aggrFnc.preferenceOfPointInPC(pointPrefCube, linPrefModelConf)

  # linPrefModelConf:LinPrefModelConfiguration
  def getMorphismOfAggregationFncToDataCubePairOfPoints(self, linPrefModelConf):
    # points:Point[]
    points = self.getAggregationFunction(linPrefModelConf)

    isp1 = getMorphismOfPrefCubePointToDataCubePoint(points[0], self.prefFncX, self.prefFncY)
    isp2 = getMorphismOfPrefCubePointToDataCubePoint(points[1], self.prefFncX, self.prefFncY)

    result = Pair(isp1, isp2)
    # result:Pair(Point[], Point[])
    return result


  # aggrLevel:float, linPrefModelConf:ModelConfiguration
  def getMorphismOfAggregationFncToDataCubeLines(self, aggrLevel, linPrefModelConf):
    # LineSegment[]
    return AlgorithmContourLine.getMorphismOfAggregationFncToDataCubeLines(
        self.prefFncX, self.prefFncY, self.aggrFnc, aggrLevel, linPrefModelConf)


  # aggrLevel:float, linPrefModelConf:LinPrefModelConfiguration
  def getMorphismOfAggregationFncToDataCubePolygon(self, aggrLevel, linPrefModelConf):

    # polygonLineSegments:LineSegment[]
    polygonLineSegments = AlgorithmContourLine.getMorphismOfAggregationFncToDataCubeLines(
        self.prefFncX, self.prefFncY, self.aggrFnc, aggrLevel, linPrefModelConf)

    # polygon:Point[]
    return AlgorithmContourLine.sortDataCubePolygon(polygonLineSegments)

