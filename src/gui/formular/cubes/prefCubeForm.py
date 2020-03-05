from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QComboBox, QLabel, QDoubleSpinBox, QGroupBox, QVBoxLayout, QCheckBox

class PrefCubeForm:
    def __init__(self, diagonalDC, showLabels, eventFnc):

        # qCheckBoxDiagonalPC:QCheckBox
        self.qCheckBoxDiagonalPC = QCheckBox("Diagonal")
        self.qCheckBoxDiagonalPC.setChecked(diagonalDC)
        self.qCheckBoxDiagonalPC.stateChanged.connect(eventFnc)

        # qCheckBoxPointLabelsPC:QCheckBox
        self.qCheckBoxPointLabelsPC = QCheckBox("Point Labels")
        self.qCheckBoxPointLabelsPC.setChecked(showLabels)
        self.qCheckBoxPointLabelsPC.stateChanged.connect(eventFnc)

        # layoutToolPC:QFormLayout
        layoutToolPC = QFormLayout()
        layoutToolPC.addRow(self.qCheckBoxDiagonalPC)
        layoutToolPC.addRow(self.qCheckBoxPointLabelsPC)

        # qGroupBoxToolPC:QGroupBox
        self.qGroupBoxToolPC = QGroupBox("Pref. Cube")
        self.qGroupBoxToolPC.setLayout(layoutToolPC)