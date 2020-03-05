import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.figure import Figure

from geometry.point import Point
from graphicModel.linPrefModel.canvasModel import CanvasModel, CanvasModelOfPrefFncX, CanvasModelOfPrefFncY, \
    CanvasModelOfAggregationFnc, CanvasModelOfContorLines, CanvasModelOfPoint
from gui.inputOfForms import InputSimpleShow
from gui.frame.twoUsersFrame.actions import getUserProfileModel
from gui.frame.modelTypes import ModelTypes
from gui.formular.cubes.auxLineForm import AuxLineForm
from gui.formular.cubes.dataCubeForm import DataCubeForm
from gui.formular.cubes.prefFncXCForm import PrefFncXCForm
from gui.formular.cubes.prefFncYCForm import PrefFncYCForm
from gui.formular.cubes.prefCubeForm import PrefCubeForm
from gui.formular.simpleShowForm_old import SimpleShowForm_old

from userProfileModel.user import User2D


class SimpleShowFrame_old:
    # layout:QVBoxLayout
    def __init__(self, layout):
        # layout:QVBoxLayout
        self.layout = layout
        # modelTypeIndex:int
        self.modelTypeIndex = 0
        # color:Qt.color
        self.colorU1 = Qt.green
        # auxiliaryLinesDataCube:Boolean
        self.auxiliaryLinesDataCube = False;
        # auxiliaryLinesPrefCube:Boolean
        self.auxiliaryLinesPrefCube = False;
        # auxiliaryLinesPrefFncXCube:Boolean
        self.auxiliaryLinesPrefFncXCube = False;
        # auxiliaryLinesPrefFncYCube:Boolean
        self.auxiliaryLinesPrefFncYCube = False;
        # diagonalDC:Boolean
        self.diagonalDC = False
        # pointsPrefFncX:Boolean
        self.pointsPrefFncX = False
        # pointsPrefFncY:Boolean
        self.pointsPrefFncY = False
        # contourLineDC:Boolean
        self.contourLineDC = False


    # modelType:ModelTypes
    def show(self, width, height):

        # linPrefModelConf:LinPrefModelConfiguration
        self.linPrefModelConf = InputSimpleShow.linPrefModelConf

        # aggrLevel:Float
        self.aggrLevel = InputSimpleShow.aggrLevel
        # user2D:User2D
        self.user2D = InputSimpleShow.user2D

        # pointsDataCube:Point[]
        self.pointsDataCube = InputSimpleShow.pointsDataCube
        # labels:String[]
        self.labels = InputSimpleShow.labels

        self.width = width
        self.height = height

        self.updateModel()


    def clear(self):
         self.__clearLayout(self.layout)

    def __clearLayout(self, layout):
        if layout == None:
           return
        while layout.count():
           child = layout.takeAt(0)
           if child.widget() is not None:
              child.widget().deleteLater()
              child.widget().close()
           elif child.layout() is not None:
              self.__clearLayout(child.layout())


    def updateModel(self):
        self.clear()

        self.formLeft()
        self.formRight()

        self.model1()
        #self.model2()

    def _update_canvas(self):
        self._dynamic_ax.clear()
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._dynamic_ax.plot(t, np.sin(t + time.time()))
        self._dynamic_ax.figure.canvas.draw()

    def formLeft(self):

        self.user1Form = SimpleShowForm_old(self.modelTypeIndex, self.user2D, self.aggrLevel,
                                            self.linPrefModelConf, self.clickOnFormular)

        # layoutForm:QVBoxLayout
        layoutForm = QVBoxLayout()
        layoutForm.addWidget(self.user1Form.qGroupBoxUser)
        layoutForm.addStretch(1)

        self.layout.addLayout(layoutForm, 0,0,1,1)


    def formRight(self):

        self.auxLineForm = AuxLineForm(self.auxiliaryLinesDataCube, self.auxiliaryLinesPrefCube,
                 self.auxiliaryLinesPrefFncXCube, self.auxiliaryLinesPrefFncYCube, self.clickOnFormular)

        self.contourLineDCForm = DataCubeForm(self.contourLineDC, self.clickOnFormular)

        self.prefFncXCForm = PrefFncXCForm(self.pointsPrefFncX, self.clickOnFormular)

        self.prefFncYCForm = PrefFncYCForm(self.pointsPrefFncY, self.clickOnFormular)

        self.prefCubeForm = PrefCubeForm(self.diagonalDC, self.clickOnFormular)


        # layoutTool:QVBoxLayout
        layoutTool = QVBoxLayout()
        layoutTool.addWidget(self.auxLineForm.qGroupBoxTool)
        layoutTool.addWidget(self.contourLineDCForm.qGroupBoxToolDC)
        layoutTool.addWidget(self.prefFncXCForm.qGroupBoxToolPFX)
        layoutTool.addWidget(self.prefFncYCForm.qGroupBoxToolPFY)
        layoutTool.addWidget(self.prefCubeForm.qGroupBoxToolPC)
        layoutTool.addStretch(1)

        self.layout.addLayout(layoutTool, 0,5,1,1)


    def model1(self):
        modelType = ModelTypes.TRIANGULAR
        if self.modelTypeIndex == 0:
          modelType = ModelTypes.TRIANGULAR
        if self.modelTypeIndex == 1:
          modelType = ModelTypes.REFRACTED
        if self.modelTypeIndex == 2:
          modelType = ModelTypes.TROUGH

        # pointsDC:list<Point>
        pointsDC = [Point(0.5, 0.5), Point(0.65, 0.5), Point(0.6, 0.75), Point(0.85, 0.45)]

        #userProfileModel:UserProfileModel
        userProfileModel = getUserProfileModel(self.user2D, self.linPrefModelConf, modelType)
        # aggrLine:LineSegment
        aggrLine = userProfileModel.aggrFnc.exportAsLineSegment(Point(self.aggrLevel, self.aggrLevel), self.linPrefModelConf)
        # contorLines:LineSegment[]
        contorLines = userProfileModel.getMorphismOfAggregationFncToDataCubeLines(self.aggrLevel, self.linPrefModelConf)

        # pointsPC:List<Point>
        pointsPC = userProfileModel.pointsDataCubeToPointsPrefCube(pointsDC)

        # pointsPXC:List<Point>
        pointsPXC = [Point(pointsDC[i].x, pointsPC[i].y) for i in range(len(pointsDC))]

        # pointsPYC:List<Point>
        pointsPYC = [Point(pointsPC[i].x, pointsDC[i].y) for i in range(len(pointsDC))]

