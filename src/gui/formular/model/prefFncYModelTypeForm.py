from PyQt5.QtWidgets import QLabel

from gui.formular.model.prefFncXModelTypeForm import PrefFncXModelTypeForm

class PrefFncYModelTypeForm:
    # modelTypeIndex:int, eventFnc:Fnc
    def __init__(self, modelTypeIndex, eventFnc):
        prefFncXModelTypeForm = PrefFncXModelTypeForm(modelTypeIndex, eventFnc)
        self.qComboBoxModelType = prefFncXModelTypeForm.qComboBoxModelType

    def exportToLayout(self, layout):
        layout.addRow(QLabel("Fnc. Type:"), self.qComboBoxModelType)