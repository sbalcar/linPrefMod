from PyQt5.QtWidgets import QLabel, QDoubleSpinBox

from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc


class AggrFncForm:
    def __init__(self, wx, aggrLevel, linPrefModelConf, eventFnc):

        # qDoubleSpinBoxWeightX:QDoubleSpinBox
        self.qDoubleSpinBoxWeightX = QDoubleSpinBox();
        self.qDoubleSpinBoxWeightX.setValue(wx)
        self.qDoubleSpinBoxWeightX.setMinimum(0.05)
        self.qDoubleSpinBoxWeightX.setMaximum(0.95)
        self.qDoubleSpinBoxWeightX.setSingleStep(0.05)
        self.qDoubleSpinBoxWeightX.valueChanged.connect(eventFnc)

        # qDoubleSpinBoxContourLine:QDoubleSpinBox
        self.qDoubleSpinBoxContourLine = QDoubleSpinBox();
        self.qDoubleSpinBoxContourLine.setValue(aggrLevel)
        self.qDoubleSpinBoxContourLine.setMinimum(0.05)
        self.qDoubleSpinBoxContourLine.setMaximum(0.95)
        self.qDoubleSpinBoxContourLine.setSingleStep(0.05)
        self.qDoubleSpinBoxContourLine.valueChanged.connect(eventFnc)


    def exportToLayout(self, layout):

        layout.addRow(QLabel("Weight X:"), self.qDoubleSpinBoxWeightX)
        layout.addRow(QLabel("Contour Line:"), self.qDoubleSpinBoxContourLine)

    def export(self):
        wx = self.qDoubleSpinBoxWeightX.value()
        return AggrFnc([wx, 1 - wx])

    def exportAggrLevel(self):
        aggrLevel = self.qDoubleSpinBoxContourLine.value()
        return aggrLevel

