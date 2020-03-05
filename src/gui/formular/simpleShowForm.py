from PyQt5.QtWidgets import QFormLayout, QGroupBox

from gui.formular.model.prefFnc.triangularForm.prefFncXTriangularForm import PrefFncXTriangularForm
from gui.formular.model.prefFnc.triangularForm.prefFncYTriangularForm import PrefFncYTriangularForm

from gui.formular.model.prefFnc.refractedForm.prefFncXRefractedForm import PrefFncXRefractedForm
from gui.formular.model.prefFnc.refractedForm.prefFncYRefractedForm import PrefFncYRefractedForm

from gui.formular.model.prefFncXModelTypeForm import PrefFncXModelTypeForm
from gui.formular.model.prefFncYModelTypeForm import PrefFncYModelTypeForm

from gui.formular.model.prefFnc.troughForm.prefFncXTroughForm import PrefFncXTroughForm
from gui.formular.model.prefFnc.troughForm.prefFncYTroughForm import PrefFncYTroughtForm

from gui.formular.model.prefFnc.categoricalForm.prefFncXCategoricalForm import PrefFncXCategoricalForm
from gui.formular.model.prefFnc.categoricalForm.prefFncYCategoricalForm import PrefFncYCategoricalForm

from gui.formular.model.prefFnc.pointSequenceForm.prefFncXPointSequenceForm import PrefFncXPointSequenceForm
from gui.formular.model.prefFnc.pointSequenceForm.prefFncYPointSequenceForm import PrefFncYPointSequenceForm

from gui.formular.model.aggrFnc.aggrFncForm import AggrFncForm

from userProfileModel.userProfileModelStructured import UserProfileModelStructured

from userProfileModel.model.prefFnc.model.prefFncTriangularModel import PrefFncTriangularModel
from userProfileModel.model.prefFnc.model.prefFncRefractedModel import PrefFncRefractedModel
from userProfileModel.model.prefFnc.model.prefFncTroughModel import PrefFncTroughModel
from userProfileModel.model.prefFnc.model.prefFncCategoricalModel import PrefFncCategoricalModel
from userProfileModel.model.prefFnc.model.prefFncPointSequenceModel import PrefFncPointSequenceModel


from geometry.point import Point #class


