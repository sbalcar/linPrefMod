from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QComboBox, QLabel, QDoubleSpinBox, QGroupBox, QVBoxLayout, QCheckBox

class PrefFncYCForm:
    def __init__(self, pointsPrefFncY, eventFnc):

        # qCheckBoxPrefFncYPC:QCheckBox
        self.qCheckBoxPrefFncYPC = QCheckBox("Points")
        self.qCheckBoxPrefFncYPC.setChecked(pointsPrefFncY)
        self.qCheckBoxPrefFncYPC.stateChanged.connect(eventFnc)

        # layoutToolPFY:QFormLayout
        layoutToolPFY = QFormLayout()
        layoutToolPFY.addRow(self.qCheckBoxPrefFncYPC)

        # qGroupBoxToolPFY:QGroupBox
        self.qGroupBoxToolPFY = QGroupBox("Pref. Fnc. Y")
        self.qGroupBoxToolPFY.setLayout(layoutToolPFY)