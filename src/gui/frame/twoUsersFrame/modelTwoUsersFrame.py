from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout

from geometry.point import Point
from graphicModel.linPrefModel.canvasModel import CanvasModel

from gui.inputOfForms import InputTwoUsers
from gui.frame.twoUsersFrame.actions import getUserProfileModel
from gui.frame.modelTypes import ModelTypes
from gui.formular.cubes.prefFncXCForm import PrefFncXCForm
from gui.formular.cubes.prefFncYCForm import PrefFncYCForm
from gui.formular.cubes.prefCubeForm import PrefCubeForm
from gui.formular.cubes.auxLineForm import AuxLineForm
from gui.formular.user2Form import User2Form
from gui.formular.cubes.dataCubeForm import DataCubeForm

from graphicModel.linPrefModel.canvasDimensions import CanvasDimensions
from graphicModel.linPrefModel.canvasWidget import CanvasWidget

from userProfileModel.user import User2D


class ModelTwoUsersFrame:
    def __init__(self, layout):
        self.layout = layout
        # modelTypeIndex1:int
        self.modelTypeIndex1 = 0
        # modelTypeIndex2:int
        self.modelTypeIndex2 = 0
        # color:Qt.color
        self.colorU1 = Qt.green
        # color:Qt.color
        self.colorU2 = Qt.red
        # auxiliaryLinesDataCube:Boolean
        self.auxiliaryLinesDataCube = False;
        # auxiliaryLinesPrefCube:Boolean
        self.auxiliaryLinesPrefCube = False;
        # auxiliaryLinesPrefFncXCube:Boolean
        self.auxiliaryLinesPrefFncXCube = False;
        # auxiliaryLinesPrefFncYCube:Boolean
        self.auxiliaryLinesPrefFncYCube = False;
        # diagonalDC:Boolean
        self.diagonalPC = False
        # pointsPrefFncX:Boolean
        self.pointsPrefFncX = False
        # pointsPrefFncY:Boolean
        self.pointsPrefFncY = False
        # contourLineDC:Boolean
        self.contourLineDC = False

        self.pointLabelsDC = False
        self.pointLabelsPC = False
        self.selectedPointIdDC = None

        #linPrefModelConf:LinPrefModelConfiguration
        self.linPrefModelConf = InputTwoUsers.linPrefModelConf

        #user2D1:User2D
        self.user2D1 = InputTwoUsers.user2D1
        #user2D2:User2D
        self.user2D2 = InputTwoUsers.user2D2

        # aggrLevel1:Float
        self.aggrLevel1 = InputTwoUsers.aggrLevel1
        # aggrLevel2:Float
        self.aggrLevel2 = InputTwoUsers.aggrLevel2

        #pointsWithIdVisitedDC:list<PointWithID>
        self.pointsWithIdVisitedDC = InputTwoUsers.pointsWithIdVisitedDC


    # modelType:ModelTypes
    def show(self, width, height):
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

    def formLeft(self):

        self.user2Form = User2Form(self.modelTypeIndex1, self.user2D1, self.aggrLevel1,
                    self.modelTypeIndex2, self.user2D2, self.aggrLevel2, self.linPrefModelConf, self.clickUser1)

        # layoutFormUsers:QVBoxLayout
        layoutFormUsers = QVBoxLayout()
        layoutFormUsers.addWidget(self.user2Form.qGroupBoxUser1)
        layoutFormUsers.addWidget(self.user2Form.qGroupBoxUser2)

        # qGroupBox:QGroupBox
        qGroupBoxUser = QGroupBox("User definition")
        qGroupBoxUser.setLayout(layoutFormUsers)

        # layoutForm:QVBoxLayout
        layoutForm = QVBoxLayout()
        layoutForm.addWidget(qGroupBoxUser)
        layoutForm.addStretch(1)

        self.layout.addLayout(layoutForm, 0,0,1,1)


    def formRight(self):

        self.auxLineForm = AuxLineForm(self.auxiliaryLinesDataCube, self.auxiliaryLinesPrefCube,
                 self.auxiliaryLinesPrefFncXCube, self.auxiliaryLinesPrefFncYCube, self.clickUser1)

        self.contourLineDCForm = DataCubeForm(self.contourLineDC, self.pointLabelsDC, self.clickUser1)

        self.prefFncXCForm = PrefFncXCForm(self.pointsPrefFncX, self.clickUser1)

        self.prefFncYCForm = PrefFncYCForm(self.pointsPrefFncY, self.clickUser1)

        self.prefCubeForm = PrefCubeForm(self.diagonalPC, self.pointLabelsPC, self.clickUser1)


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

        modelType1 = ModelTypes.TRIANGULAR
        if self.modelTypeIndex1 == 0:
          modelType1 = ModelTypes.TRIANGULAR
        if self.modelTypeIndex1 == 1:
          modelType1 = ModelTypes.REFRACTED
        if self.modelTypeIndex1 == 2:
          modelType1 = ModelTypes.TROUGH

        modelType2 = ModelTypes.TRIANGULAR
        if self.modelTypeIndex2 == 0:
          modelType2 = ModelTypes.TRIANGULAR
        if self.modelTypeIndex2 == 1:
          modelType2 = ModelTypes.REFRACTED
        if self.modelTypeIndex2 == 2:
          modelType2 = ModelTypes.TROUGH


        #userProfileModel:UserProfileModel
        upModel1 = getUserProfileModel(self.user2D1, self.linPrefModelConf, modelType1)
        # aggrLine:LineSegment
        aggrLineU1 = upModel1.aggrFnc.exportAsLineSegment(Point(self.aggrLevel1, self.aggrLevel1), self.linPrefModelConf)
        # contorLines:LineSegment[]
        contorLinesU1 = upModel1.getMorphismOfAggregationFncToDataCubeLines(self.aggrLevel1, self.linPrefModelConf)
        # pointsPC1:List<PointWithID>
        pointsPC1 = upModel1.pointsWithIdDCToPointsWithIdPC(self.pointsWithIdVisitedDC)

        #userProfileModel:UserProfileModel
        userProfileModel2 = getUserProfileModel(self.user2D2, self.linPrefModelConf, modelType2)
        # aggrLine:LineSegment
        aggrLineU2 = userProfileModel2.aggrFnc.exportAsLineSegment(Point(self.aggrLevel2, self.aggrLevel2), self.linPrefModelConf)
        # contorLines:LineSegment[]
        contorLinesU2 = userProfileModel2.getMorphismOfAggregationFncToDataCubeLines(self.aggrLevel2, self.linPrefModelConf)
        # pointsPC2:List<PointWithID>
        pointsPC2 = userProfileModel2.pointsWithIdDCToPointsWithIdPC(self.pointsWithIdVisitedDC)


        # pointsVisitedPC:List<PointWithID>
        pointsVisitedPC = upModel1.pointsWithIdDCToPointsWithIdPC(self.pointsWithIdVisitedDC)

        cModel = CanvasModel()
        cModel.addPrefFncX(upModel1.prefFncX, self.colorU1)
        cModel.addPrefFncY(upModel1.prefFncY, self.colorU1)
        #cModel.addAggregationFnc(aggrLine, self.colorU1)
        #cModel.addContorLines(contorLines, self.colorU1)
        cModel.addDataCubePoints(pointsPC1, self.pointLabelsDC, self.colorU1)
        cModel.addDataCubePoints(pointsPC2, self.pointLabelsDC, Qt.yellow)
        #cModel.addDataCubePoint(selectedPointWithIdDC, self.pointLabelsDC, Qt.red)

        #cModel.addPrefFncXCubePoints([p for p in pointsWithIdVisitedPXC if self.pointsPrefFncX], self.colorU1)
        #cModel.addPrefFncYCubePoints([p for p in pointsWithIdVisitedPYC if self.pointsPrefFncY], self.colorU1)

        cModel.addPrefCubePoints(pointsVisitedPC, self.pointLabelsPC, self.colorU1)
        cModel.auxiliaryLinesDataCube = self.auxiliaryLinesDataCube
        cModel.auxiliaryLinesPrefCube = self.auxiliaryLinesPrefCube
        cModel.auxiliaryLinesPrefFncXCube = self.auxiliaryLinesPrefFncXCube
        cModel.auxiliaryLinesPrefFncYCube = self.auxiliaryLinesPrefFncYCube
        cModel.diagonalDC = self.diagonalPC
        cModel.contourLineDC = self.contourLineDC
        cModel.pointIDSelected = self.selectedPointIdDC

        # cDimensions:CanvasDimensions
        cDimensions = CanvasDimensions(self.linPrefModelConf, self.width * 0.5, self.height * 0.7)

        # linPrefModelWidget:CanvasWidget
        linPrefModelWidget = CanvasWidget(cDimensions, cModel, self.linPrefModelConf, self.clickOnCanvas)
        linPrefModelWidget.setMinimumWidth(550)
        linPrefModelWidget.setMinimumHeight(550)

        self.layout.addWidget(linPrefModelWidget, 0,1, 2,4)

    def clickUser1(self):

        self.modelTypeIndex1 = self.user2Form.qComboBoxModelType1.currentIndex()
        self.modelTypeIndex2 = self.user2Form.qComboBoxModelType2.currentIndex()

        self.aggrLevel1 = self.user2Form.qDoubleSpinBoxContourLine1.value()
        self.aggrLevel2 = self.user2Form.qDoubleSpinBoxContourLine2.value()

        ix1 = self.user2Form.qDoubleSpinBoxIdealX1.value()
        iy1 = self.user2Form.qDoubleSpinBoxIdealY1.value()
        wx1 = self.user2Form.qDoubleSpinBoxWeightX1.value()

        self.user2D1 = User2D(1, ix1, iy1, wx1)

        ix2 = self.user2Form.qDoubleSpinBoxIdealX2.value()
        iy2 = self.user2Form.qDoubleSpinBoxIdealY2.value()
        wx2 = self.user2Form.qDoubleSpinBoxWeightX2.value()

        self.user2D2 = User2D(1, ix2, iy2, wx2)

        self.updateModel()

    def clickUser2(self):
        self.aggrLevel2 = self.qDoubleSpinBoxContourLine2.value()

        ix = self.qDoubleSpinBoxIdealX2.value()
        iy = self.qDoubleSpinBoxIdealY2.value()
        wx = self.qDoubleSpinBoxWeightX2.value()

        self.user2D2 = User2D(1, ix, iy, wx)

        self.updateModel()

    def clickOnCanvas(self, event):
        print("clickOnCanvas")
