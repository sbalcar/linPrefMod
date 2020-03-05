#!/usr/bin/python3

import csv
import random

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from userProfileModel.userProfileModelDefinition import UserProfileModelDefinition #class

from datasets.rating import Rating #class
from datasets.generator.input import InputOfGenerator #class
from datasets.generator.datasetModelDescription import DatasetModelDescription #class

from userProfileModel.model.aggrFnc.aggrFncND import AggrFncND #class

from geometry.pointND import PointND #class
from geometry.pointNDWithID import PointNDWithID #class

import json

def generate__():
  # initialising dictionary 
  test1 = { "testname" : "akshat", 
            "test2name" : "manjeet", 
            "test3name" : "nikhil"} 
  test1 = PointND([0.5, 0.4])  

  # print original dictionary 
  print (type(test1)) 
  print ("initial dictionary = ", test1) 
  
  # convert dictionary into string 
  # using json.dumps() 
  result = json.dumps(test1.__dict__) 
  
  # printing result as string 
  print ("\n", type(result)) 
  print ("final string = ", result)

  d = json.loads(result)
  #print(d["testname"])
  print(d)


def generate():
   # dmDescription:DatasetModelDescription
   dmDescription = InputOfGenerator.input01()   

   # gUsers:GeneratorOfUsers
   gUsers = GeneratorOfUsers()
   # upModelsDefs:List<UserProfileModelDefinition>
   upModelsDefs = gUsers.generateUsers(dmDescription)
   gUsers.writeUsers(upModelsDefs, dmDescription.fileNameUsers)


   # gItems:GeneratorOfItems
   gItems = GeneratorOfItems()
   # pointNDWithIDs:List<PointNDWithID>
   pointsNDWithIDs = gItems.generateItems(dmDescription)
   gItems.writeItems(pointsNDWithIDs, dmDescription.fileNameItems)

   # gRatings:GeneratorOfRatings
   gRatings = GeneratorOfRatings()
   # ratings:List<Rating>
   ratings = gRatings.generateRatings(dmDescription, upModelsDefs, pointsNDWithIDs)
   gRatings.writeRatings(ratings, dmDescription.fileNameRatings)



class GeneratorOfUsers:

  # dmDescription:DatasetModelDescription
  def generateUsers(self, dmDescription):
     if type(dmDescription) is not DatasetModelDescription:
        raise ValueError("Argument dmDescription isn't type DatasetModelDescription.")

     # numberOfUsers:int
     numberOfUsers = dmDescription.numberOfUsers

     # pfRestrs:List<PrefFncRestriction>
     pfRestrs = dmDescription.prefFncRestrs

     ## numberOfDimensions:int
     #numberOfDimensions = len(pfRestrs)

     # upmDefs:List<UserProfileModelDefinition>
     upmDefs = [self.__generateUser(userIdI, pfRestrs) for userIdI in range(1, numberOfUsers+1)]
      
     # List<UserProfileModelDefinition>
     return upmDefs;

  # userID:int, pfRestrictions:List<PrefFncRestriction>
  def __generateUser(self, userID, pfRestrictions):
    
     # prefFncs:PrefFnc[] 
     prefFncs = [pfRestrI.generate() for pfRestrI in pfRestrictions]

     # numberOfDimensions:float
     numberOfDimensions = len(prefFncs)

     # aggregation:AggrFncND
     aggrFnc = AggrFncND(self.__generateWeights(numberOfDimensions))

     return UserProfileModelDefinition(userID, prefFncs, aggrFnc)

  # numberOfDimensions:int
  def __generateWeights(self, numberOfDimensions):
     # intervals:float[]
     intervalsMax = [random.random() for i in range(numberOfDimensions)]
     intervalsMax.sort()

     intervalsMin = [0.0] + intervalsMax
     intervalsMin.pop()

     # float[]
     return [intervalI[1] -intervalI[0] for intervalI in zip(intervalsMin, intervalsMax)]

  # userProfileModelDefs:List<UserProfileModelDefinition>, fileName:str
  def writeUsers(self, userProfileModelDefs, fileName):

     dimension = userProfileModelDefs[0].dimension();
     chars = [chr(x) for x in range(65, 123)]

     header = ['"UID"'];
     for i in range(dimension):
       header.append("I" + chars[i])
     for i in range(dimension):
       header.append("P" + chars[i])

     # lines:list<list<str>>
     lines = [upModelDefI.exportAsList() for upModelDefI in userProfileModelDefs]

     # writing to csv file 
     with open(fileName, 'w') as csvfile: 
       # creating a csv writer object 
       csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
       csvwriter.writerow(header)

       for lineI in lines:
         csvwriter.writerow(lineI)


