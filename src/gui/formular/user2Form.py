from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QComboBox, QLabel, QDoubleSpinBox, QGroupBox, QVBoxLayout, QCheckBox

from gui.formular.simpleShowForm_old import SimpleShowForm_old

class User2Form:
    def __init__(self, modelTypeIndex1, user2D1, aggrLevel1,
                 modelTypeIndex2, user2D2, aggrLevel2, linPrefModelConf, eventFnc):

        # u1:User1Form
        u1 = SimpleShowForm_old(modelTypeIndex1, user2D1, aggrLevel1, linPrefModelConf, eventFnc)

        # qComboBoxModelType1:QComboBox
        self.qComboBoxModelType1 = u1.qComboBoxModelType

        # qDoubleSpinBoxIdealX1:QDoubleSpinBox
        self.qDoubleSpinBoxIdealX1 = u1.qDoubleSpinBoxIdealX

        # qDoubleSpinBoxIdealY1:QDoubleSpinBox
        self.qDoubleSpinBoxIdealY1 = u1.qDoubleSpinBoxIdealY

        # qDoubleSpinBoxWeightX1:QDoubleSpinBox
        self.qDoubleSpinBoxWeightX1 = u1.qDoubleSpinBoxWeightX

        # qDoubleSpinBoxContourLine1:QDoubleSpinBox
        self.qDoubleSpinBoxContourLine1 = u1.qDoubleSpinBoxContourLine

        # qGroupBoxUser1:QGroupBox
        self.qGroupBoxUser1 = u1.qGroupBoxUser


        # u2:User1Form
        u2 = SimpleShowForm_old(modelTypeIndex2, user2D2, aggrLevel2, linPrefModelConf, eventFnc)

        # qComboBoxModelType2:QComboBox
        self.qComboBoxModelType2 = u2.qComboBoxModelType

        # qDoubleSpinBoxIdealX2:QDoubleSpinBox
        self.qDoubleSpinBoxIdealX2 = u2.qDoubleSpinBoxIdealX

        # qDoubleSpinBoxIdealY2:QDoubleSpinBox
        self.qDoubleSpinBoxIdealY2 = u2.qDoubleSpinBoxIdealY

        # qDoubleSpinBoxWeightX2:QDoubleSpinBox
        self.qDoubleSpinBoxWeightX2 = u2.qDoubleSpinBoxWeightX

        # qDoubleSpinBoxContourLine2:QDoubleSpinBox
        self.qDoubleSpinBoxContourLine2 = u2.qDoubleSpinBoxContourLine

        # qGroupBoxUser2:QGroupBox
        self.qGroupBoxUser2 = u2.qGroupBoxUser

