#!/usr/bin/python3

import mpl_toolkits.axes_grid1.axes_size as Size
from mpl_toolkits.axes_grid1 import Divider
import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple #pair

from generator import *

from geometry.point import Point #class

from geometry.lineSegment import LineSegment #class


class GraphicalPreferenceCubeModel:

  # modelConf:LinPrefModelConfiguration
  def __init__(self, linPrefModelConf):
    self.linPrefModelConf = linPrefModelConf

  # title:String
  def initFigure(self, title):

    #plt.figure(figsize=(10,7)) # 10 is width, 7 is height
    self.figure = plt.figure()
    plt.title(title, pad=20)
    plt.xlabel('Y')
    plt.ylabel('X')
    plt.xlim(self.linPrefModelConf.AXIS_Y_END_PREF_CUBE, self.linPrefModelConf.AXIS_Y_BEGIN_PREF_CUBE)
    plt.ylim(self.linPrefModelConf.AXIS_X_END_PREF_CUBE, self.linPrefModelConf.AXIS_X_BEGIN_PREF_CUBE)
    #plt.legend(loc=title)
    
#    cid = self.figure.canvas.mpl_connect('button_press_event', onclick)
#    self.figure.canvas.mpl_connect('pick_even', onclick)

    #self.figure.canvas.mpl_disconnect(cid)

  # pointsPrefCube:Point[]
  def paintPrefCubePoints(self, pointsPrefCube, labels=[], marker='o', color="b", size=1):
    pointsPrefCubePair=transformToPair(pointsPrefCube)
    #plt.plot(pointsPrefCubePair.second, pointsPrefCubePair.first, marker, labels)
    #return
    for pointIndexI in range(len(pointsPrefCube)):
       #pointI:Point
       pointI = pointsPrefCube[pointIndexI];
       #labelI:String
       labelI = labels[pointIndexI];
    
       plt.scatter(pointI.y, pointI.x, marker=marker, color=color);
       plt.text(pointI.y+0.005, pointI.x-0.02, labelI, fontsize=9)

  def paintPrefCubeDiagonal(self, color="y", linewidth=0.8):
    # points:Point[]
    points = [Point(self.linPrefModelConf.AXIS_X_BEGIN_PREF_CUBE, self.linPrefModelConf.AXIS_Y_BEGIN_PREF_CUBE),
            Point(self.linPrefModelConf.AXIS_X_END_PREF_CUBE, self.linPrefModelConf.AXIS_Y_END_PREF_CUBE)];
    pointsPair = transformToPair(points);
    plt.plot(pointsPair.second, pointsPair.first, color=color, linewidth=linewidth);

  # point1:Point, point2:Point
  def paintPrefCubeAggregationFnc(self, point1, point2, color="r", linewidth=1.0):
    #line:Pair(Point, Point)
    pointsPrefCubePair = transformToPair([point1, point2]);
    plt.plot(pointsPrefCubePair.second, pointsPrefCubePair.first, color=color, linewidth=linewidth);

  # point:Point
  def perpendicularsToPoint(self, point, color="y", linewidth=0.5):
    points = [Point(0, point.y), point]
    pointsPair = transformToPair(points);
    plt.plot(pointsPair.second, pointsPair.first, color=color, linewidth=linewidth);

    points = [Point(point.x, 0), point]
    pointsPair = transformToPair(points);
    plt.plot(pointsPair.second, pointsPair.first, color=color, linewidth=linewidth);

  def save(self, id):
    plt.savefig('../images/dataCube' + str(id) + '.png')
    

  def paint(self, id):
    plt.show()

  def close(self):
    plt.close('all');






# points:Point[]
def transformToPair(points):
    pointsX=[points[i].x for i in range(0, len(points))]
    pointsY=[points[i].y for i in range(0, len(points))]
    # Pair(double[], double[])
    return Pair(pointsX, pointsY)





