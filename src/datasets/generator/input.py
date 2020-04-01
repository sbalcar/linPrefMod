#!/usr/bin/python3

from datasets.generator.datasetModelDescription import DatasetModelDescription #class

from userProfileModel.model.prefFnc.prefFncRestriction import PrefFncRestriction #class

from userProfileModel.model.prefFnc.model.prefFncTriangularModel import PrefFncTriangularModel #class
from userProfileModel.model.prefFnc.model.prefFncRefractedModel import PrefFncRefractedModel #class
from userProfileModel.model.prefFnc.model.prefFncCategoricalModel import PrefFncCategoricalModel #class
import os

class InputOfGenerator:

  def input01():
     print("input01")

     # NUMBER_OF_DIMENSIONS:int
     NUMBER_OF_DIMENSIONS = 3;

     NUMBER_OF_USERS = 300;

     NUMBER_OF_ITEM_CLUSTERS = 10;
     NUMBER_OF_ITEMS_IN_CLUSTER = 100;
     RADIUS_OF_CIRCLE = 0.2   

     MAX_NUMBER_OF_ITEMS_FOR_USER = 50

     # fileNameUsers:str
     fileNameUsers = ".." + os.sep + "datasets" + os.sep + "usersMy.csv"
     fileNameItems = ".." + os.sep + "datasets" + os.sep + "itemsMy.csv"
     fileNameRatings = ".." + os.sep + "datasets" + os.sep + "ratingsMy.csv"

     # restr1:APrefFncModel
     restr1 = PrefFncRestriction(PrefFncTriangularModel, "generate", None)
     restr2 = PrefFncRestriction(PrefFncRefractedModel, "generate", None)
     restr3 = PrefFncRestriction(PrefFncCategoricalModel, "generate", 4)
     # restrs:List<APrefFncModel>
     restrs = [restr1, restr2, restr3]

     # dModelDesr:DatasetModelDescription
     dModelDesr = DatasetModelDescription(restrs)
     dModelDesr.numberOfDimensions = NUMBER_OF_DIMENSIONS

     dModelDesr.numberOfUsers = NUMBER_OF_USERS

     dModelDesr.numberOfItemClusters = NUMBER_OF_ITEM_CLUSTERS
     dModelDesr.numberOfItemsInCluster = NUMBER_OF_ITEMS_IN_CLUSTER
     dModelDesr.radiusOfCircle = RADIUS_OF_CIRCLE

     dModelDesr.maxNumberOfItemsForUser = MAX_NUMBER_OF_ITEMS_FOR_USER

     dModelDesr.fileNameUsers = fileNameUsers
     dModelDesr.fileNameItems = fileNameItems
     dModelDesr.fileNameRatings = fileNameRatings

     # DatasetModelDescription
     return dModelDesr;


