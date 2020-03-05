from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QComboBox, QLabel, QDoubleSpinBox, QGroupBox, QVBoxLayout, QCheckBox

class AuxLineForm:
    def __init__(self, auxiliaryLinesDataCube, auxiliaryLinesPrefCube,
                 auxiliaryLinesPrefFncXCube, auxiliaryLinesPrefFncYCube, eventFnc):

        # qCheckBoxAuxLineDC:QCheckBox
        self.qCheckBoxAuxLineDC = QCheckBox("Data Cube")
        self.qCheckBoxAuxLineDC.setChecked(auxiliaryLinesDataCube)
        self.qCheckBoxAuxLineDC.stateChanged.connect(eventFnc)

        # qCheckBoxAuxLinePC:QCheckBox
        self.qCheckBoxAuxLinePC = QCheckBox("Pref Cube")
        self.qCheckBoxAuxLinePC.setChecked(auxiliaryLinesPrefCube)
        self.qCheckBoxAuxLinePC.stateChanged.connect(eventFnc)

        # qCheckBoxAuxLinePXC:QCheckBox
        self.qCheckBoxAuxLinePXC = QCheckBox("PrefFncX Cube")
        self.qCheckBoxAuxLinePXC.setChecked(auxiliaryLinesPrefFncXCube)
        self.qCheckBoxAuxLinePXC.stateChanged.connect(eventFnc)

        # qCheckBoxAuxLinePYC:QCheckBox
        self.qCheckBoxAuxLinePYC = QCheckBox("PrefFncY Cube")
        self.qCheckBoxAuxLinePYC.setChecked(auxiliaryLinesPrefFncYCube)
        self.qCheckBoxAuxLinePYC.stateChanged.connect(eventFnc)

        # layoutTool:QFormLayout
        layoutTool = QFormLayout()
        layoutTool.addRow(self.qCheckBoxAuxLineDC)
        layoutTool.addRow(self.qCheckBoxAuxLinePC)
        layoutTool.addRow(self.qCheckBoxAuxLinePXC)
        layoutTool.addRow(self.qCheckBoxAuxLinePYC)

        # qGroupBox:QGroupBox
        self.qGroupBoxTool = QGroupBox("Auxiliary Lines")
        self.qGroupBoxTool.setLayout(layoutTool)
