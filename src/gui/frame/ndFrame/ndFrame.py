#!/usr/bin/python3

import time

from matplotlib.backends.qt_compat import is_pyqt5
if is_pyqt5():
    pass
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas)
from matplotlib.figure import Figure


from generator import *

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from PyQt5.QtWidgets import (QFormLayout, QGroupBox, QLabel, QSpinBox, QTextEdit,
                             QDoubleSpinBox)

from gui.frame.ndFrame.actions import visualisationOfContourLinesOneUser #function

from gui.inputOfForms import InputND #class


class NdFrame:
    # layout:QVBoxLayout
    def __init__(self, layout):
        # layout:QVBoxLayout
        self.layout = layout

        input = InputND()
        # items, ratings, users:(List<PointNDWithID>, List<Rating>, List<UserProfileModelDefinition>)
        items, ratings, users = input.read()

        # pointsNDWithIdDataCube:List<PointNDWithID>
        self.pointsNDWithIdDataCube = items
 
        # ratings:List<Rating>
        self.ratings = ratings

        # users:List<UserProfileModelDefinition>
        self.users = users
        

    # width:int, height:int
    def show(self, width, height):

        # linPrefModelConf:LinPrefModelConfiguration
        self.linPrefModelConf = LinPrefModelConfiguration(1.0, 1.0, 1.0, 1.0)

        # userID:int
        self.userID = 1

        # dimensionX:int
        self.dimensionX = 0
        self.dimensionY = 1

        self.wx = 0.5

        # aggrLevel:Float
        self.aggrLevel = 0.8

        self.form();
        self.model1()
        #self.model2()


    def updateModel(self):

        # pointsDataCube:List<Point>
        pointsDataCube = [pointsNDWithIdI.exportPointWithID(self.dimensionX, self.dimensionY).point for pointsNDWithIdI in self.pointsNDWithIdDataCube]
        # labels:List<str>
        labels = [pointsNDWithIdI.pointID for pointsNDWithIdI in self.pointsNDWithIdDataCube]

        # ratings:List<Float>
        ratings = [ratingI.rating for ratingI in self.ratings if ratingI.userID == self.userID]

        # user:UserProfileModelDefinition
        user = [userI for userI in self.users if userI.userID == self.userID][0]
        # userProfileModel:UserProfileModel
        userProfileModel = user.exportUserProfileModel(self.dimensionX, self.dimensionY)

        # linPrefModelFig:Figure
        linPrefModelFig = visualisationOfContourLinesOneUser(userProfileModel, self.aggrLevel, pointsDataCube, labels, ratings, self.linPrefModelConf);
        # figureCanvas1New:FigureCanvas
        figureCanvas1New = FigureCanvas(linPrefModelFig)

        # removing old figure
        self.figureCanvas1.deleteLater()

        self.layout.replaceWidget(self.figureCanvas1, figureCanvas1New)
        self.figureCanvas1 = figureCanvas1New

        # update qTextEditUser
        self.qTextEditUser.clear()
        for uLineI in self.users[self.userID].exportAsList():
          self.qTextEditUser.append(str(uLineI))
        self.qTextEditUser.verticalScrollBar().setValue(self.qTextEditUser.verticalScrollBar().minimum())


    def _update_canvas(self):
        self._dynamic_ax.clear()
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._dynamic_ax.plot(t, np.sin(t + time.time()))
        self._dynamic_ax.figure.canvas.draw()

    def form(self):

        # layout:QFormLayout
        layout = QFormLayout()

        # qIntegerSpinBoxUserID:QSpinBox
        self.qIntegerSpinBoxUserID = QSpinBox();
        self.qIntegerSpinBoxUserID.setValue(self.userID)
        self.qIntegerSpinBoxUserID.setMinimum(0)
        self.qIntegerSpinBoxUserID.setMaximum(len(self.users))
        self.qIntegerSpinBoxUserID.setSingleStep(1)
        self.qIntegerSpinBoxUserID.valueChanged.connect(self.clickUser1)
        layout.addRow(QLabel("User ID:"), self.qIntegerSpinBoxUserID)

        # qIntegerSpinBoxDimensionX:QSpinBox
        self.qIntegerSpinBoxDimensionX = QSpinBox();
        self.qIntegerSpinBoxDimensionX.setValue(self.dimensionX)
        self.qIntegerSpinBoxDimensionX.setMinimum(0)
        self.qIntegerSpinBoxDimensionX.setMaximum(3)
        self.qIntegerSpinBoxDimensionX.setSingleStep(1)
        self.qIntegerSpinBoxDimensionX.valueChanged.connect(self.clickUser1)
        layout.addRow(QLabel("Dimension X:"), self.qIntegerSpinBoxDimensionX)

        # qIntegerSpinBoxDimensionY:QSpinBox
        self.qIntegerSpinBoxDimensionY = QSpinBox();
        self.qIntegerSpinBoxDimensionY.setValue(self.dimensionY)
        self.qIntegerSpinBoxDimensionY.setMinimum(0)
        self.qIntegerSpinBoxDimensionY.setMaximum(3)
        self.qIntegerSpinBoxDimensionY.setSingleStep(1)
        self.qIntegerSpinBoxDimensionY.valueChanged.connect(self.clickUser1)
        layout.addRow(QLabel("Dimension Y:"), self.qIntegerSpinBoxDimensionY)

        # self.qTextEditUser:QTextEdit
        self.qTextEditUser = QTextEdit()
        for uLineI in self.users[self.userID].exportAsList():
          self.qTextEditUser.append(str(uLineI))
        self.qTextEditUser.verticalScrollBar().setValue(self.qTextEditUser.verticalScrollBar().minimum())
        #self.qTextEditUser.setReadOnly(True)
        layout.addRow("User Profile Model Def.", self.qTextEditUser)

        # qDoubleSpinBoxWeightX:QDoubleSpinBox
        self.qDoubleSpinBoxWeightX = QDoubleSpinBox();
        self.qDoubleSpinBoxWeightX.setValue(self.wx)
        self.qDoubleSpinBoxWeightX.setMinimum(0.05)
        self.qDoubleSpinBoxWeightX.setMaximum(0.95)
        self.qDoubleSpinBoxWeightX.setSingleStep(0.05)
        self.qDoubleSpinBoxWeightX.valueChanged.connect(self.clickUser1)
        layout.addRow(QLabel("Weight X:"), self.qDoubleSpinBoxWeightX)

        # qDoubleSpinBoxContourLine:QDoubleSpinBox
        self.qDoubleSpinBoxContourLine = QDoubleSpinBox();
        self.qDoubleSpinBoxContourLine.setValue(self.aggrLevel)
        self.qDoubleSpinBoxContourLine.setMinimum(0.05)
        self.qDoubleSpinBoxContourLine.setMaximum(0.95)
        self.qDoubleSpinBoxContourLine.setSingleStep(0.05)
        self.qDoubleSpinBoxContourLine.valueChanged.connect(self.clickUser1)
        layout.addRow(QLabel("Contour Line:"), self.qDoubleSpinBoxContourLine)

