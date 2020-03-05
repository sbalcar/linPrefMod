from PyQt5.QtWidgets import QFormLayout, QComboBox, QLabel, QGroupBox

from gui.formular.model.prefFnc.triangularForm.prefFncXTriangularForm import PrefFncXTriangularForm
from gui.formular.model.prefFnc.triangularForm.prefFncYTriangularForm import PrefFncYTriangularForm
from gui.formular.model.aggrFnc.aggrFncForm import AggrFncForm

class SimpleShowForm_old:
    def __init__(self, modelTypeIndex, user2D, aggrLevel, linPrefModelConf, eventFnc):

        self.qComboBoxModelType = QComboBox()
        self.qComboBoxModelType.addItem("Triangular")
        self.qComboBoxModelType.addItem("Refracted")
        self.qComboBoxModelType.addItem("Trough")
        self.qComboBoxModelType.setCurrentIndex(modelTypeIndex)
        self.qComboBoxModelType.currentIndexChanged.connect(eventFnc)


        prefFncXTriangularForm = PrefFncXTriangularForm(user2D.ix, linPrefModelConf, eventFnc)
        self.qDoubleSpinBoxIdealX = prefFncXTriangularForm.qDoubleSpinBoxIdealX

        prefFncYTriangularForm = PrefFncYTriangularForm(user2D.iy, linPrefModelConf, eventFnc)
        self.qDoubleSpinBoxIdealY = prefFncYTriangularForm.qDoubleSpinBoxIdealY

        aggrFncForm = AggrFncForm(user2D.wx, aggrLevel, linPrefModelConf, eventFnc)
        self.qDoubleSpinBoxWeightX = aggrFncForm.qDoubleSpinBoxWeightX
        self.qDoubleSpinBoxContourLine = aggrFncForm.qDoubleSpinBoxContourLine


        # layoutUser:QFormLayout
        layoutUser = QFormLayout()
        layoutUser.addRow(QLabel("Model Type:"), self.qComboBoxModelType)
        layoutUser.addRow(QLabel("Ideal X:"), self.qDoubleSpinBoxIdealX)
        layoutUser.addRow(QLabel("Ideal Y:"), self.qDoubleSpinBoxIdealY)
        layoutUser.addRow(QLabel("Weight X:"), self.qDoubleSpinBoxWeightX)
        layoutUser.addRow(QLabel("Contour Line:"), self.qDoubleSpinBoxContourLine)

        # qGroupBoxUser:QGroupBox
        self.qGroupBoxUser = QGroupBox("User definition")
        self.qGroupBoxUser.setLayout(layoutUser)

