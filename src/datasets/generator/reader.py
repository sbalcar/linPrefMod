#!/usr/bin/python3

import csv
import ast 
#import random
#from pydoc import locate

from datasets.rating import Rating #class

#from datasets.generator.datasetModelDescription import DatasetModelDescription #class

#from userProfileModel.prefFnc.prefFncRestriction import PrefFncRestriction #class

#from userProfileModel.prefFnc.model.aPrefFncModel import APrefFncModel #class
from userProfileModel.model.prefFnc.model.prefFncTriangularModel import PrefFncTriangularModel #class
from userProfileModel.model.prefFnc.model.prefFncRefractedModel import PrefFncRefractedModel #class
from userProfileModel.model.prefFnc.model.prefFncCategoricalModel import PrefFncCategoricalModel #class

from userProfileModel.model.aggrFnc.aggrFncND import AggrFncND #class

#from userProfileModel.user import UserND #class

from geometry.pointND import PointND #class
from geometry.pointNDWithID import PointNDWithID #class

from userProfileModel.userProfileModelDefinition import UserProfileModelDefinition #class


class Reader:

  # fileNameItems:str, fileNameRatings:str
  def read(fileNameItems, fileNameRatings, fileNameUsers):

    #items:List<PointNDWithID>
    items = Reader.__readItems(fileNameItems);

    #ratings:List<Rating>
    ratings = Reader.__readRatings(fileNameRatings)

    # users:List<UserProfileModelDefinition>
    users = Reader.__readUsers(fileNameUsers)

    #(List<PointNDWithID>, List<Rating>, List<UserProfileModelDefinition>)
    return (items, ratings, users)


  def __readItems(fileName):

    #items:PointNDWithID[]
    items = []
    with open(fileName, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        next(csvreader)

        # lineI:list
        for lineI in csvreader:
          iidI = int(lineI.pop(0))
          coordinatesI = [float(coordinateI) for coordinateI in lineI]
          # pointI:PointNDWithID
          pointI = PointNDWithID(PointND(coordinatesI), iidI)
          items.append(pointI)
    #items:PointNDWithID[]
    return items


  def __readRatings(fileName):

    #ratings:Rating[]
    ratings = []
    with open(fileName, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        next(csvreader)

        # lineI:list
        for lineI in csvreader:
          userID = int(lineI[0])
          itemID = int(lineI[1])
          rating = float(lineI[2])
          ratingI = Rating(userID, itemID, rating)
          ratings.append(ratingI)
    #ratings:Rating[]
    return ratings


  def __readUsers(fileName):

    #users:List<UserProfileModelDefinition>
    users = []
    with open(fileName, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')

        # extracting field names through first row
        next(csvreader)

        # lineI:list
        for lineI in csvreader:
          # userID:int
          userID = int(lineI.pop(0))
          dimensions = int(len(lineI)/2)
          #prefFncs:List<APrefFnc>
          prefFncs = []
          for i in range(dimensions):
            prefFncStrI = lineI.pop(0)
            prefFncI = Reader.__aaa(prefFncStrI)
            prefFncs.append(prefFncI)
          # aggr:AggrFncND
          aggr = AggrFncND([float(w) for w in lineI])
          # userI:UserProfileModelDefinition
          userI = UserProfileModelDefinition(userID, prefFncs, aggr)
          users.append(userI)
    #users:User<ProfileModelDefinition>
    return users

   
  def __aaa(prefFnc):
    class_ = prefFnc[:prefFnc.find('(')]
    args = prefFnc[prefFnc.find('(')+1:-1]

    if class_ == "PrefFncTriangularModel":
      iCoordinate = float(args)
      return PrefFncTriangularModel(iCoordinate)

    if class_ == "PrefFncRefractedModel":
      iCoordinate = float(args)
      return PrefFncRefractedModel(iCoordinate)

    if class_ == "PrefFncCategoricalModel":
      intervalsStr = args[:args.find(']')+1]
      # intervals:list<Tuple<float, float>
      intervals = ast.literal_eval(intervalsStr) 

      functionValuesStr = args[args.rfind('['):args.rfind(']')+1]
      # functionValues:list<float>
      functionValues = ast.literal_eval(functionValuesStr) 
      return PrefFncCategoricalModel(intervals, functionValues)




