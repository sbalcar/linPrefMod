
from gui.formular.model.prefFnc.categoricalForm.prefFncXCategoricalForm import PrefFncXCategoricalForm


class PrefFncYCategoricalForm(PrefFncXCategoricalForm):

    # intervals:list<Tuple<float, float>>, functionValues:list<float>
    def __init__(self, intervals, functionValues, linPrefModelConf, eventFnc):
       super().__init__(intervals, functionValues, linPrefModelConf, eventFnc)

    def exportAsPrefFncYModel(self):
        return self.exportAsPrefFncXModel()