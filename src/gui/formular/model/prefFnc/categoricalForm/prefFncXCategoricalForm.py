from PyQt5.QtWidgets import QLabel, QDoubleSpinBox, QHBoxLayout

from userProfileModel.model.prefFnc.model.prefFncCategoricalModel import PrefFncCategoricalModel


class PrefFncXCategoricalForm:
    # intervals:list<Tuple<float, float>>, functionValues:list<float>
    def __init__(self, intervals, functionValues, linPrefModelConf, eventFnc):

        # qDoubleSpinBoxNumberOfIntervals:QDoubleSpinBox
        self.qDoubleSpinBoxNumberOfIntervals = QDoubleSpinBox()
        self.qDoubleSpinBoxNumberOfIntervals.setValue(len(intervals))
        self.qDoubleSpinBoxNumberOfIntervals.setMinimum(2)
        self.qDoubleSpinBoxNumberOfIntervals.setMaximum(10)
        self.qDoubleSpinBoxNumberOfIntervals.setSingleStep(1)
        self.qDoubleSpinBoxNumberOfIntervals.valueChanged.connect(eventFnc)

        self.categoryForms = []
        for i in range(len(intervals)):
            cI = CategoryForm(i, intervals[i][0], intervals[i][1], functionValues[i],
                              self.categoryForms, linPrefModelConf, eventFnc)
            self.categoryForms.append(cI)

    def exportToLayout(self, layout):
        layout.addRow(QLabel("Categories:"), self.qDoubleSpinBoxNumberOfIntervals)

        for categoryFormI in self.categoryForms:
            categoryFormI.exportToLayout(layout)

    def exportAsPrefFncXModel(self):
        intervals = [(formI.qDoubleSpinBoxMin.value(), formI.qDoubleSpinBoxMax.value())
                     for formI in self.categoryForms]
        fncValues = [formI.qDoubleSpinBoxFncValue.value() for formI in self.categoryForms]

        numberOfIntervals = int(self.qDoubleSpinBoxNumberOfIntervals.value())

        intervals.extend( [(1.0,1.0)]*(numberOfIntervals -len(intervals)) )
        fncValues.extend( [1.0]*(numberOfIntervals -len(fncValues)) )
        intervals = intervals[0:numberOfIntervals]
        fncValues = fncValues[0:numberOfIntervals]

        #print(intervals)
        return PrefFncCategoricalModel(intervals, fncValues)



class CategoryForm:
    # intervalId:float, min:float, max:float, functionValue:float, neighborForms:list<CategoryForm>, linPrefModelConf:LinPrefModelConf, eventFnc:Fnc
    def __init__(self, intervalId, min, max, fncValue, neighborForms, linPrefModelConf, eventFnc):
        # intervalId:int
        self.intervalId = intervalId
        # min: float
        self.min = min
        # max:float
        self.max = max
        # functionValue: float
        self.fncValue = fncValue
        # neighborForms:list<CategoryForm>
        self.neighborForms = neighborForms
        # eventFnc:Fnc
        self.eventFnc = eventFnc

        # qDoubleSpinBoxMin:QDoubleSpinBox
        self.qDoubleSpinBoxMin = QDoubleSpinBox()
        self.qDoubleSpinBoxMin.setValue(min)
        self.qDoubleSpinBoxMin.setMinimum(0)
        self.qDoubleSpinBoxMin.setMaximum(1)
        self.qDoubleSpinBoxMin.setSingleStep(0.05)
        self.qDoubleSpinBoxMin.valueChanged.connect(self.clickEvent)

        # qDoubleSpinBoxMax:QDoubleSpinBox
        self.qDoubleSpinBoxMax = QDoubleSpinBox()
        self.qDoubleSpinBoxMax.setValue(max)
        self.qDoubleSpinBoxMax.setMinimum(0)
        self.qDoubleSpinBoxMax.setMaximum(1)
        self.qDoubleSpinBoxMax.setSingleStep(0.05)
        self.qDoubleSpinBoxMax.valueChanged.connect(self.clickEvent)

        # qDoubleSpinBoxFncValue:QDoubleSpinBox
        self.qDoubleSpinBoxFncValue = QDoubleSpinBox()
        self.qDoubleSpinBoxFncValue.setValue(fncValue)
        self.qDoubleSpinBoxFncValue.setMinimum(0)
        self.qDoubleSpinBoxFncValue.setMaximum(1)
        self.qDoubleSpinBoxFncValue.setSingleStep(0.05)
        self.qDoubleSpinBoxFncValue.valueChanged.connect(eventFnc)


    def exportToLayout(self, layout):
        qHBoxLayout =  QHBoxLayout()
        qHBoxLayout.addWidget(self.qDoubleSpinBoxMin)
        qHBoxLayout.addWidget(self.qDoubleSpinBoxMax)

        layout.addRow(QLabel("Interval " + str(self.intervalId) + ":"), qHBoxLayout)
        layout.addRow(QLabel("Fnc:"), self.qDoubleSpinBoxFncValue)

    def clickEvent(self, event):

        self.min = self.qDoubleSpinBoxMin.value()
        self.max = self.qDoubleSpinBoxMax.value()

        if self.intervalId != 0:
            fomrmPrev = self.neighborForms[self.intervalId -1]
            fomrmPrev.qDoubleSpinBoxMax.setValue(self.min)

        if self.intervalId != len(self.neighborForms) -1:
            fomrmNext = self.neighborForms[self.intervalId +1]
            fomrmNext.qDoubleSpinBoxMin.setValue(self.max)

        self.eventFnc(event)