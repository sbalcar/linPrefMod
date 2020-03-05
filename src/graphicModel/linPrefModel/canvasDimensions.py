#!/usr/bin/python3

import os, sys

import mpl_toolkits.axes_grid1.axes_size as Size
from mpl_toolkits.axes_grid1 import Divider
import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple #pair

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from generator import *
from geometry.point import Point #class
from geometry.lineSegment import LineSegment #class

from morphism.morphism import getMorphismAggregationFncToPrefCube #function
from morphism.morphism import getMorphismToPrefCube #function

from tkinter import *

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QRadioButton, QDoubleSpinBox, QToolBar, QAction, QWidget)

from PyQt5.QtGui import QFont, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint 
from PyQt5 import QtGui, QtWidgets



class CanvasDimensions:

   # linPrefModelConf:LinPrefModelConfiguration, width:int, height:int
   def __init__(self, linPrefModelConf, width, height):
     self.linPrefModelConf = linPrefModelConf
     self._width = width
     self._height = height

   def __BORDER_WIDTH(self):
      return 40
   def __BORDER_HEIGHT(self):
      return 40

   def __PREF_CUBE_WIDTH(self):
      return 200 * self.linPrefModelConf.SIZE_X_PREF_CUBE
   def __PREF_CUBE_HEIGHT(self):
      return 200 * self.linPrefModelConf.SIZE_Y_PREF_CUBE


   def __DATA_CUBE_WIDTH(self):
      return 200 * self.linPrefModelConf.SIZE_X_DATA_CUBE
   def __DATA_CUBE_HEIGHT(self):
      return 200 * self.linPrefModelConf.SIZE_Y_DATA_CUBE

   def __DATA_CUBE_LABELS(self):
      return 5


   def __PREFFNCX_CUBE_WIDTH(self):
      return 200 * self.linPrefModelConf.SIZE_X_DATA_CUBE
   def __PREFFNCX_CUBE_HEIGHT(self):
      return 200 * self.linPrefModelConf.SIZE_Y_PREF_CUBE

   def __PREFFNCY_CUBE_WIDTH(self):
      return 200 * self.linPrefModelConf.SIZE_X_PREF_CUBE
   def __PREFFNCY_CUBE_HEIGHT(self):
      return 200 * self.linPrefModelConf.SIZE_Y_DATA_CUBE


   def __LENGTH_OF_ARROW(self):
      return 30
   def __WING_OF_ARROW(self):
      return 5



   def __getPrefCubeEndX(self):
     return self.__BORDER_WIDTH()
   def __getPrefCubeEndY(self):
     return self.__BORDER_HEIGHT()
   def __getPrefCubeStartX(self):
     return self.__BORDER_WIDTH() +self.__PREF_CUBE_WIDTH()
   def __getPrefCubeStartY(self):
     return self.__BORDER_HEIGHT() +self.__PREF_CUBE_HEIGHT()


   def __getDataCubeStartX(self):
     return self.__getPrefCubeStartX() +self.__BORDER_WIDTH()
   def __getDataCubeStartY(self):
     return self.__getPrefCubeStartY() +self.__BORDER_HEIGHT()
   def __getDataCubeEndX(self):
     return self.__getDataCubeStartX() +self.__DATA_CUBE_WIDTH()
   def __getDataCubeEndY(self):
     return self.__getDataCubeStartY() +self.__DATA_CUBE_HEIGHT()


   def __getPrefFncXCubeStartX(self):
     return self.__getPrefCubeStartX() +self.__BORDER_WIDTH()
   def __getPrefFncXCubeStartY(self):
     return self.__getPrefCubeStartY()
   def __getPrefFncXCubeEndX(self):
     return self.__getPrefFncXCubeStartX() +self.__PREFFNCX_CUBE_WIDTH()
   def __getPrefFncXCubeEndY(self):
     return self.__getPrefFncXCubeStartY() -self.__PREFFNCX_CUBE_HEIGHT()


   def __getPrefFncYCubeStartX(self):
     return self.__getPrefCubeStartX()
   def __getPrefFncYCubeStartY(self):
     return self.__getPrefCubeStartY() +self.__BORDER_WIDTH()
   def __getPrefFncYCubeEndX(self):
     return self.__getPrefFncYCubeStartX() -self.__PREFFNCY_CUBE_WIDTH()
   def __getPrefFncYCubeEndY(self):
     return self.__getPrefFncYCubeStartY() +self.__PREFFNCY_CUBE_HEIGHT()


   def getLengthOfArrow(self):
     return self.__LENGTH_OF_ARROW()
   def getWingOfArrow(self):
     return self.__WING_OF_ARROW()

   def width(self):
     return 3* self.__BORDER_WIDTH() + self.__PREF_CUBE_WIDTH() + self.__DATA_CUBE_WIDTH()
   def height(self):
     return 3* self.__BORDER_HEIGHT() + self.__PREF_CUBE_HEIGHT() + self.__DATA_CUBE_HEIGHT()






   def getPrefCubeEndX(self):
     return self.__coorX(self.__getPrefCubeEndX())
   def getPrefCubeEndY(self):
     return self.__coorY(self.__getPrefCubeEndY())
   def getPrefCubeStartX(self):
     return self.__coorX(self.__getPrefCubeStartX())
   def getPrefCubeStartY(self):
     return self.__coorY(self.__getPrefCubeStartY())


   def getDataCubeStartX(self):
     return self.__coorX(self.__getDataCubeStartX())
   def getDataCubeStartY(self):
     return self.__coorY(self.__getDataCubeStartY())
   def getDataCubeEndX(self):
     return self.__coorX(self.__getDataCubeEndX())
   def getDataCubeEndY(self):
     return self.__coorY(self.__getDataCubeEndY())


   def getPrefFncXCubeStartX(self):
     return self.__coorX(self.__getPrefFncXCubeStartX())
   def getPrefFncXCubeStartY(self):
     return self.__coorY(self.__getPrefFncXCubeStartY())
   def getPrefFncXCubeEndX(self):
     return self.__coorX(self.__getPrefFncXCubeEndX())
   def getPrefFncXCubeEndY(self):
     return self.__coorY(self.__getPrefFncXCubeEndY())


   def getPrefFncYCubeStartX(self):
     return self.__coorX(self.__getPrefFncYCubeStartX())
   def getPrefFncYCubeStartY(self):
     return self.__coorY(self.__getPrefFncYCubeStartY())
   def getPrefFncYCubeEndX(self):
     return self.__coorX(self.__getPrefFncYCubeEndX())
   def getPrefFncYCubeEndY(self):
     return self.__coorY(self.__getPrefFncYCubeEndY())




   def getLegendOfPreferenceCube(self):
     return [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
   def getLegendOfDataCube(self):
     return [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

   def getLegendOfPrefFncXCube(self):
     bit = self.linPrefModelConf.SIZE_X_DATA_CUBE / self.__DATA_CUBE_LABELS()
     bit = round(bit,2)
     a = str(bit).endswith("0") or str(bit).endswith("5")
     if not a:
        bit = round(bit, 1)

     return [round(bit * i, 2) for i in range(self.__DATA_CUBE_LABELS() +1)]

   def getLegendOfPrefFncYCube(self):
     bit = self.linPrefModelConf.SIZE_Y_DATA_CUBE / self.__DATA_CUBE_LABELS()
     bit = round(bit,2)
     a = str(bit).endswith("0") or str(bit).endswith("5")
     if not a:
        bit = round(bit, 1)
     return [round(bit * i, 2) for i in range(self.__DATA_CUBE_LABELS() +1)]
   
   # x:int
   def __inverzCoorX(self, x):
     multiplicator = self._width / self.width()
     return x / multiplicator
   # y:int
   def __inverzCoorY(self, y):
     multiplicator = self._height / self.height()
     return (-y +self._height)/ multiplicator
   # x:int, y:int
   def inverzDataCube(self, x, y):
     ix = self.__inverzCoorX(x) - self.__getDataCubeStartX()
     iy = self.__inverzCoorY(y) - self.__getDataCubeStartY()

     if (0 <= ix and ix <= self.__DATA_CUBE_WIDTH() and
         0 <= iy and iy <= self.__DATA_CUBE_HEIGHT()):
          return (ix / self.__DATA_CUBE_WIDTH(), iy / self.__DATA_CUBE_HEIGHT())
     return None
   # x:int, y:int
   def inverzPreferenceCube(self, x, y):
     ix = self.__inverzCoorX(x) - self.__getPrefCubeEndX()
     iy = self.__inverzCoorY(y) - self.__getPrefCubeEndY()

     if (0 <= ix and ix <= self.__PREF_CUBE_WIDTH() and
         0 <= iy and iy <= self.__PREF_CUBE_HEIGHT()):
          return (ix, iy)
     return None

   # x:int, y:int
   def coorDataCube(self, x, y):
     # x,y = standardized values <0,1>
     # dcx,dcy = pixels
     dcX = self.__DATA_CUBE_WIDTH() * x / self.linPrefModelConf.SIZE_X_DATA_CUBE
     dcY = self.__DATA_CUBE_HEIGHT() * y / self.linPrefModelConf.SIZE_Y_DATA_CUBE
     return (self.__coorX(self.__getDataCubeStartX() + dcX), self.__coorY(self.__getDataCubeStartY() + dcY))

   # x:int, y:int
   def coorPrefFncX(self, x, y):
     pX = self.__PREFFNCX_CUBE_WIDTH() * x / self.linPrefModelConf.SIZE_X_DATA_CUBE
     pY = self.__PREFFNCX_CUBE_HEIGHT() * y / self.linPrefModelConf.SIZE_Y_PREF_CUBE
     return (self.__coorX(self.__getPrefFncXCubeStartX() + pX), self.__coorY(self.__getPrefFncXCubeStartY() - pY))

   # x:int, y:int
   def coorPrefFncY(self, x, y):
     pX = self.__PREFFNCY_CUBE_WIDTH() * x / self.linPrefModelConf.SIZE_X_PREF_CUBE
     pY = self.__PREFFNCY_CUBE_HEIGHT() * y / self.linPrefModelConf.SIZE_Y_DATA_CUBE
     return (self.__coorX(self.__getPrefFncYCubeStartX() - pX), self.__coorY(self.__getPrefFncYCubeStartY() + pY))

   # x:int, y:int
   def coorPrefCube(self, x, y):
     pX = self.__PREF_CUBE_WIDTH() * x / self.linPrefModelConf.SIZE_X_PREF_CUBE
     pY = self.__PREF_CUBE_HEIGHT() * y / self.linPrefModelConf.SIZE_Y_PREF_CUBE
     #return (self.__coorX(self.__getPrefCubeEndX() + pX), self.__coorY(self.__getPrefCubeEndY() + pY))
     return (self.__coorX(self.__getPrefCubeStartX() - pX), self.__coorY(self.__getPrefCubeStartY() - pY))

   def __coorY(self, y):
     multiplicator = self._height / self.height()
     return (self.height() -y) * multiplicator
   def __coorX(self, x):
     multiplicator = self._width / self.width()
     return x * multiplicator

     

