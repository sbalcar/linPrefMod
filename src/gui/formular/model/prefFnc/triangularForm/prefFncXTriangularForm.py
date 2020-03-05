from PyQt5.QtWidgets import QLabel, QDoubleSpinBox

from userProfileModel.model.prefFnc.model.prefFncTriangularModel import PrefFncTriangularModel


class PrefFncXTriangularForm:
    def __init__(self, ix, linPrefModelConf, eventFnc):

        self.linPrefModelConf = linPrefModelConf

        # qDoubleSpinBoxIdealX:QDoubleSpinBox
        self.qDoubleSpinBoxIdealX = QDoubleSpinBox();
        self.qDoubleSpinBoxIdealX.setValue(ix)
        self.qDoubleSpinBoxIdealX.setMinimum(0)
        self.qDoubleSpinBoxIdealX.setMaximum(linPrefModelConf.SIZE_X_DATA_CUBE)
        self.qDoubleSpinBoxIdealX.setSingleStep(0.05)
        self.qDoubleSpinBoxIdealX.valueChanged.connect(eventFnc)

    def exportToLayout(self, layout):
        layout.addRow(QLabel("Ideal X:"), self.qDoubleSpinBoxIdealX)

    def exportAsPrefFncXModel(self):
        ix = self.qDoubleSpinBoxIdealX.value()
        return PrefFncTriangularModel(ix)