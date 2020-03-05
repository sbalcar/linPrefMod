from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QComboBox, QLabel, QDoubleSpinBox, QGroupBox, QVBoxLayout, QCheckBox


class PrefFncXModelTypeForm:
    # modelTypeIndex:int, eventFnc:Fnc
    def __init__(self, modelTypeIndex, eventFnc):

        self.qComboBoxModelType = QComboBox()
        self.qComboBoxModelType.addItem("Triangular")
        self.qComboBoxModelType.addItem("Refracted")
        self.qComboBoxModelType.addItem("Trough")
        self.qComboBoxModelType.addItem("Categorical")
        self.qComboBoxModelType.addItem("Point Sequence")
        self.qComboBoxModelType.setCurrentIndex(modelTypeIndex)
        self.qComboBoxModelType.currentIndexChanged.connect(eventFnc)


    def exportToLayout(self, layout):
        layout.addRow(QLabel("Fnc. Type:"), self.qComboBoxModelType)
