#!/usr/bin/python3

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from datasets.userProfile import getUserProfileModelExample01 #function
from datasets.userProfile import getUserProfileModelExample02 #function

from geometry.point import Point #class

from graphicModel.linPrefModel.painting_old import Painting #class

from geometry.surfaceArea import countIntersection #function
from geometry.surfaceArea import countPolygonSurfaceArea #function


def paintContourLinesExample():
  #linPrefModelConf:LinPrefModelConfiguration
  linPrefModelConf = LinPrefModelConfiguration(2.0, 1.25, 1.0, 1.0)

  #userProfileModel1:UserProfileModel
  userProfileModel1 = getUserProfileModelExample01()

  #userProfileModel2:UserProfileModel
  userProfileModel2 = getUserProfileModelExample02()

  aggrLevel = 0.667


  #polygon1:Point[]
  polygon1 = userProfileModel1.getMorphismOfAggregationFncToDataCubePolygon(aggrLevel, linPrefModelConf)

  # surface:float
  surface1 = countPolygonSurfaceArea(polygon1);
  print("Surface1: ", surface1)


  #polygon1:Point[]
  polygon2 = userProfileModel2.getMorphismOfAggregationFncToDataCubePolygon(aggrLevel, linPrefModelConf)

  # surface:float
  surface2 = countPolygonSurfaceArea(polygon2);
  print("Surface2: ", surface2)

  surfaceOfOverlap = countIntersection(polygon1, polygon2)
  print("Overlap: ", surfaceOfOverlap)


  #pointsDataCube:Point[]
  pointsDataCube = [Point(0.73, 0.755), Point(1.125, 0.45), Point(1.624, 0.15)]
  labels = ["A", "B", "C"]

  pointsPrefCube = userProfileModel1.pointsDataCubeToPointsPrefCube(pointsDataCube)
  pointsPrefCube2 = userProfileModel2.pointsDataCubeToPointsPrefCube(pointsDataCube)

  # title:String
  title = 'Lin. pref. model'
  # painting:Painting
  painting = Painting(linPrefModelConf, title)
  painting.paintOnlyModel(userProfileModel1, aggrLevel, 'r')
  painting.paintOnlyModel(userProfileModel2, aggrLevel, 'g')

  painting.paintPoints(pointsDataCube, pointsPrefCube, labelsDataCube=labels, labelsPrefCube=labels, color="r", size=1)
  painting.paintPoints(pointsDataCube, pointsPrefCube2, labelsDataCube=labels, labelsPrefCube=labels, color="b", size=1)


  painting.paint("");


