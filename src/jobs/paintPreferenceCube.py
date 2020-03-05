#!/usr/bin/python3

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from geometry.point import Point #class

from graphicModel.preferenceCubeModel.paintingPreferenceCubeModel import PaintingPreferenceCubeModel #class


def paintPreferenceCube():
   #linPrefModelConf:LinPrefModelConfiguration
   linPrefModelConf = LinPrefModelConfiguration(2.0, 1.25, 1.0, 1.0)
 
   #points:Point[]
   points = [Point(0.1, 0.1), Point(0.2, 0.2), Point(0.3, 0.4), Point(0.9, 0.5)]

   g = PaintingPreferenceCubeModel(linPrefModelConf, "Data Cube")
   g.paintPreferencerCube(points)
   g.paint(1)



