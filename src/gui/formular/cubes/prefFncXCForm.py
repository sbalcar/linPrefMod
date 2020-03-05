from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QComboBox, QLabel, QDoubleSpinBox, QGroupBox, QVBoxLayout, QCheckBox

class PrefFncXCForm:
    def __init__(self, pointsPrefFncX, eventFnc):

        # qCheckBoxPrefFncXC:QCheckBox
        self.qCheckBoxPrefFncXC = QCheckBox("Points")
        self.qCheckBoxPrefFncXC.setChecked(pointsPrefFncX)
        self.qCheckBoxPrefFncXC.stateChanged.connect(eventFnc)

        # layoutToolPFX:QFormLayout
        layoutToolPFX = QFormLayout()
        layoutToolPFX.addRow(self.qCheckBoxPrefFncXC)

        # qGroupBoxToolPFX:QGroupBox
        self.qGroupBoxToolPFX = QGroupBox("Pref. Fnc. X")
        self.qGroupBoxToolPFX.setLayout(layoutToolPFX)