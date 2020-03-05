from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QComboBox, QLabel, QDoubleSpinBox, QGroupBox, QVBoxLayout, QCheckBox

class DataCubeForm:
    def __init__(self, contourLineDC, pointLabelsDC, eventFnc):

        # qCheckBoxAuxLinePYC:QCheckBox
        self.qCheckBoxContourLineDC = QCheckBox("Contour Lines")
        self.qCheckBoxContourLineDC.setChecked(contourLineDC)
        self.qCheckBoxContourLineDC.stateChanged.connect(eventFnc)

        # qCheckBoxPointLabelsDC:QCheckBox
        self.qCheckBoxPointLabelsDC = QCheckBox("Point Labels")
        self.qCheckBoxPointLabelsDC.setChecked(pointLabelsDC)
        self.qCheckBoxPointLabelsDC.stateChanged.connect(eventFnc)

        # layoutToolDC:QFormLayout
        layoutToolDC = QFormLayout()
        layoutToolDC.addRow(self.qCheckBoxContourLineDC)
        layoutToolDC.addRow(self.qCheckBoxPointLabelsDC)

        # qGroupBoxToolDC:QGroupBox
        self.qGroupBoxToolDC = QGroupBox("Data Cube")
        self.qGroupBoxToolDC.setLayout(layoutToolDC)