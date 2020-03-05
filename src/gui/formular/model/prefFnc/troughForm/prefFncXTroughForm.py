from PyQt5.QtWidgets import QLabel, QDoubleSpinBox

from gui.formular.model.prefFnc.triangularForm.prefFncXTriangularForm import PrefFncXTriangularForm
from userProfileModel.model.prefFnc.model.prefFncTroughModel import PrefFncTroughModel


class PrefFncXTroughForm:
    def __init__(self, ix, bottom, linPrefModelConf, eventFnc):

        prefFncXTriangularForm = PrefFncXTriangularForm(ix, linPrefModelConf, eventFnc)

        # qDoubleSpinBoxIdealX:QDoubleSpinBox
        self.qDoubleSpinBoxIdealX = prefFncXTriangularForm.qDoubleSpinBoxIdealX

        # qDoubleSpinBoxIdealX:QDoubleSpinBox
        self.qDoubleSpinBoxBottom = QDoubleSpinBox();
        self.qDoubleSpinBoxBottom.setValue(bottom)
        self.qDoubleSpinBoxBottom.setMinimum(0)
        self.qDoubleSpinBoxBottom.setMaximum(linPrefModelConf.SIZE_X_DATA_CUBE)
        self.qDoubleSpinBoxBottom.setSingleStep(0.05)
        self.qDoubleSpinBoxBottom.valueChanged.connect(eventFnc)

    def exportToLayout(self, layout):
        layout.addRow(QLabel("Ideal X:"), self.qDoubleSpinBoxIdealX)
        layout.addRow(QLabel("Bottom:"), self.qDoubleSpinBoxBottom)

    def exportAsPrefFncXModel(self):
        ix = self.qDoubleSpinBoxIdealX.value()
        bottom = self.qDoubleSpinBoxBottom.value()
        return PrefFncTroughModel(ix, bottom)

#    def exportAsPrefFncX(self):
#        #bottom = self.qDoubleSpinBoxBottom.value()
#        bottom = self.bottom
#        return PrefFncX([Point(0, 0), Point(self.ix -bottom/2, 1), Point(self.ix +bottom/2, 1), Point(self.linPrefModelConf.SIZE_X_DATA_CUBE, 0)])