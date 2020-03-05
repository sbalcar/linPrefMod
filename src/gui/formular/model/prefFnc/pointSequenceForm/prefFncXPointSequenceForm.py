from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QHBoxLayout, QLayout, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

from userProfileModel.model.prefFnc.model.prefFncPointSequenceModel import PrefFncPointSequenceModel

from geometry.points import Points #class


class PrefFncXPointSequenceForm:
    # pointsList:list<Point>, linPrefModelConf:LinPrefModelConf, eventFnc:Fnc
    def __init__(self, pointsList, linPrefModelConf, eventFnc):

        # points:Points
        self.points = Points(pointsList)
        string = self.points.exportAsString()

        self.qLineEditPoints = QLineEdit()
        self.qLineEditPoints.setText(string)
        self.qLineEditPoints.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        self.qPushButtonShow = QPushButton("Show")
        self.qPushButtonShow.clicked.connect(eventFnc)
        #self.qPushButtonShow.setFixedWidth(70)

        self.qPushButtonClear = QPushButton("Clear")
        self.qPushButtonClear.clicked.connect(self.__clear)
        #self.qPushButtonClear.setFixedWidth(70)


    def exportToLayout(self, layout):
        layout.addRow(QLabel("Points:"), self.qLineEditPoints)
        #layout.addStretch(0)

        qHBoxLayout = QHBoxLayout()
        qHBoxLayout.addWidget(self.qPushButtonShow)
        qHBoxLayout.addWidget(self.qPushButtonClear)

        layout.addRow(qHBoxLayout)


    def exportAsPrefFncXModel(self):
        # pointsNew:Points
        pointsNew = Points.importAsString(self.qLineEditPoints.text())
        if pointsNew == None:
            pointsNew = self.points

        return PrefFncPointSequenceModel(pointsNew.points)

    def __clear(self, event):
        string = self.points.exportAsString()

        self.qLineEditPoints.setText(string)