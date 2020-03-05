from PyQt5.QtWidgets import QLabel, QDoubleSpinBox

from userProfileModel.model.prefFnc.model.prefFncTriangularModel import PrefFncTriangularModel


class PrefFncYTriangularForm:
    def __init__(self, iy, linPrefModelConf, eventFnc):

        # qDoubleSpinBoxIdealY:QDoubleSpinBox
        self.qDoubleSpinBoxIdealY = QDoubleSpinBox();
        self.qDoubleSpinBoxIdealY.setValue(iy)
        self.qDoubleSpinBoxIdealY.setMinimum(0)
        self.qDoubleSpinBoxIdealY.setMaximum(linPrefModelConf.SIZE_Y_DATA_CUBE)
        self.qDoubleSpinBoxIdealY.setSingleStep(0.05)
        self.qDoubleSpinBoxIdealY.valueChanged.connect(eventFnc)


    def exportToLayout(self, layout):
        layout.addRow(QLabel("Ideal Y:"), self.qDoubleSpinBoxIdealY)

    def exportAsPrefFncYModel(self):
        iy = self.qDoubleSpinBoxIdealY.value()
        return PrefFncTriangularModel(iy)


#    def exportAsPrefFncY(self):
#        return PrefFncY([Point(0, 0), Point(1, self.iy), Point(0, self.linPrefModelConf.SIZE_Y_DATA_CUBE)])
