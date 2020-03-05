#!/usr/bin/python3

from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc
from userProfileModel.model.prefFnc.model.aPrefFncModel import APrefFncModel
from userProfileModel.userProfileModel import UserProfileModel


class UserProfileModelStructured:
    # prefFncXModel:PrefFncTriangularModel, prefFncYModel:PrefFncTriangularModel, aggregation:AggrFnc
    def __init__(self, prefFncXModel, prefFncYModel, aggrFnc):
        if not isinstance(prefFncXModel, APrefFncModel):
            raise ValueError("Argument prefFncX isn't type APrefFncModel.")
        if not isinstance(prefFncYModel, APrefFncModel):
            raise ValueError("Argument prefFncY isn't type PrefFncTriangularModel.")
        if type(aggrFnc) is not AggrFnc:
            raise ValueError("Argument aggregation isn't type AggrFnc.")
        self.prefFncXModel = prefFncXModel
        self.prefFncYModel = prefFncYModel
        self.aggrFnc = aggrFnc


    def exportAsUserProfileModel(self, linPrefModelConf):

        # prefFncX:PrefFncX
        prefFncX = self.prefFncXModel.exportAsPrefFncX(linPrefModelConf)
        # prefFncY:PrefFncY
        prefFncY = self.prefFncYModel.exportAsPrefFncY(linPrefModelConf)

        return UserProfileModel(prefFncX, prefFncY, self.aggrFnc)