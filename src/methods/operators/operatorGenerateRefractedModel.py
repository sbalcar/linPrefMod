#!/usr/bin/python3

from methods.individual.individualUserProfileModel import IndividualUserProfileModel #class

from userProfileModel.userProfileModel import UserProfileModel #class
from userProfileModel.model.prefFnc.model.prefFncRefractedModel import PrefFncRefractedModel #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class

# linPrefModelConf:LinPrefModelConfiguration
def operatorGenerateRefractedModel(linPrefModelConf):

    prefFncX = PrefFncRefractedModel.generate(None).exportAsPrefFncX(linPrefModelConf)
    prefFncY = PrefFncRefractedModel.generate(None).exportAsPrefFncY(linPrefModelConf)
    aggrFnc = AggrFnc.generate()

    # upModel:UserProfileModel
    upModel = UserProfileModel(prefFncX, prefFncY, aggrFnc)

    # IndividualUserTrinity
    return IndividualUserProfileModel(upModel)