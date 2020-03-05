#!/usr/bin/python3

#from graphicModel.linPrefModel.graphicalModel import GraphicalModel #class
from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from datasets.userProfile import getUserProfileModel01 #function
from datasets.userProfile import getUserProfileModel02 #function

from geometry.point import Point #class

from graphicModel.linPrefModel.painting_old import Painting #class

from methods.operators.evaluation.fitness_old import rmse #function

from datasets.datasets import readItems #function


def paintData():
  #linPrefModelConf:LinPrefModelConfiguration
  linPrefModelConf = LinPrefModelConfiguration(1.0, 1.0, 1.0, 1.0)

  #userProfileModel1:UserProfileModel
  userProfileModel1 = getUserProfileModel01()

  #userProfileModel2:UserProfileModel
  userProfileModel2 = getUserProfileModel02()

  # fileNameItems:String
  fileNameItems = "../datasets/itemsRefractedModel.csv"

  # items:Item[]
  items = readItems(fileNameItems);

  #pointsDataCube:Point[]
  pointsDataCube = [Point(i.x, i.y) for i in items]

  pointsPrefCube1 = userProfileModel1.pointsDataCubeToPointsPrefCube(pointsDataCube);
  pointsPrefCube2 = userProfileModel2.pointsDataCubeToPointsPrefCube(pointsDataCube);

  # preferences:float[]
  preferences1 = userProfileModel1.preferenceOfPointsInPC(pointsPrefCube1, linPrefModelConf);
  preferences2 = userProfileModel2.preferenceOfPointsInPC(pointsPrefCube2, linPrefModelConf);

  rmseVal = rmse(preferences1, preferences2)
  print("rmse: ", rmseVal);

  #title:String
  title = 'Lin. pref. model';

  #painting:Painting
  painting = Painting(linPrefModelConf, title)
  painting.paintModelOnlyPoints(userProfileModel1, pointsDataCube, pointsPrefCube1, "r");
  painting.paintModelOnlyPoints(userProfileModel2, pointsDataCube, pointsPrefCube1, "g");

  painting.paint("");