class SimpleShowForm:
    # userProfileModel:UserProfileModel2,
    def __init__(self, userProfileModel, aggrLevel, linPrefModelConf, eventFnc):

        self.__prefFncXForm(userProfileModel.prefFncXModel, linPrefModelConf, eventFnc)
        self.__prefFncYForm(userProfileModel.prefFncYModel, linPrefModelConf, eventFnc)

        self.__aggrFncForm(userProfileModel.aggrFnc, aggrLevel, linPrefModelConf, eventFnc)


        # layoutPrefFncX:QFormLayout
        layoutPrefFncX = QFormLayout()

        self.prefFncModel1TypeForm.exportToLayout(layoutPrefFncX)
        self.prefFncXForm.exportToLayout(layoutPrefFncX)

        # qGroupBoxPrefFncX:QGroupBox
        qGroupBoxPrefFncX = QGroupBox("Pref. Fnc.X")
        qGroupBoxPrefFncX.setLayout(layoutPrefFncX)



        # layoutPrefFncY:QFormLayout
        layoutPrefFncY = QFormLayout()

        self.prefFncModel2TypeForm.exportToLayout(layoutPrefFncY)
        self.prefFncYForm.exportToLayout(layoutPrefFncY)

        # qGroupBoxPrefFncY:QGroupBox
        qGroupBoxPrefFncY = QGroupBox("Pref. Fnc.Y")
        qGroupBoxPrefFncY.setLayout(layoutPrefFncY)



        # layoutAggrFnc:QFormLayout
        layoutAggrFnc = QFormLayout()

        self.aggrFncForm.exportToLayout(layoutAggrFnc)

        # qGroupBoxUser:QGroupBox
        qGroupBoxAggrFnc = QGroupBox("Aggr. Fnc.")
        qGroupBoxAggrFnc.setLayout(layoutAggrFnc)



        # layoutUser:QFormLayout
        layoutUser = QFormLayout()
        layoutUser.addRow(qGroupBoxPrefFncX)
        layoutUser.addRow(qGroupBoxPrefFncY)
        layoutUser.addRow(qGroupBoxAggrFnc)

        # qGroupBoxUser:QGroupBox
        self.qGroupBoxUser = QGroupBox("User definition")
        self.qGroupBoxUser.setLayout(layoutUser)


    # prefFncX:APrefFncModel, linPrefModelConf:LinPrefModelConf, eventFnc:Fnc
    def __prefFncXForm(self, prefFncXModel, linPrefModelConf, eventFnc):

        modelTypeXIndex = 0
        if type(prefFncXModel) is PrefFncTriangularModel:
            modelTypeXIndex = 0
        if type(prefFncXModel) is PrefFncRefractedModel:
            modelTypeXIndex = 1
        if type(prefFncXModel) is PrefFncTroughModel:
            modelTypeXIndex = 2
        if type(prefFncXModel) is PrefFncCategoricalModel:
            modelTypeXIndex = 3
        if type(prefFncXModel) is PrefFncPointSequenceModel:
            modelTypeXIndex = 4


        self.prefFncModel1TypeForm = PrefFncXModelTypeForm(modelTypeXIndex, eventFnc)

        if modelTypeXIndex == 0:
            self.prefFncXForm = PrefFncXTriangularForm(prefFncXModel.iCoordinate, linPrefModelConf, eventFnc)
        if modelTypeXIndex == 1:
            self.prefFncXForm = PrefFncXRefractedForm(prefFncXModel.iCoordinate, linPrefModelConf, eventFnc)
        if modelTypeXIndex == 2:
            self.prefFncXForm = PrefFncXTroughForm(prefFncXModel.iCoordinate, prefFncXModel.bottom, linPrefModelConf, eventFnc)
        if modelTypeXIndex == 3:
            #intervals:list<Tuple<float, float>>, functionValues:list<float>
            self.prefFncXForm = PrefFncXCategoricalForm(prefFncXModel.intervals, prefFncXModel.functionValues, linPrefModelConf, eventFnc)
        if modelTypeXIndex == 4:
            self.prefFncXForm =  PrefFncXPointSequenceForm(prefFncXModel.points, linPrefModelConf, eventFnc)

    # prefFncY:APrefFncModel, linPrefModelConf:LinPrefModelConf, eventFnc:Fnc
    def __prefFncYForm(self, prefFncYModel, linPrefModelConf, eventFnc):

        modelTypeYIndex = 0
        if type(prefFncYModel) is PrefFncTriangularModel:
            modelTypeYIndex = 0
        if type(prefFncYModel) is PrefFncRefractedModel:
            modelTypeYIndex = 1
        if type(prefFncYModel) is PrefFncTroughModel:
            modelTypeYIndex = 2
        if type(prefFncYModel) is PrefFncCategoricalModel:
            modelTypeYIndex = 3
        if type(prefFncYModel) is PrefFncPointSequenceModel:
            modelTypeYIndex = 4


        self.prefFncModel2TypeForm = PrefFncYModelTypeForm(modelTypeYIndex, eventFnc)

        if modelTypeYIndex == 0:
           self.prefFncYForm = PrefFncYTriangularForm(prefFncYModel.iCoordinate, linPrefModelConf, eventFnc)
        if modelTypeYIndex == 1:
           self.prefFncYForm = PrefFncYRefractedForm(prefFncYModel.iCoordinate, linPrefModelConf, eventFnc)
        if modelTypeYIndex == 2:
           self.prefFncYForm = PrefFncYTroughtForm(prefFncYModel.iCoordinate, prefFncYModel.bottom, linPrefModelConf, eventFnc)
        if modelTypeYIndex == 3:
           self.prefFncYForm = PrefFncYCategoricalForm(prefFncYModel.intervals, prefFncYModel.functionValues, linPrefModelConf, eventFnc)
        if modelTypeYIndex == 4:
           self.prefFncYForm = PrefFncYPointSequenceForm(prefFncYModel.points, linPrefModelConf, eventFnc)


    def __aggrFncForm(self, aggrFnc, aggrLevel, linPrefModelConf, eventFnc):

        wx = aggrFnc.weights[0]
        self.aggrFncForm = AggrFncForm(wx, aggrLevel, linPrefModelConf, eventFnc)


    def exportUserProfileModel(self, linPrefModelConf):
        prefFncXModel = self.prefFncXForm.exportAsPrefFncXModel()
        prefFncYModel = self.prefFncYForm.exportAsPrefFncYModel()

        modelTypeXIndex = self.prefFncModel1TypeForm.qComboBoxModelType.currentIndex()
        modelTypeYIndex = self.prefFncModel2TypeForm.qComboBoxModelType.currentIndex()

        if modelTypeXIndex == 0 and type(prefFncXModel) is not PrefFncTriangularModel:
            prefFncXModel = PrefFncTriangularModel(0.5)
        if modelTypeXIndex == 1 and type(prefFncXModel) is not PrefFncRefractedModel:
            prefFncXModel = PrefFncRefractedModel(0.5)
        if modelTypeXIndex == 2 and type(prefFncXModel) is not PrefFncTroughModel:
            prefFncXModel = PrefFncTroughModel(0.5, 0.2)
        if modelTypeXIndex == 3 and type(prefFncXModel) is not PrefFncCategoricalModel:
            prefFncXModel = PrefFncCategoricalModel([(0, 0.5), (0.5, linPrefModelConf.SIZE_X_DATA_CUBE)], [0.3, 0.6])
        if modelTypeXIndex == 4 and type(prefFncXModel) is not PrefFncPointSequenceModel:
            prefFncXModel = PrefFncPointSequenceModel([Point(0, 0), Point(0.2, 0.8), Point(0.3, 0.4), Point(0.5, 1.0), Point(0.7, 0.7), Point(linPrefModelConf.SIZE_X_DATA_CUBE, 0)])


        if modelTypeYIndex == 0 and type(prefFncYModel) is not PrefFncTriangularModel:
            prefFncYModel = PrefFncTriangularModel(0.5)
        if modelTypeYIndex == 1 and type(prefFncYModel) is not PrefFncRefractedModel:
            prefFncYModel = PrefFncRefractedModel(0.5)
        if modelTypeYIndex == 2 and type(prefFncYModel) is not PrefFncTroughModel:
            prefFncYModel = PrefFncTroughModel(0.5, 0.2)
        if modelTypeYIndex == 3 and type(prefFncYModel) is not PrefFncCategoricalModel:
            prefFncYModel = PrefFncCategoricalModel([(0, 0.5), (0.5, linPrefModelConf.SIZE_Y_DATA_CUBE)], [0.3, 0.6])
        if modelTypeYIndex == 4 and type(prefFncYModel) is not PrefFncPointSequenceModel:
            prefFncYModel = PrefFncPointSequenceModel([Point(0, 0), Point(0.2, 0.8), Point(0.3, 0.4), Point(0.5, 1.0), Point(0.7, 0.7), Point(linPrefModelConf.SIZE_Y_DATA_CUBE, 0)])


        # aggrFncForm:AggrFnc
        aggrFncForm = self.aggrFncForm.export()

        return UserProfileModelStructured(prefFncXModel, prefFncYModel, aggrFncForm)


    def exportAggrLevel(self):
        return self.aggrFncForm.exportAggrLevel()