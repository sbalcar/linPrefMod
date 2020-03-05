#!/usr/bin/python3

from matplotlib.backends.qt_compat import QtWidgets, is_pyqt5
if is_pyqt5():
    pass
else:
    pass

from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class

from PyQt5.QtWidgets import (QFormLayout, QGroupBox, QLabel, QSpinBox, QVBoxLayout, QDoubleSpinBox)

from gui.frame.tresholdFrame.actions import paintPreferenceCube #function

from gui.inputOfForms import InputThreshold #class

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg

class ThresholdFrame:
    # layout:QVBoxLayout
    def __init__(self, layout):
        # layout:QVBoxLayout
        self.layout = layout
        

    # width:int, height:int
    def show(self, width, height):

        input = InputThreshold()

        # linPrefModelConf:LinPrefModelConfiguration
        self.linPrefModelConf = input.linPrefModelConf

        # title:String
        self.title = input.title

        # pointsWithIDs:PointWithID[]
        self.pointsWithIDs = input.pointsWithIDs;

        # wx:float
        self.wx = 0.5
        #numberOfThresholds:integer
        self.numberOfThresholds = 0

        self.form();
        self.model1()


    def updateModel(self):

        # aggregation:AggrFnc
        aggrFnc = AggrFnc([self.wx, 1 - self.wx])

        # preferenceCubeFig:Figure
        preferenceCubeFig = paintPreferenceCube(self.linPrefModelConf, self.title, self.pointsWithIDs, aggrFnc, self.numberOfThresholds)

        # figureCanvas1New:FigureCanvas
        figureCanvas1New = FigureCanvasQTAgg(preferenceCubeFig)

        # removing old figure
        self.figureCanvas1.deleteLater()

        self.layout.replaceWidget(self.figureCanvas1, figureCanvas1New)
        self.figureCanvas1 = figureCanvas1New


    def form(self):

        # layout:QFormLayout
        layout = QFormLayout()

        # qDoubleSpinBoxWeightX:QDoubleSpinBox
        self.qDoubleSpinBoxWeightX = QDoubleSpinBox();
        self.qDoubleSpinBoxWeightX.setValue(self.wx)
        self.qDoubleSpinBoxWeightX.setMinimum(0.05)
        self.qDoubleSpinBoxWeightX.setMaximum(0.95)
        self.qDoubleSpinBoxWeightX.setSingleStep(0.05)
        layout.addRow(QLabel("Weight X:"), self.qDoubleSpinBoxWeightX)

        # qIntegerSpinBoxNumberOfThresholds:QSpinBox
        self.qIntegerSpinBoxNumberOfThresholds = QSpinBox();
        self.qIntegerSpinBoxNumberOfThresholds.setValue(self.numberOfThresholds)
        self.qIntegerSpinBoxNumberOfThresholds.setMinimum(0)
        self.qIntegerSpinBoxNumberOfThresholds.setMaximum(len(self.pointsWithIDs))
        self.qIntegerSpinBoxNumberOfThresholds.setSingleStep(1)
        layout.addRow(QLabel("Number of Thresholds:"), self.qIntegerSpinBoxNumberOfThresholds)


        # button:QPushButton
        button = QtWidgets.QPushButton('Show')
        button.clicked.connect(self.clickUser1)
        layout.addWidget(button)

        # qGroupBoxUser:QGroupBox
        qGroupBoxUser = QGroupBox("User definition")
        qGroupBoxUser.setLayout(layout)

        # layoutForm:QVBoxLayout
        layoutForm = QVBoxLayout()
        layoutForm.addWidget(qGroupBoxUser)
        layoutForm.addStretch(1)

        self.layout.addLayout(layoutForm, 0,0,1,1)


    def model1(self):

        # aggregation:AggrFnc
        aggrFnc = AggrFnc([self.wx, 1 - self.wx])

        #preferenceCubeFig:Figure
        preferenceCubeFig = paintPreferenceCube(self.linPrefModelConf, self.title, self.pointsWithIDs, aggrFnc, self.numberOfThresholds)

        # figureCanvas1:FigureCanvas
        self.figureCanvas1 = FigureCanvasQTAgg(preferenceCubeFig)

        self.layout.addWidget(self.figureCanvas1, 0,1, 2,4)


    def clickUser1(self):

        self.wx = self.qDoubleSpinBoxWeightX.value()
        self.numberOfThresholds = self.qIntegerSpinBoxNumberOfThresholds.value()

        self.updateModel()

