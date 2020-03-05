from PyQt5.QtWidgets import QLabel

from userProfileModel.model.prefFnc.model.prefFncRefractedModel import PrefFncRefractedModel

from gui.formular.model.prefFnc.triangularForm.prefFncYTriangularForm import PrefFncYTriangularForm


class PrefFncYRefractedForm:
    def __init__(self, iy, linPrefModelConf, eventFnc):

        prefFncYTriangularForm = PrefFncYTriangularForm(iy, linPrefModelConf, eventFnc)

        # qDoubleSpinBoxIdealY:QDoubleSpinBox
        self.qDoubleSpinBoxIdealY = prefFncYTriangularForm.qDoubleSpinBoxIdealY

    def exportToLayout(self, layout):
        layout.addRow(QLabel("Ideal Y:"), self.qDoubleSpinBoxIdealY)

    def exportAsPrefFncYModel(self):
        iy = self.qDoubleSpinBoxIdealY.value()
        return PrefFncRefractedModel(iy)

#    def exportAsPrefFncY(self):
#
#        lineSegments = self.exportIntervals();
#        # +30 in domain of a function -> +10 in range
#        # +50 in domain of a function -> +80 in range
#        # +20 in domain of a function -> +10 in range
#        segmentation = [Pair(10, 30), Pair(80, 50), Pair(10, 20)]
#        # refractedPrefFnc:LineSegment[]
#        refractedPrefFnc = []
#        for lineSegmI in lineSegments.lineSegments:
#            # s:LineSegment[]
#            s = []
#            if lineSegmI.isDecreasingOnX():
#                s = lineSegmI.exportSegmentation(segmentation)
#            else:
#                s = lineSegmI.exportSegmentation(segmentation[::-1])
#            refractedPrefFnc = refractedPrefFnc + s
#
#        r = PrefFncY([]);
#        r.constructor(refractedPrefFnc)
#        # PrefFncX
#        return r;