class GeneratorOfItems:

  # dmDescription:DatasetModelDescription
  def generateItems(self, dmDescription):
     if type(dmDescription) is not DatasetModelDescription:
        raise ValueError("Argument dmDescription isn't type DatasetModelDescription.")

     # numberOfDimensions:int
     numberOfDimensions = dmDescription.numberOfDimensions

     # numberOfItemClusters:int
     numberOfItemClusters = dmDescription.numberOfItemClusters
     numberOfItemsInCluster = dmDescription.numberOfItemsInCluster
     radiusOfCircle = dmDescription.radiusOfCircle

     # pointNDs:PointND[]
     pointNDs = []
     for itemIdI in range(numberOfItemClusters):
        # pointNDI:PointND
        pointNDI = PointND.generate(numberOfDimensions)
        pointNDs.append(pointNDI)
        # neighboursI:Point[]
        neighboursI = pointNDI.generateNeighbours(numberOfItemsInCluster -1, radiusOfCircle)
        pointNDs.extend(neighboursI);   

     #PointNDWithID[]
     return [PointNDWithID(pairI[1], pairI[0]) for pairI in zip(range(1, len(pointNDs) +1), pointNDs)]

  # pointsNDWithIDs:PointNDWithID[], fileName:str
  def writeItems(self, pointsNDWithIDs, fileName):

     dimension = pointsNDWithIDs[0].dimension();
     chars = [chr(x) for x in range(65, 123)]

     header = ['"IID"'];
     for i in range(dimension):
       header.append(chars[i])

     lines = [pointNDWithIDI.exportAsList() for pointNDWithIDI in pointsNDWithIDs]

     # writing to csv file 
     with open(fileName, 'w') as csvfile: 
       # creating a csv writer object 
       csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
       csvwriter.writerow(header)

       for lineI in lines:
         csvwriter.writerow(lineI)


class GeneratorOfRatings:

  # dmDescription:DatasetModelDescription, upModelsDefs:List<UserProfileModelDefinition>, pointNDWithIDs:PointNDWithID
  def generateRatings(self, dmDescription, upModelsDefs, pointNDWithIDs):
     if type(dmDescription) is not DatasetModelDescription:
        raise ValueError("Argument dmDescription isn't type DatasetModelDescription.")
     if type(upModelsDefs) is not list:
        raise ValueError("Argument userProfileNDs isn't type list.")
     for upModelsDefI in upModelsDefs:
        if type(upModelsDefI) is not UserProfileModelDefinition:
           raise ValueError("Argument userProfileNDs don't contain UserProfileModelDefinition.")

     # ratings:list<float>
     ratings = []

     # upModelsDefI:UserProfileModelDefinition
     for upModelsDefI in upModelsDefs:
        # ratingI:float
        ratingI = self. __generateRatings(dmDescription, upModelsDefI, pointNDWithIDs)
        ratings.extend(ratingI)

     # list<float>
     return ratings;


  # dmDescription:DatasetModelDescription, upModelsDef:UserProfileModelDefinition, pointNDWithIDs:PointNDWithID
  def __generateRatings(self, dmDescription, upModelsDef, pointNDWithIDs):
     # upModel:UserProfileModelND
     upModel= upModelsDef.exportUserProfileModelND()

     # points:list<PointND>
     points = [pointI.point for pointI in pointNDWithIDs]

     #linPrefModelConf:LinPrefModelConfiguration
     linPrefModelConf = LinPrefModelConfiguration(1.0, 1.0, 1.0, 1.0)

     # ratingValues:List<float>
     ratingValues = upModel.preferenceOfPointsInDataCube(points, linPrefModelConf)

     # ratings:List<Rating>
     ratings = [Rating(upModelsDef.userID, pointNDWithIDs[i].pointID, ratingValues[i]) for i in range(len(ratingValues))]
     
     return ratings;


  # ratings:List<Rating>, fileName:str
  def writeRatings(self, ratings, fileName):

     header = ['"UID"', '"IID"', '"RATING"'];

     lines = [ratingI.exportAsList() for ratingI in ratings]

     # writing to csv file 
     with open(fileName, 'w') as csvfile: 
       # creating a csv writer object 
       csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
       csvwriter.writerow(header)

       for lineI in lines:
         csvwriter.writerow(lineI)

