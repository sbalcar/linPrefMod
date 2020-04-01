#!/usr/bin/python3

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from userProfileModel.user import User2D #class

from geometry.point import Point #class
from geometry.pointWithID import PointWithID #class

#from gui.threshold.thresholdFrame import ThresholdFrame #class
#from gui.nd.ndFrame import NdFrame #class

from datasets.generator.reader import Reader #class

from geometry.point import Point
from geometry.pointWithID import PointWithID

from userProfileModel.model.prefFnc.model.prefFncRefractedModel import PrefFncRefractedModel
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc

from userProfileModel.userProfileModelStructured import UserProfileModelStructured

import random
import os


class InputSimpleShow:
    # linPrefModelConf:LinPrefModelConfiguration
    linPrefModelConf = LinPrefModelConfiguration(1.0, 1.0, 1.0, 1.0)

    # userProfileModelStructured:UserProfileModelStructured
    userProfileModelStructured = UserProfileModelStructured(
        PrefFncRefractedModel(0.5), PrefFncRefractedModel(0.5), AggrFnc([0.5, 0.5]))

    # aggrLevel:Float
    aggrLevel = 0.8

    # pointsVisitedDC:list<PointWithID>
    pointsWithIDVisitedDC = [PointWithID(Point(0.70, 0.75), "A"), PointWithID(Point(0.15, 0.45), "B"),
                             PointWithID(Point(0.60, 0.15), "C"), PointWithID(Point(0.40, 0.85), "D"),
                             PointWithID(Point(0.5, 0.5), "E")]

    # pointsNoVisitedDC:list<PointWithID>
    pointsWithIDNoVisitedDC = [PointWithID(Point(0.25, 0.15), "M"), PointWithID(Point(0.1, 0.65), "N"),
                               PointWithID(Point(0.35, 0.85), "O"), PointWithID(Point(0.9, 0.7), "P"),
                               PointWithID(Point(0.65, 0.45), "Q")]

    def generatePointsWithIDVisitedDC(count):
        points = []
        for i in range(count):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            pI = PointWithID(Point(x, y), i)
            points.append(pI)
        return points

    def generatePointsWithIDNoVisitedDC(count):
        points = []
        for i in range(count):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            pI = PointWithID(Point(x, y), 100 +i)
            points.append(pI)
        return points

class InputTwoUsers:
    #linPrefModelConf:LinPrefModelConfiguration
    linPrefModelConf = LinPrefModelConfiguration(2.0, 1.25, 1.0, 1.0)

    #user2D1:User2D
    user2D1 = User2D(1, 1.5, 0.3, 0.66)
    #user2D2:User2D
    user2D2 = User2D(2, 0.5, 0.9, 0.33)

    # aggrLevel1:Float
    aggrLevel1 = 0.667
    # aggrLevel2:Float
    aggrLevel2 = 0.667

    #pointsWithIdVisitedDC:Point[]
    #pointsDataCube = [Point(0.73, 0.755), Point(1.125, 0.45), Point(1.624, 0.15)]
    pointsWithIdVisitedDC = [PointWithID(Point(0.5, 0.5), "A"), PointWithID(Point(0.75, 0.5), "B"),
                             PointWithID(Point(0.5, 0.75), "C"), PointWithID(Point(0.75, 0.75), "D")]
    #labels:String[]
    #labels = ["A", "B", "C"]


class InputThreshold:
    #linPrefModelConf:LinPrefModelConfiguration
    linPrefModelConf = LinPrefModelConfiguration(2.0, 1.25, 1.0, 1.0)

    #title:String
    title = "Preferenc Cube"; 

    #points:Point[]
    points = [Point(0.1, 0.1), Point(0.2, 0.2), Point(0.3, 0.4), Point(0.9, 0.5)]

    # pointsWithIDs:PointWithID[]
    pointsWithIDs = [PointWithID(Point(0.1, 0.9), 'A'), PointWithID(Point(0.2, 0.8), 'B'), PointWithID(Point(0.3, 0.7), 'C'), PointWithID(Point(0.4, 0.6), 'D'), PointWithID(Point(0.5, 0.5), 'E')]


class InputND:
   #fileNameItems:String

   fileNameItems = ".." + os.sep + "datasets" + os.sep + "itemsMy.csv"
   #fileNameRatings:String
   fileNameRatings = ".." + os.sep + "datasets" + os.sep + "ratingsMy.csv"
   #fileNameUsers:String
   fileNameUsers = ".." + os.sep + "datasets" + os.sep + "usersMy.csv"

   def read(self):
      return Reader.read(self.fileNameItems, self.fileNameRatings, self.fileNameUsers)     


