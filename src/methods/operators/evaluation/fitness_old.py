#!/usr/bin/python3

from sklearn.metrics import mean_squared_error
from math import sqrt


# uIndividual:IndividualUser, modelConf:LinPrefModelConfiguration, pointsTrain:Point[], prefsTrain:Point[]
def fitnessRMSE_(uIndividual, modelConf, pointsTrain, prefsTrain):

    #userProfileModel = uIndividual.exportUserProfileTriangularModel()
    userProfileModel = uIndividual.exportUserProfileRefractedModel()
    #userProfileModel.print()

    # pointsPrefCubeTrain:Point[]
    pointsPrefCubeTrain = userProfileModel.pointsDataCubeToPointsPrefCube(pointsTrain);

    # prefsPointsPrefCubeTrain:Point[]
    prefsPointsPrefCubeTrain = userProfileModel.preferenceOfPointsInPC(pointsPrefCubeTrain, modelConf);

    fitnessRMSETrain = rmse(prefsPointsPrefCubeTrain, prefsTrain)
    #print("fitnessRMSETrain: ", fitnessRMSETrain);

    return fitnessRMSETrain;


# preferences1:float[], preferences2:float[]
def rmse(preferences1, preferences2):
  rmse = sqrt(mean_squared_error(preferences1, preferences2))
  # rmse:float
  return rmse;
