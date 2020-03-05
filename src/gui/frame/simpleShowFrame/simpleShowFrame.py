from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox

from geometry.point import Point
from geometry.pointWithID import PointWithID
from geometry.pointsWithID import PointsWithID
from geometry.pointWithRating import PointWithRating

from graphicModel.linPrefModel.canvasModel import CanvasModel
from gui.inputOfForms import InputSimpleShow
from gui.formular.cubes.auxLineForm import AuxLineForm
from gui.formular.cubes.prefFncXCForm import PrefFncXCForm
from gui.formular.cubes.prefFncYCForm import PrefFncYCForm
from gui.formular.cubes.prefCubeForm import PrefCubeForm
from gui.formular.cubes.dataCubeForm import DataCubeForm
from gui.formular.simpleShowForm import SimpleShowForm
from gui.formular.methods.methodsForm import MethodsForm

from graphicModel.linPrefModel.canvasDimensions import CanvasDimensions
from graphicModel.linPrefModel.canvasWidget import CanvasWidget

from methods.model.methodsModel import MethodsModel


class SimpleShowFrame:
    # layout:QVBoxLayout
    def __init__(self, layout):
        # layout:QVBoxLayout
        self.layout = layout
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
        # pointsPrefFncX:Boolean
        self.pointsPrefFncX = False
        # pointsPrefFncY:Boolean
        self.pointsPrefFncY = False
        # diagonalDC:Boolean
        self.diagonalPC = False
        # pointLabelsPC:Boolean
        self.pointLabelsPC = False
        # contourLineDC:Boolean
        self.contourLineDC = False
        # pointLabelsDC:Boolean
        self.pointLabelsDC = False
        # selectedPointIdDC:str
        self.selectedPointIdDC = None

        # linPrefModelConf:LinPrefModelConfiguration
        self.linPrefModelConf = InputSimpleShow.linPrefModelConf

        # userProfileModelStructured:UserProfileModelStructured
        self.userProfileModelStructured = InputSimpleShow.userProfileModelStructured
        # aggrLevel:Float
        self.aggrLevel = InputSimpleShow.aggrLevel

        # pointsWithIdVisitedDC:list<PointWithID>
        #self.pointsWithIdVisitedDC = InputSimpleShow.pointsWithIDVisitedDC
        self.pointsWithIdVisitedDC = InputSimpleShow.generatePointsWithIDVisitedDC(100)
        # pointsWithIdNoVisitedDC:list<PointWithID>
        #self.pointsWithIdNoVisitedDC = InputSimpleShow.pointsWithIDNoVisitedDC
        self.pointsWithIdNoVisitedDC = InputSimpleShow.generatePointsWithIDNoVisitedDC(100)

        # methodsModel:MethodsModel
        self.methodsModel = MethodsModel.getModel()


