from PyQt5.QtWidgets import QLabel

from userProfileModel.model.prefFnc.model.prefFncTroughModel import PrefFncTroughModel

from gui.formular.model.prefFnc.triangularForm.prefFncYTriangularForm import PrefFncYTriangularForm

from gui.formular.model.prefFnc.troughForm.prefFncXTroughForm import PrefFncXTroughForm



class PrefFncYTroughtForm:
    def __init__(self, iy, bottom, linPrefModelConf, eventFnc):

        prefFncYTriangularForm = PrefFncYTriangularForm(iy, linPrefModelConf, eventFnc)

        # qDoubleSpinBoxIdealY:QDoubleSpinBox
        self.qDoubleSpinBoxIdealY = prefFncYTriangularForm.qDoubleSpinBoxIdealY

        prefFncXTroughForm = PrefFncXTroughForm(iy, bottom, linPrefModelConf, eventFnc)

        # qDoubleSpinBoxBottom:QDoubleSpinBox
        self.qDoubleSpinBoxBottom = prefFncXTroughForm.qDoubleSpinBoxBottom

    def exportToLayout(self, layout):
        layout.addRow(QLabel("Ideal Y:"), self.qDoubleSpinBoxIdealY)
        layout.addRow(QLabel("Bottom:"), self.qDoubleSpinBoxBottom)

    def exportAsPrefFncYModel(self):
        iy = self.qDoubleSpinBoxIdealY.value()
        bottom = self.qDoubleSpinBoxBottom.value()
        return PrefFncTroughModel(iy, bottom)

#    def exportAsPrefFncY(self):
#        bottom = self.qDoubleSpinBoxBottom.value()
#        return PrefFncY([Point(0, 0), Point(self.ix - bottom/2, 1), Point(self.ix + bottom/2, 1), Point(self.linPrefModelConf.SIZE_X_DATA_CUBE, 0)])