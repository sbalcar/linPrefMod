#!/usr/bin/python3

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from datasets.datasets import readItems #function
from datasets.datasets import readUsers #function
from datasets.datasets import Rating #class
from datasets.datasets import readRatings #function
from datasets.datasets import writeRatings #function

import os


def convertRefractedModelToTrianularModel():

    #modelConf:LinPrefModelConfiguration
    modelConf = LinPrefModelConfiguration(1.0, 1.0, 1.0, 1.0)

    # usersAll:User[]
    usersAll = readUsers();
    #print("usersAll: ", len(usersAll))

    # fileNameRatings:String
    fileNameRatings = ".." + os.sep + "datasets" + os.sep + "ratingsRefractedModel.csv"
    # ratingsAll:Rating[]
    ratingsAll = readRatings(fileNameRatings);
    #print("ratingsAll: ", len(ratingsAll))

    # itemsAll:Item[]
    itemsAll = readItems();
    #print("itemsAll: ", len(itemsAll))

    # ratingsNew:Rating[]
    ratingsNew =[]

    # userIds:int[]
    userIds = [u.uid for u in usersAll]

    for userIdI in userIds:
       #print(userIdI)

       # user:User
       user = [u for u in usersAll if u.uid == userIdI][0];
       #user.printUser();

       #userProfileModel = user.exportUserProfileTriangularModel()
       userProfileModel = user.exportUserProfileRefractedModel()

       # ratings:Rating[]
       ratings = [r for r in ratingsAll if r.uid == userIdI]
       #print("ratings: ", len(ratings))

       # items:Item[]
       items = [i for i in itemsAll if i.iid in [r.iid for r in ratings]]
       #print("items: ", len(items))

       # pointsDataCube:Point[]
       #pointsDataCube = [i.exportAsPoint() for i in items]
       
       # preferences:Float[]
       #preferences = userProfileModel.preferenceOfPointsInDataCube(pointsInDataCube, modelConf);

       # itemIndexI:int
       for itemIndexI in range(0, len(items)):
          # itemI:Item
          itemI = items[itemIndexI];
          # ratingI:Rating
          ratingI = ratings[itemIndexI];

          # pointInDataCubeI:Point
          pointInDataCubeI = itemI.exportAsPoint();

          # preferencesI:Float[]
          preference2I = userProfileModel.preferenceOfPointInDataCube(pointInDataCubeI, modelConf);

          # ratingI:Rating[]
          ratingI = Rating(userIdI, ratingI.iid, preference2I, 0, ratingI.typ);

          ratingsNew.append(ratingI)
    
    fileNameRatings2 = ".." + os.sep + "datasets" + os.sep + "ratingsRectangledModel.csv"
    writeRatings(ratingsNew, fileNameRatings2)

    # test reading computed dataset
    # ratingsAll3:Rating[]
    ratingsAll3 = readRatings(fileNameRatings2);