#    MethodsModel

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

        self.__showFormLeft()
        self.__showFormRight()
        self.__showModels()

        self.__showFormDown()

    def __showFormLeft(self):

        self.user1Form = SimpleShowForm(self.userProfileModelStructured, self.aggrLevel,
                                        self.linPrefModelConf, self.clickOnFormular)

        # layoutForm:QVBoxLayout
        layoutForm = QVBoxLayout()
        layoutForm.addWidget(self.user1Form.qGroupBoxUser)
        layoutForm.addStretch(0)
        layoutForm.minimumSize()

        self.layout.addLayout(layoutForm, 0,0,1,1)

    def __showFormRight(self):

        self.auxLineForm = AuxLineForm(self.auxiliaryLinesDataCube, self.auxiliaryLinesPrefCube,
                 self.auxiliaryLinesPrefFncXCube, self.auxiliaryLinesPrefFncYCube, self.clickOnFormular)

        self.dataCubeForm = DataCubeForm(self.contourLineDC, self.pointLabelsDC, self.clickOnFormular)

        self.prefFncXCForm = PrefFncXCForm(self.pointsPrefFncX, self.clickOnFormular)

        self.prefFncYCForm = PrefFncYCForm(self.pointsPrefFncY, self.clickOnFormular)

        self.prefCubeForm = PrefCubeForm(self.diagonalPC, self.pointLabelsPC, self.clickOnFormular)


        # layoutTool:QVBoxLayout
        layoutTool = QVBoxLayout()
        layoutTool.addWidget(self.auxLineForm.qGroupBoxTool)
        layoutTool.addWidget(self.dataCubeForm.qGroupBoxToolDC)
        layoutTool.addWidget(self.prefFncXCForm.qGroupBoxToolPFX)
        layoutTool.addWidget(self.prefFncYCForm.qGroupBoxToolPFY)
        layoutTool.addWidget(self.prefCubeForm.qGroupBoxToolPC)
        layoutTool.addStretch(1)

        self.layout.addLayout(layoutTool, 0,5,1,1)

    def __showFormDown(self):

        # pointsVisitedDC:list<Point>
        pointsVisitedDC = [p.point for p in self.pointsWithIdVisitedDC]
        # pointsWithRatingDC:list<PointWithRating>
        pointsWithRatingDC = [PointWithRating(pointsVisitedDC[i], self.preferences[i]) for i in range(len(pointsVisitedDC))]

        # methodsModel:MethodsModel, pointsWithRatingDC:List<PointWithRating>, linPrefModelConf:LinPrefModelConfiguration, updateModel:Function
        self.methodsForm = MethodsForm(self.methodsModel, pointsWithRatingDC, self.linPrefModelConf, self.updateModel)

        self.layout.addWidget(self.methodsForm.qGroupBoxToolMethods, 5, 1, 1, 4)


    def __showModels(self):
        cModel = CanvasModel()

        self.__showModelBasedOnForm(cModel)
        self.__showModelBasedOnMethods(cModel)

        # size:float
        size = min(self.width * 0.55, self.height * 0.70)
        # cDimensions:CanvasDimensions
        self.cDimensions = CanvasDimensions(self.linPrefModelConf, size, size)

        # linPrefModelWidget:CanvasWidget
        linPrefModelWidget = CanvasWidget(self.cDimensions, cModel, self.linPrefModelConf, self.clickOnCanvas)
        #linPrefModelWidget.setMinimumWidth(self.width * 0.64)
        #linPrefModelWidget.setMinimumHeight(self.height * 0.75)
        linPrefModelWidget.setMinimumWidth(550)
        linPrefModelWidget.setMinimumHeight(550)

        canvasLayout = QHBoxLayout()
        #canvasLayout.setAlignment(Qt.No)
        canvasLayout.addWidget(linPrefModelWidget)
        #canvasLayout.addStretch()

        # qGroupBoxVisualization:QGroupBox
        qGroupBoxVisualization = QGroupBox("Visualization")
        qGroupBoxVisualization.setLayout(canvasLayout)

        self.layout.addWidget(qGroupBoxVisualization, 0,1, 4,4)


    def __showModelBasedOnForm(self, cModel):

        #upModel:UserProfileModel
        self.upModel = self.userProfileModelStructured.exportAsUserProfileModel(self.linPrefModelConf)

        # pointsVisitedPC:List<PointWithID>
        self.pointsWithIDVisitedPC = self.upModel.pointsWithIdDCToPointsWithIdPC(self.pointsWithIdVisitedDC)
        # preferences:list<float>
        self.preferences = self.upModel.aggrFnc.preferenceOfPointsWitIDInPC(self.pointsWithIDVisitedPC, self.linPrefModelConf)


        # aggrLine:LineSegment
        aggrLine = self.upModel.aggrFnc.exportAsLineSegment(Point(self.aggrLevel, self.aggrLevel), self.linPrefModelConf)
        # contorLines:LineSegment[]
        contorLines = self.upModel.getMorphismOfAggregationFncToDataCubeLines(self.aggrLevel, self.linPrefModelConf)

        # pointsWithIdVisitedPXC:List<PointWithID>
        pointsWithIdVisitedPXC = [PointWithID(Point(self.pointsWithIdVisitedDC[i].point.x, self.pointsWithIDVisitedPC[i].point.y), self.pointsWithIdVisitedDC[i].pointID) for i in range(len(self.pointsWithIdVisitedDC))]
        # pointsWithIdVisitedPYC:List<PointWithID>
        pointsWithIdVisitedPYC = [PointWithID(Point(self.pointsWithIDVisitedPC[i].point.x, self.pointsWithIdVisitedDC[i].point.y), self.pointsWithIDVisitedPC[i].pointID) for i in range(len(self.pointsWithIdVisitedDC))]

        # selectedPointWithIdDC:PointWithId
        selectedPointWithIdDC = None if self.selectedPointIdDC is None else PointsWithID(self.pointsWithIdVisitedDC).exportPoint(self.selectedPointIdDC)


        cModel.addPrefFncX(self.upModel.prefFncX, self.colorU1)
        cModel.addPrefFncY(self.upModel.prefFncY, self.colorU1)
        cModel.addAggregationFnc(aggrLine, self.colorU1)
        cModel.addContorLines(contorLines, self.colorU1)
        cModel.addDataCubePoints(self.pointsWithIdVisitedDC, self.pointLabelsDC, self.colorU1)
        cModel.addDataCubePoints(self.pointsWithIdNoVisitedDC, self.pointLabelsDC, Qt.yellow)
        cModel.addDataCubePoint(selectedPointWithIdDC, self.pointLabelsDC, Qt.red)

        cModel.addPrefFncXCubePoints([p for p in pointsWithIdVisitedPXC if self.pointsPrefFncX], self.colorU1)
        cModel.addPrefFncYCubePoints([p for p in pointsWithIdVisitedPYC if self.pointsPrefFncY], self.colorU1)

        cModel.addPrefCubePoints(self.pointsWithIDVisitedPC, self.pointLabelsPC, self.colorU1)
        cModel.auxiliaryLinesDataCube = self.auxiliaryLinesDataCube
        cModel.auxiliaryLinesPrefCube = self.auxiliaryLinesPrefCube
        cModel.auxiliaryLinesPrefFncXCube = self.auxiliaryLinesPrefFncXCube
        cModel.auxiliaryLinesPrefFncYCube = self.auxiliaryLinesPrefFncYCube
        cModel.diagonalDC = self.diagonalPC
        cModel.contourLineDC = self.contourLineDC
        cModel.pointIDSelected = self.selectedPointIdDC


    def __showModelBasedOnMethods(self, cModel):
        # upModel:UserProfileModel
        #upModel = self.methodsForm.currentUserProfileModel
        upModel = self.methodsModel.currentUserProfileModel
        if upModel is None:
            return

        # aggrLine:LineSegment
        aggrLine = upModel.aggrFnc.exportAsLineSegment(Point(self.aggrLevel, self.aggrLevel), self.linPrefModelConf)

        # contorLines:LineSegment[]
        contorLines = upModel.getMorphismOfAggregationFncToDataCubeLines(self.aggrLevel, self.linPrefModelConf)

        cModel.addPrefFncX(upModel.prefFncX, Qt.red)
        cModel.addPrefFncY(upModel.prefFncY, Qt.red)
        cModel.addAggregationFnc(aggrLine, Qt.red)
        cModel.addContorLines(contorLines, Qt.red)

    def clickOnFormular(self, event):

        # userProfileModelStructured:UserProfileModelStructured
        self.userProfileModelStructured = self.user1Form.exportUserProfileModel(self.linPrefModelConf)

        # aggrLevel:float
        self.aggrLevel = self.user1Form.exportAggrLevel()

        self.auxiliaryLinesDataCube = self.auxLineForm.qCheckBoxAuxLineDC.isChecked()
        self.auxiliaryLinesPrefCube = self.auxLineForm.qCheckBoxAuxLinePC.isChecked()
        self.auxiliaryLinesPrefFncXCube = self.auxLineForm.qCheckBoxAuxLinePXC.isChecked()
        self.auxiliaryLinesPrefFncYCube = self.auxLineForm.qCheckBoxAuxLinePYC.isChecked()

        self.pointsPrefFncX = self.prefFncXCForm.qCheckBoxPrefFncXC.isChecked()
        self.pointsPrefFncY = self.prefFncYCForm.qCheckBoxPrefFncYPC.isChecked()

        self.diagonalPC = self.prefCubeForm.qCheckBoxDiagonalPC.isChecked()
        self.pointLabelsPC = self.prefCubeForm.qCheckBoxPointLabelsPC.isChecked()

        self.contourLineDC = self.dataCubeForm.qCheckBoxContourLineDC.isChecked()
        self.pointLabelsDC = self.dataCubeForm.qCheckBoxPointLabelsDC.isChecked()

        self.updateModel()


    def clickOnCanvas(self, event):

        # iPoint:Tube<int, int>
        iPoint = self.cDimensions.inverzDataCube(event.pos().x(), event.pos().y())
        if iPoint is None:
          return

        x = iPoint[0] * self.linPrefModelConf.SIZE_X_DATA_CUBE
        y = iPoint[1] * self.linPrefModelConf.SIZE_Y_DATA_CUBE

        # pointID:float
        self.selectedPointIdDC = PointsWithID(self.pointsWithIdVisitedDC).exportTheNearest(Point(x, y), 0.02)
        #print(self.selectedPointIdDC)

        self.updateModel()