############################

        cModel = CanvasModel()
        cModel.addPrefFncX(CanvasModelOfPrefFncX(userProfileModel.prefFncX, self.colorU1))
        cModel.addPrefFncY(CanvasModelOfPrefFncY(userProfileModel.prefFncY, self.colorU1))
        cModel.addAggregationFnc(CanvasModelOfAggregationFnc(aggrLine, self.colorU1))
        cModel.addContorLines(CanvasModelOfContorLines(contorLines, self.colorU1))
        cModel.addDataCubePoints([CanvasModelOfPoint(pointsDC[i], i, Qt.green) for i in range(len(pointsDC))])

        cModel.addPrefFncXCubePoints([CanvasModelOfPoint(pointsPXC[i], i, Qt.green) for i in range(len(pointsPXC)) if self.pointsPrefFncX])
        cModel.addPrefFncYCubePoints([CanvasModelOfPoint(pointsPYC[i], i, Qt.green) for i in range(len(pointsPYC)) if self.pointsPrefFncY])

        cModel.addPrefCubePoints([CanvasModelOfPoint(pointsPC[i], i, Qt.green) for i in range(len(pointsPC))])
        cModel.auxiliaryLinesDataCube = self.auxiliaryLinesDataCube
        cModel.auxiliaryLinesPrefCube = self.auxiliaryLinesPrefCube
        cModel.auxiliaryLinesPrefFncXCube = self.auxiliaryLinesPrefFncXCube
        cModel.auxiliaryLinesPrefFncYCube = self.auxiliaryLinesPrefFncYCube
        cModel.diagonalDC = self.diagonalDC
        cModel.contourLineDC = self.contourLineDC

        width = 550
        height = 550

        # gModel:GraphicalModel
        gModel = GraphicalModel(self.linPrefModelConf, cModel, self.clickOnCanvas)
        linPrefModelWidget = gModel.paintCanvasModel(width, height)
        linPrefModelWidget.setMinimumWidth(width)
        linPrefModelWidget.setMinimumHeight(height)


        self.layout.addWidget(linPrefModelWidget, 0,1, 2,4)


    def model2(self):

        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout.addWidget(dynamic_canvas)

        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._timer = dynamic_canvas.new_timer(
            100, [(self._update_canvas, (), {})])
        self._timer.start()


    def clickOnFormular(self):
        # modelIndex:int
        self.modelTypeIndex = self.user1Form.qComboBoxModelType.currentIndex()
        #print("modelIndex: " + str(self.modelTypeIndex))

        self.aggrLevel = self.user1Form.qDoubleSpinBoxContourLine.value()

        ix = self.user1Form.qDoubleSpinBoxIdealX.value()
        iy = self.user1Form.qDoubleSpinBoxIdealY.value()
        wx = self.user1Form.qDoubleSpinBoxWeightX.value()

        self.user2D = User2D(1, ix, iy, wx)

        self.auxiliaryLinesDataCube = self.auxLineForm.qCheckBoxAuxLineDC.isChecked()
        self.auxiliaryLinesPrefCube = self.auxLineForm.qCheckBoxAuxLinePC.isChecked()
        self.auxiliaryLinesPrefFncXCube = self.auxLineForm.qCheckBoxAuxLinePXC.isChecked()
        self.auxiliaryLinesPrefFncYCube = self.auxLineForm.qCheckBoxAuxLinePYC.isChecked()

        self.pointsPrefFncX = self.prefFncXCForm.qCheckBoxPrefFncXC.isChecked()
        self.pointsPrefFncY = self.prefFncYCForm.qCheckBoxPrefFncYPC.isChecked()

        self.diagonalDC = self.prefCubeForm.qCheckBoxDiagonalPC.isChecked()

        self.contourLineDC = self.contourLineDCForm.qCheckBoxContourLineDC.isChecked()

        self.updateModel()


    def clickOnCanvas(self, event):
        print("clickOnCanvas")