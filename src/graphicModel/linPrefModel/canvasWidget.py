#!/usr/bin/python3

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from geometry.point import Point #class

from graphicModel.linPrefModel.painting.paintLinPrefModelSkelet import PaintLinPrefModelSkelet
from graphicModel.linPrefModel.painting.paintPrefFncX import PaintPrefFncX
from graphicModel.linPrefModel.painting.paintPrefFncY import PaintPrefFncY
from graphicModel.linPrefModel.canvasModel import CanvasModelOfPoint #class

from tkinter import *

#from matplotlib.backends.qt_compat import QtWidgets, is_pyqt5
#if is_pyqt5():
#    pass
#else:
#    pass

from PyQt5.QtGui import QPen, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets



class CanvasWidget(QtWidgets.QWidget):

    # c:CanvasDimensions, cModel:CanvasModel, linPrefModelConf:LinPrefModelConfiguration, clickFnc:Fnc
    def __init__(self, c, cModel, linPrefModelConf, clickFnc):
        super().__init__()
        self.c = c
        self.cModel = cModel
        self.linPrefModelConf = linPrefModelConf
        self.clickFnc = clickFnc

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self) 

        self.__paintSkelet(qp)
        self.__paintPrefFncsX(qp)
        self.__paintPrefFncsY(qp)
        self.__paintContourLiness(qp)
        self.__paintAggregationFncs(qp)
        self.__paintDataCubePoints(qp)
        self.__paintPrefFncXCubePoints(qp)
        self.__paintPrefFncYCubePoints(qp)
        self.__paintPrefCubePoints(qp)
        self.__paintDataCubeAuxiliaryLiness(qp)
        self.__paintPrefCubeAuxiliaryLiness(qp)
        self.__paintPrefFncXCubeAuxiliaryLiness(qp)
        self.__paintPrefFncYCubeAuxiliaryLiness(qp)
        self.__paintDiagonalPC(qp)
        self.__paintABC(qp)

        qp.end()

    def __paintSkelet(self, qp):
        paintLinPrefModel = PaintLinPrefModelSkelet(self.c, "ahoj")
        paintLinPrefModel.paint(qp)

    def __paintPrefFncsX(self, qp):
        # prefFncXI:CanvasModelOfPrefFncX
        for prefFncXI in self.cModel.prefFncsX:
           self.__paintPrefFncX(qp, prefFncXI)

    # prefFncX:CanvasModelOfPrefFncX
    def __paintPrefFncX(self, qp, cmPrefFncX):
        p = PaintPrefFncX(self.c)
        p.paint(qp, cmPrefFncX)

    def __paintPrefFncsY(self, qp):
        for prefFncYI in self.cModel.prefFncsY:
           self.__paintPrefFncY(qp, prefFncYI)

    # prefFncY:CanvasModelOfPrefFncY
    def __paintPrefFncY(self, qp, prefFncY):
        p = PaintPrefFncY(self.c)
        p.paint(qp, prefFncY)


    def __paintContourLiness(self, qp):
        if not self.cModel.contourLineDC:
            return
        for contorLinesI in self.cModel.contorLines:
           self.__paintContourLines(qp, contorLinesI)

    # cmContorLines:CanvasModelOfContorLines
    def __paintContourLines(self, qp, cmContourLines):
        qp.setPen(QPen(cmContourLines.color, 2, Qt.SolidLine))
        # lineI:LineSegment
        for lineI in cmContourLines.contorLines:
            x1, y1 = self.c.coorDataCube(lineI.point1.x, lineI.point1.y)
            x2, y2 = self.c.coorDataCube(lineI.point2.x, lineI.point2.y)
            qp.drawLine(x1, y1, x2, y2)

    def __paintAggregationFncs(self, qp):
        # aggrFncI:CanvasModelOfAggregationFnc
        for aggrFncI in self.cModel.aggrFncs:
          self.__paintAggregationFnc(qp, aggrFncI)

    # cmAggrFnc:CanvasModelOfAggregationFnc
    def __paintAggregationFnc(self, qp, cmAggrFnc):
        qp.setPen(QPen(cmAggrFnc.color, 2, Qt.SolidLine))
        # aggrLine:LineSegment
        aggrLine = cmAggrFnc.aggrFnc
        x1, y1 = self.c.coorPrefCube(aggrLine.point1.x, aggrLine.point1.y)
        x2, y2 = self.c.coorPrefCube(aggrLine.point2.x, aggrLine.point2.y)
        qp.drawLine(x1, y1, x2, y2)

    def __paintDataCubePoints(self, qp):
        # cmPointI:CanvasModelOfPoint
        for cmPointI in self.cModel.pointsDataCube:
            self.__paintDataCubePoint(qp, cmPointI)

    # cmPoint:CanvasModelOfPoint
    def __paintDataCubePoint(self, qp, cmPoint):
        r = 5
        qp.setBrush(QBrush(cmPoint.color, Qt.SolidPattern))
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        # cmPoint:Point
        point = cmPoint.point
        cX, cY = self.c.coorDataCube(point.x, point.y)
        qp.drawEllipse(cX -r/2, cY -r/2, r, r)
        if cmPoint.showLabels:
          qp.drawText(cX -r/2 + 6, cY -r/2, str(cmPoint.pointID))


    def __paintPrefFncXCubePoints(self, qp):
        # cmPointI:CanvasModelOfPoint
        for cmPointI in self.cModel.pointsPrefFncXCube:
            self.__paintPrefFncXCubePoint(qp, cmPointI)

    # cmPoints:list<CanvasModelOfPoint>
    def __paintPrefFncXCubePoint(self, qp, cmPoint):
        r = 5
        qp.setBrush(QBrush(cmPoint.color, Qt.SolidPattern))
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        # cmPoint:Point
        point = cmPoint.point
        cX, cY = self.c.coorPrefFncX(point.x, point.y)
        qp.drawEllipse(cX -r/2, cY -r/2, r, r)


    def __paintPrefFncYCubePoints(self, qp):
        # cmPointI:CanvasModelOfPoint
        for cmPointI in self.cModel.pointsPrefFncYCube:
            self.__paintPrefFncYCubePoint(qp, cmPointI)

    # cmPoints:list<CanvasModelOfPoint>
    def __paintPrefFncYCubePoint(self, qp, cmPoint):
        r = 5
        qp.setBrush(QBrush(cmPoint.color, Qt.SolidPattern))
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        # cmPoint:Point
        point = cmPoint.point
        cX, cY = self.c.coorPrefFncY(point.x, point.y)
        qp.drawEllipse(cX -r/2, cY -r/2, r, r)


    def __paintPrefCubePoints(self, qp):
        # cmPointI:CanvasModelOfPoint
        for cmPointI in self.cModel.pointsPrefCube:
            self.__paintPrefCubePoint(qp, cmPointI)

    # cmPoint:CanvasModelOfPoint
    def __paintPrefCubePoint(self, qp, cmPoint):
        r = 5
        qp.setBrush(QBrush(cmPoint.color, Qt.SolidPattern))
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        # cmPoint:Point
        point = cmPoint.point
        cX, cY = self.c.coorPrefCube(point.x, point.y)
        qp.drawEllipse(cX -r/2, cY -r/2, r, r)
        if cmPoint.showLabels:
          qp.drawText(cX -r/2 + 6, cY -r/2, str(cmPoint.pointID))

    def __paintDataCubeAuxiliaryLiness(self, qp):
        if not self.cModel.auxiliaryLinesDataCube:
           return
        self.__paintDataCubeAuxiliaryLines(qp)

    def __paintDataCubeAuxiliaryLines(self, qp):
        # pointSelected:Point
        pointSelected = self.cModel.getPointDataCube(self.cModel.pointIDSelected)
        if pointSelected is None:
            return

        x1, y1 = self.c.coorDataCube(pointSelected.x, pointSelected.y)
        x2, y2 = self.c.coorDataCube(pointSelected.x, 0)
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        qp.drawLine(x1, y1, x2, y2)

        x3, y3 = self.c.coorDataCube(0, pointSelected.y)
        qp.drawLine(x1, y1, x3, y3)

    def __paintPrefFncXCubeAuxiliaryLiness(self, qp):
        if not self.cModel.auxiliaryLinesPrefFncXCube:
           return
        self.__paintPrefFncXCubeAuxiliaryLines(qp)

    def __paintPrefFncXCubeAuxiliaryLines(self, qp):
        # pointDCSlctd:Point
        pointDCSlctd = self.cModel.getPointDataCube(self.cModel.pointIDSelected)
        pointPCSlctd = self.cModel.getPointPrefCube(self.cModel.pointIDSelected)
        if pointDCSlctd is None or pointPCSlctd is None:
            return

        x1, y1 = self.c.coorPrefFncX(pointDCSlctd.x, pointPCSlctd.y)
        x2, y2 = self.c.coorPrefFncX(pointDCSlctd.x, 0)
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        qp.drawLine(x1, y1, x2, y2)

        x3, y3 = self.c.coorPrefFncX(0, pointPCSlctd.y)
        qp.drawLine(x1, y1, x3, y3)

    def __paintPrefFncYCubeAuxiliaryLiness(self, qp):
        if not self.cModel.auxiliaryLinesPrefFncYCube:
           return
        self.__paintPrefFncYCubeAuxiliaryLines(qp)

    def __paintPrefFncYCubeAuxiliaryLines(self, qp):
        # pointDCSlctd:Point
        pointDCSlctd = self.cModel.getPointDataCube(self.cModel.pointIDSelected)
        pointPCSlctd = self.cModel.getPointPrefCube(self.cModel.pointIDSelected)
        if pointDCSlctd is None or pointPCSlctd is None:
            return

        x1, y1 = self.c.coorPrefFncY(pointPCSlctd.x, pointDCSlctd.y)
        x2, y2 = self.c.coorPrefFncY(pointPCSlctd.x, 0)
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        qp.drawLine(x1, y1, x2, y2)

        x3, y3 = self.c.coorPrefFncY(0, pointDCSlctd.y)
        qp.drawLine(x1, y1, x3, y3)

    def __paintPrefCubeAuxiliaryLiness(self, qp):
        if not self.cModel.auxiliaryLinesPrefCube:
           return
        self.__paintPrefCubeAuxiliaryLines(qp)

    def __paintPrefCubeAuxiliaryLines(self, qp):
        # pointDCSlctd:Point
        pointSelected = self.cModel.getPointPrefCube(self.cModel.pointIDSelected)
        if pointSelected is None:
            return

        x1, y1 = self.c.coorPrefCube(pointSelected.x, pointSelected.y)
        x2, y2 = self.c.coorPrefCube(pointSelected.x, 0)
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        qp.drawLine(x1, y1, x2, y2)

        x3, y3 = self.c.coorPrefCube(0, pointSelected.y)
        qp.drawLine(x1, y1, x3, y3)

    def __paintDiagonalPC(self, qp):
        if not self.cModel.diagonalDC:
           return

        x1, y1 = self.c.coorPrefCube(0, 0)
        x2, y2 = self.c.coorPrefCube(1, 1)

        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        qp.drawLine(x1, y1, x2, y2)

    def __paintABC(self, qp):
        font = QFont("Comic Sans MS", 17);
        qp.setFont(font)
        x1, y1 = self.c.coorPrefCube(0.0, -0.05)
        qp.drawText(x1, y1, str("Center"))

        x1, y1 = self.c.coorPrefFncX(0.4, 1.2)
        qp.drawText(x1, y1, str("Fref. fnc. X Cube"))

        x1, y1 = self.c.coorDataCube(0.4, 1.05)
        qp.drawText(x1, y1, str("Data Cube"))

        x1, y1 = self.c.coorPrefFncY(0.6, 1.05)
        qp.drawText(x1, y1, str("Fref. fnc. Y Cube"))

        x1, y1 = self.c.coorPrefCube(0.6, 1.2)
        qp.drawText(x1, y1, str("Pref. Cube"))


    def mouseDoubleClickEvent(self, event):

        # iPoint:Tube<int, int>
        iPoint = self.c.inverzDataCube(event.pos().x(), event.pos().y())
        if iPoint is None:
          return

        self.clickFnc(event)



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Linear Monotone Preference Model')
        self.resize(550, 550)

        self._main = QtWidgets.QWidget()

        self.setCentralWidget(self._main)
        self.layout = QtWidgets.QVBoxLayout(self._main)

        self.model = ModelOfPoints()
        self.c = CanvasDimensions(550, 550)

        #widget = CanvasWidget(self.c, self.model)
        #self.layout.addWidget(widget)

        linPrefModelConf = LinPrefModelConfiguration(1,1,1,1)
        model = GraphicalModel(linPrefModelConf)
        model.initFigure("ahoj")
   
        self.layout.addWidget(model.fig1)

    def resizeEvent(self, event):
        width = event.size().width()
        height = event.size().height()

        self.clearLayout()
        self.c = CanvasDimensions(width, height)
        widget = CanvasWidget(self.c, self.model)
        self.layout.addWidget(widget)

        #self.setCentralWidget(widget)

    def clearLayout(self):
        for i in reversed(range(self.layout.count())):
          self.layout.itemAt(i).widget().deleteLater()


def main():
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec()

#main()