#        # button:QPushButton
#        button = QtWidgets.QPushButton('Show')
#        button.clicked.connect(self.clickUser1)
#        layout.addWidget(button)

        # qGroupBox:QGroupBox
        qGroupBox = QGroupBox("User definition")
        qGroupBox.setLayout(layout)

        self.layout.addWidget(qGroupBox)


    def model1(self):

        # pointsDataCube:List<Point>
        pointsDataCube = [pointsNDWithIdI.exportPointWithID(self.dimensionX, self.dimensionY).point for pointsNDWithIdI in self.pointsNDWithIdDataCube]
        # labels:List<str>
        labels = [pointsNDWithIdI.pointID for pointsNDWithIdI in self.pointsNDWithIdDataCube]

        # ratings:List<Float>
        ratings = [ratingI.rating for ratingI in self.ratings if ratingI.userID == self.userID]

        # user:UserProfileModelDefinition
        user = [userI for userI in self.users if userI.userID == self.userID][0]
        # userProfileModel:UserProfileModel
        userProfileModel = user.exportUserProfileModel(self.dimensionX, self.dimensionY)

        # linPrefModelFig:Figure
        linPrefModelFig = visualisationOfContourLinesOneUser(userProfileModel, self.aggrLevel, pointsDataCube, labels, ratings, self.linPrefModelConf);

        # figureCanvas1:FigureCanvas
        #self.figureCanvas1 = FigureCanvas(linPrefModelFig)
        #self.layout.addWidget(self.figureCanvas1)

        self.layout.addWidget(linPrefModelFig)

    def model2(self):

        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout.addWidget(dynamic_canvas)

        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._timer = dynamic_canvas.new_timer(
            100, [(self._update_canvas, (), {})])
        self._timer.start()


    def clickUser1(self):

        self.userID = self.qIntegerSpinBoxUserID.value()

        self.dimensionX = self.qIntegerSpinBoxDimensionX.value()
        self.dimensionY = self.qIntegerSpinBoxDimensionY.value()

        self.aggrLevel = self.qDoubleSpinBoxContourLine.value()

        #ix = self.qDoubleSpinBoxIdealX.value()
        #iy = self.qDoubleSpinBoxIdealY.value()
        wx = self.qDoubleSpinBoxWeightX.value()

        self.updateModel()

