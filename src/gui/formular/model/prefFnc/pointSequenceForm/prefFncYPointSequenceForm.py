from userProfileModel.model.prefFnc.model.prefFncPointSequenceModel import PrefFncPointSequenceModel

from gui.formular.model.prefFnc.pointSequenceForm.prefFncXPointSequenceForm import PrefFncXPointSequenceForm

from geometry.points import Points #class


class PrefFncYPointSequenceForm(PrefFncXPointSequenceForm):
    # pointsList:list<Point>, linPrefModelConf:LinPrefModelConf, eventFnc:Fnc
    def __init__(self, pointsList, linPrefModelConf, eventFnc):
        super().__init__(pointsList, linPrefModelConf, eventFnc)


    def exportAsPrefFncYModel(self):
        # points:Points
        points = Points.importAsString(self.qLineEditPoints.text())

        # PrefFncPointSequenceModel
        return PrefFncPointSequenceModel(points.points)