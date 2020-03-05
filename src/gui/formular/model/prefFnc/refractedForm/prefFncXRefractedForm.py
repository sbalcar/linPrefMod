from PyQt5.QtWidgets import QLabel

from userProfileModel.model.prefFnc.model.prefFncRefractedModel import PrefFncRefractedModel

from gui.formular.model.prefFnc.triangularForm.prefFncXTriangularForm import PrefFncXTriangularForm


class PrefFncXRefractedForm:
    def __init__(self, ix, linPrefModelConf, eventFnc):

        prefFncXTriangularForm = PrefFncXTriangularForm(ix, linPrefModelConf, eventFnc)

        # qDoubleSpinBoxIdealX:QDoubleSpinBox
        self.qDoubleSpinBoxIdealX =prefFncXTriangularForm.qDoubleSpinBoxIdealX

    def exportToLayout(self, layout):
        layout.addRow(QLabel("Ideal X:"), self.qDoubleSpinBoxIdealX)

    def exportAsPrefFncXModel(self):
        ix = self.qDoubleSpinBoxIdealX.value()
        return PrefFncRefractedModel(ix)


#    def exportAsPrefFncX(self):
#
#        lineSegments = self.exportIntervals();
#        # +30 in domain of a function -> +10 in range
#        # +50 in domain of a function -> +80 in range
#        # +20 in domain of a function -> +10 in range
#        segmentation = [Pair(30, 10), Pair(50, 80), Pair(20, 10)]
#        # refractedPrefFnc:LineSegment[]
#        refractedPrefFnc = []
#        for lineSegmI in lineSegments.lineSegments:
#            # s:LineSegment[]
#            s = []
#            if lineSegmI.isDecreasingOnY():
#                s = lineSegmI.exportSegmentation(segmentation)
#            else:
#                s = lineSegmI.exportSegmentation(segmentation[::-1])
#            refractedPrefFnc = refractedPrefFnc + s
#
#        r = PrefFncX([])
#        r.constructor(refractedPrefFnc)
#        # PrefFncX
#        return r;
