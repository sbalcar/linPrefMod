#!/usr/bin/python3

import os

import mpl_toolkits.axes_grid1.axes_size as Size
from mpl_toolkits.axes_grid1 import Divider
import matplotlib.pyplot as plt

from generator import *

from geometry.point import Point #class

class graphicalModel_old:
# modelConf:LinPrefModelConfiguration
  def __init__(self, modelConf):
    self.gModelConf = modelConf

  # title:String
  def initFigure(self, title):
    #self.fig1 = plt.figure(1, (6.0, 4.4))
    self.fig1 = plt.figure()
    self.fig1.suptitle(title, fontsize=16)
    self.fig1.canvas.set_window_title(title)

    # the rect parameter will be ignore as we will set axes_locator
    rect = (0.1, 0.1, 0.75, 0.75)

    self.ax = []
    self.ax.append(self.fig1.add_axes(rect, label=0));
    self.ax.append(self.fig1.add_axes(rect, label=1));
    self.ax.append(self.fig1.add_axes(rect, label=2));
    self.ax.append(self.fig1.add_axes(rect, label=3));

    # Size.Scaled
    horiz = [Size.Scaled(self.gModelConf.SIZE_X_PREF_CUBE), Size.Scaled(self.gModelConf.SIZE_X_DATA_CUBE)]
    vert = [Size.Scaled(self.gModelConf.SIZE_Y_PREF_CUBE), Size.Scaled(self.gModelConf.SIZE_Y_DATA_CUBE)]


    # divide the axes rectangle into grid whose size is specified by horiz * vert
    divider = Divider(self.fig1, rect, horiz, vert, aspect=False)

    self.ax[0].set_axes_locator(divider.new_locator(nx=1, ny=1))
    self.ax[1].set_axes_locator(divider.new_locator(nx=0, ny=1))
    self.ax[2].set_axes_locator(divider.new_locator(nx=0, ny=0))
    self.ax[3].set_axes_locator(divider.new_locator(nx=1, ny=0))


    self.ax[0].axis([self.gModelConf.AXIS_X_BEGIN_DATA_CUBE, self.gModelConf.AXIS_X_END_DATA_CUBE,
        self.gModelConf.AXIS_Y_BEGIN_DATA_CUBE, self.gModelConf.AXIS_Y_END_DATA_CUBE])
    self.ax[1].axis([self.gModelConf.AXIS_X_END_PREF_CUBE, self.gModelConf.AXIS_X_BEGIN_PREF_CUBE,
        self.gModelConf.AXIS_Y_BEGIN_DATA_CUBE, self.gModelConf.AXIS_Y_END_DATA_CUBE])
    self.ax[2].axis([self.gModelConf.AXIS_X_END_PREF_CUBE, self.gModelConf.AXIS_X_BEGIN_PREF_CUBE,
        self.gModelConf.AXIS_Y_END_PREF_CUBE, self.gModelConf.AXIS_Y_BEGIN_PREF_CUBE])
    self.ax[3].axis([self.gModelConf.AXIS_X_BEGIN_DATA_CUBE, self.gModelConf.AXIS_X_END_DATA_CUBE,
        self.gModelConf.AXIS_Y_END_PREF_CUBE, self.gModelConf.AXIS_Y_BEGIN_PREF_CUBE])


    self.ax[0].tick_params(labeltop=True, labelbottom=False, labelleft=False, labelright=True)
    self.ax[1].tick_params(labeltop=True, labelbottom=False, labelleft=True, labelright=False)
    self.ax[2].tick_params(labeltop=False, labelbottom=True, labelleft=True, labelright=False)
    self.ax[3].tick_params(labeltop=False, labelbottom=True, labelleft=False, labelright=True)

    #self.ax[2].canvas.mpl_connect('button_press_event', onclick)
    self.fig1.canvas.mpl_connect('button_press_event', onclick)

  # pointDataCube:Point
  def paintDataCubePoint(self, pointDataCube, color="b", size=1):
    self.paintDataCubePoints([pointDataCube], color, size)

  # pointDataCube:Point[]
  def paintDataCubePoints(self, pointsDataCube, labels=[], color="b", marker='o', size=1):
    # Pair(double[], double[])
    pointsDataCubePair=transformToPair(pointsDataCube)
    self.ax[0].scatter(pointsDataCubePair.first, pointsDataCubePair.second, marker=marker, color=color, s=size)
    for i in range(0, len(labels)):
      # pointI:Point[]
      pointI = pointsDataCube[i]
      self.ax[0].text(pointI.x + 0.05, pointI.y, labels[i], fontsize=9)

  # contorLines:LineSegment[]
  def paintDataCubeContorLines(self, contorLines, color="b"):
    for contorLineI in contorLines:
        self.paintDataCubeContorLine(contorLineI.point1, contorLineI.point2, color=color);

  def paintDataCubeContorLine(self, point1, point2, color="b"):
    linePair=transformToPair([point1, point2])
    self.ax[0].plot(linePair.first, linePair.second, color=color);

  def paintDataCubePolygonOfContorLines(self, points, color="b"):
    for i in range(len(points)):
      p1 = points[i];
      p2 = points[(i +1) % len(points)]
      self.paintDataCubeContorLine(p1, p2, color=color)

  def paintDataCubeDiagonal(self):
    diagonal=[Point(0, 0), Point(4, 4)]
    diagonalPair=transformToPair(diagonal)
    self.ax[0].plot(diagonalPair.first, diagonalPair.second, color="b");

  def paintDataCubeAuxiliaryLines(self, pointDataCube):
     auxiliaryLineX = Pair(Point(self.gModelConf.AXIS_X_BEGIN_DATA_CUBE, pointDataCube.y), pointDataCube)
     auxiliaryLinePairX = transformToPair(auxiliaryLineX)
     self.ax[0].plot(auxiliaryLinePairX.first, auxiliaryLinePairX.second, color="y", linewidth=0.5);

     auxiliaryLineY = Pair(pointDataCube, Point(pointDataCube.x, self.gModelConf.AXIS_Y_BEGIN_DATA_CUBE))
     auxiliaryLinePairY = transformToPair(auxiliaryLineY)
     self.ax[0].plot(auxiliaryLinePairY.first, auxiliaryLinePairY.second, color="y", linewidth=0.5);


  def paintPrefCubeDiagonal(self, color="b"):
    diagonal=[Point(self.gModelConf.AXIS_X_BEGIN_PREF_CUBE, self.gModelConf.AXIS_Y_BEGIN_PREF_CUBE),
            Point(self.gModelConf.AXIS_X_END_PREF_CUBE, self.gModelConf.AXIS_X_END_PREF_CUBE)]
    diagonalPair=transformToPair(diagonal)
    self.ax[2].plot(diagonalPair.first, diagonalPair.second, color);

  # pointPrefCube:Point
  def paintPrefCubeAuxiliaryLines(self, pointPrefCube):
     auxiliaryLineX = Pair(Point(self.gModelConf.AXIS_X_BEGIN_PREF_CUBE, pointPrefCube.y), pointPrefCube)
     auxiliaryLinePairX = transformToPair(auxiliaryLineX)
     self.ax[2].plot(auxiliaryLinePairX.first, auxiliaryLinePairX.second, color="y", linewidth=0.5);

     auxiliaryLineY = Pair(pointPrefCube, Point(pointPrefCube.x, self.gModelConf.AXIS_Y_BEGIN_PREF_CUBE))
     auxiliaryLinePairY = transformToPair(auxiliaryLineY)
     self.ax[2].plot(auxiliaryLinePairY.first, auxiliaryLinePairY.second, color="y", linewidth=0.5);

  # prefFncX:Point[]
  def paintPrefFncX(self, prefFncX, color="b"):
    prefFncXPair = prefFncX.exportAsPairOfXYCoordinates()
    self.ax[3].plot(prefFncXPair.first, prefFncXPair.second, color);

  # prefFncY:Point[]
  def paintPrefFncY(self, prefFncY, color="b"):
    prefFncYPair = prefFncY.exportAsPairOfXYCoordinates()
    self.ax[1].plot(prefFncYPair.first, prefFncYPair.second, color);

  # prefFncX:Point[]
  def paintPrefFncXAuxiliaryLines(self, pointPrefCubeX):
     auxiliaryLineX = Pair(Point(self.gModelConf.AXIS_X_BEGIN_PREF_CUBE, pointPrefCubeX.y), pointPrefCubeX)
     auxiliaryLinePairX = transformToPair(auxiliaryLineX)
     self.ax[3].plot(auxiliaryLinePairX.first, auxiliaryLinePairX.second, color="y", linewidth=0.5);

     auxiliaryLineY = Pair(pointPrefCubeX, Point(pointPrefCubeX.x, self.gModelConf.AXIS_Y_BEGIN_PREF_CUBE))
     auxiliaryLinePairY = transformToPair(auxiliaryLineY)
     self.ax[3].plot(auxiliaryLinePairY.first, auxiliaryLinePairY.second, color="y", linewidth=0.5);

  # prefFncY:Point[]
  def paintPrefFncYAuxiliaryLines(self, pointPrefCubeY):
     auxiliaryLineY = Pair(Point(self.gModelConf.AXIS_X_BEGIN_PREF_CUBE, pointPrefCubeY.y), pointPrefCubeY)
     auxiliaryLinePairY = transformToPair(auxiliaryLineY)
     self.ax[1].plot(auxiliaryLinePairY.first, auxiliaryLinePairY.second, color="y", linewidth=0.5);

     auxiliaryLineY = Pair(pointPrefCubeY, Point(pointPrefCubeY.x, self.gModelConf.AXIS_Y_BEGIN_PREF_CUBE))
     auxiliaryLinePairY = transformToPair(auxiliaryLineY)
     self.ax[1].plot(auxiliaryLinePairY.first, auxiliaryLinePairY.second, color="y", linewidth=0.5);


  # pointsPrefCube:Point[]
  def paintPrefCubePoints(self, pointsPrefCube, labels=[], marker='o', color="b", size=1):
    pointsPrefCubePair=transformToPair(pointsPrefCube)
    self.ax[2].scatter(pointsPrefCubePair.first, pointsPrefCubePair.second, marker=marker, color=color, s=size);
    for i in range(0, len(labels)):
      # pointI:Point[]
      pointI = pointsPrefCube[i]
      self.ax[2].text(pointI.x + 0.05, pointI.y, labels[i], fontsize=9)



  def paintPrefCubeDiagonal(self):
    # points:Point[]
    points = [Point(self.gModelConf.AXIS_X_BEGIN_PREF_CUBE, self.gModelConf.AXIS_Y_BEGIN_PREF_CUBE),
            Point(self.gModelConf.AXIS_X_END_PREF_CUBE, self.gModelConf.AXIS_Y_END_PREF_CUBE)];
    pointsPair = transformToPair(points);
    self.ax[2].plot(pointsPair.first, pointsPair.second,color="y", linewidth=1.0);

  # point1:Point, point2:Point
  def paintPrefCubeAggregationFnc(self, point1, point2, color="r"):
    #line:Pair(Point, Point)
    pointsPrefCubePair = transformToPair([point1, point2]);
    self.ax[2].plot(pointsPrefCubePair.first, pointsPrefCubePair.second, color=color, linewidth=1.0);

  # pointDataCube:Point[]
  def paintpPrefCubeXPoints(self, pointsDataCube, labels=[], color="b", marker='o', size=1):
    # Pair(double[], double[])
    pointsDataCubePair=transformToPair(pointsDataCube)
    self.ax[3].scatter(pointsDataCubePair.first, pointsDataCubePair.second, marker=marker, color=color, s=size)

  # pointDataCube:Point[]
  def paintpPrefCubeYPoints(self, pointsDataCube, labels=[], color="b", marker='o', size=1):
    # Pair(double[], double[])
    pointsDataCubePair=transformToPair(pointsDataCube)
    self.ax[1].scatter(pointsDataCubePair.first, pointsDataCubePair.second, marker=marker, color=color, s=size)

  def save(self, id, testID=""):
    path = '../images/' + testID
    if os.path.exists(path) is False:
        os.mkdir(path);
    plt.savefig(path + '/linPrefModel' + str(id) + '.png')
  
  def paint(self, id):
    #plt.savefig('../images/linPrefModel' + str(id) + '.png')
    plt.show()

  def close(self):
    plt.close('all');

def onclick(event):
    print("click")








# points:Point[]
def transformToPair(points):
    pointsX=[points[i].x for i in range(0, len(points))]
    pointsY=[points[i].y for i in range(0, len(points))]
    # Pair(double[], double[])
    return Pair(pointsX, pointsY)


