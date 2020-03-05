#!/usr/bin/python3

from PyQt5.QtCore import Qt, QPoint 

from geometry.lineSegment import LineSegment #class
from geometry.lineSegments import LineSegments #class

from geometry.point import Point #class
from geometry.pointWithID import PointWithID #class

class CanvasModel:
    def __init__(self):
       # prefFncsX:list<CanvasModelOfPrefFncX>
       self.prefFncsX = []
       # prefFncsY:list<CanvasModelOfPrefFncY>
       self.prefFncsY = []
       # aggrFncs:list<CanvasModelOfAggregationFnc>
       self.aggrFncs = []
       #contorLines:list<CanvasModelOfContorLines>
       self.contorLines = []
       # pointsDataCube:CanvasModelOfPoint
       self.pointsDataCube = []
       # pointsPrefCube:CanvasModelOfPoint
       self.pointsPrefCube = []
       # pointSelected:int
       self.pointIDSelected = 1
       self.auxiliaryLinesDataCube = False
       self.auxiliaryLinesPrefCube = False
       self.auxiliaryLinesPrefFncXCube = False
       self.auxiliaryLinesPrefFncYCube = False
       # diagonalDC:Boolean
       self.diagonalDC = False
       # pointsPrefFncX:list<CanvasModelOfPoint>
       self.pointsPrefFncXCube = []
       # pointsPrefFncY:list<CanvasModelOfPoint>
       self.pointsPrefFncYCube = []
       # contourLineDC:Boolean
       self.contourLineDC = False

    # prefFncX:CanvasModelOfPrefFncX
    def addPrefFncX(self, prefFncX, color):
        cmPrefFncX = CanvasModelOfPrefFncX(prefFncX, color)
        self.prefFncsX.append(cmPrefFncX)

    # prefFncY:PrefFncY
    def addPrefFncY(self, prefFncY, color):
        cmPrefFncY = CanvasModelOfPrefFncY(prefFncY, color)
        self.prefFncsY.append(cmPrefFncY)

    # aggrnFnc:LineSegment
    def addAggregationFnc(self, aggrLine, color):
        cmAggregationFnc = CanvasModelOfAggregationFnc(aggrLine, color)
        self.aggrFncs.append(cmAggregationFnc)

    # contorLines:CanvasModelOfContorLines
    def addContorLines(self, contorLines, color):
        cmContorLines = CanvasModelOfContorLines(contorLines, color)
        self.contorLines.append(cmContorLines)

    # cmPoints:list<CanvasModelOfPoint>
    def addDataCubePoints(self, pointsWithId, showLabels, color):
       for pointsWithId in pointsWithId:
           self.addDataCubePoint(pointsWithId, showLabels, color)

    # cmPoint:CanvasModelOfPoint
    def addDataCubePoint(self, pointsWithId, showLabels, color):
        if pointsWithId is None:
            return
        cmPoint = CanvasModelOfPoint(pointsWithId.point, pointsWithId.pointID, showLabels, color)
        self.pointsDataCube.append(cmPoint)

    # pointsPrefCube:Point[]
    def setPrefCubePoints(self, pointsPrefCube):
       self.pointsPrefCube = pointsPrefCube

    # cmPoints:list<CanvasModelOfPoint>, showLabels:Boolean
    def addPrefCubePoints(self, pointsWithId, showLabels, color):
       for pointWithIdI in pointsWithId:
          self.addPrefCubePoint(pointWithIdI, showLabels, color)

    # cmPoint:CanvasModelOfPoint, showLabels:Boolean
    def addPrefCubePoint(self, pointWithId, showLabels, color):
        cmPoint = CanvasModelOfPoint(pointWithId.point, pointWithId.pointID, showLabels, color)
        self.pointsPrefCube.append(cmPoint)

    # cmPoints:list<CanvasModelOfPoint>
    def addPrefFncXCubePoints(self, pointsWithId, color):
       for pointWithIdI in pointsWithId:
          self.addPrefFncXCubePoint(pointWithIdI, color)

    # cmPoint:CanvasModelOfPoint
    def addPrefFncXCubePoint(self, pointWithId, color):
        cmPoint = CanvasModelOfPoint(pointWithId.point, pointWithId.pointID, False, color)
        self.pointsPrefFncXCube.append(cmPoint)

    # cmPoints:list<CanvasModelOfPoint>
    def addPrefFncYCubePoints(self, pointsWithId, color):
       for pointWithIdI in pointsWithId:
          self.addPrefFncYCubePoint(pointWithIdI, color)

    # cmPoint:CanvasModelOfPoint
    def addPrefFncYCubePoint(self, pointWithId, color):
        cmPoint = CanvasModelOfPoint(pointWithId.point, pointWithId.pointID, False, color)
        self.pointsPrefFncYCube.append(cmPoint)

    # pointID:int
    def getPointDataCube(self, pointID):
        pointsWitdSelected = [pI.point for pI in self.pointsDataCube if pI.pointID == pointID]
        if len(pointsWitdSelected) == 0:
          return None
        return pointsWitdSelected[0]

    # pointID:int
    def getPointPrefCube(self, pointID):
        pointsWitdSelected = [pI.point for pI in self.pointsPrefCube if pI.pointID == pointID]
        if len(pointsWitdSelected) == 0:
          return None
        return pointsWitdSelected[0]

 


class CanvasModelOfPrefFncX:
    # prefFncX:PrefFncX, color
    def __init__(self, prefFncX, color):
       self.prefFncX = prefFncX
       self.color = color

class CanvasModelOfPrefFncY:
    # prefFncX:PrefFncY, color
    def __init__(self, prefFncY, color):
       self.prefFncY = prefFncY
       self.color = color

class CanvasModelOfAggregationFnc:
    # aggregation:LineSegment
    def __init__(self, aggrFnc, color):
       self.aggrFnc = aggrFnc
       self.color = color

class CanvasModelOfContorLines:
    # contorLines:LineSegment[]
    def __init__(self, contorLines, color):
       self.contorLines = contorLines
       self.color = color

class CanvasModelOfPoint:
    # point:Point, pointID:str, showLabels:Boolean, color:Qt.color
    def __init__(self, point, pointID, showLabels, color):
       self.point = point
       self.pointID = pointID
       self.showLabels = showLabels
       self.color = color

