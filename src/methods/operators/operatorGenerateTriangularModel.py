#!/usr/bin/python3

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from methods.individual.individualUserProfileModel import IndividualUserProfileModel #class

from userProfileModel.userProfileModel import UserProfileModel #class
from userProfileModel.model.prefFnc.model.prefFncTriangularModel import PrefFncTriangularModel #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class

# linPrefModelConf:LinPrefModelConfiguration
def operatorGenerateTriangularModel(linPrefModelConf:LinPrefModelConfiguration):

    prefFncX = PrefFncTriangularModel.generate(None).exportAsPrefFncX(linPrefModelConf)
    prefFncY = PrefFncTriangularModel.generate(None).exportAsPrefFncY(linPrefModelConf)
    aggrFnc = AggrFnc.generate()

    # upModel:UserProfileModel
    upModel = UserProfileModel(prefFncX, prefFncY, aggrFnc)

    # IndividualUserTrinity
    return IndividualUserProfileModel(upModel)
