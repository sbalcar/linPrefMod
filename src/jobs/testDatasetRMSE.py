#!/usr/bin/python3

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from graphicModel.linPrefModel.painting_old import Painting #class

from methods.operators.evaluation.fitness_old import rmse #function

from datasets.datasets import readItems #function
from datasets.datasets import readUsers #function
from datasets.datasets import readRatings #function


def testDatasetRMSE():
  aggrLevel = 0.95

  #linPrefModelConf:LinPrefModelConfiguration
  linPrefModelConf = LinPrefModelConfiguration(1.0, 1.0, 1.0, 1.0)

  # fileNameUsers:String
  fileNameUsers = "../datasets/usersRefractedModel.csv"

  # usersAll:User[]
  usersAll = readUsers(fileNameUsers);
  print("usersAll: ", len(usersAll))

  # fileNameRatings:String
  fileNameRatings = "../datasets/ratingsRefractedModel.csv"

  # ratingsAll:Rating[]
  ratingsAll = readRatings(fileNameRatings);
  #print("ratingsAll: ", len(ratingsAll))

  # fileNameItems:String
  fileNameItems = "../datasets/itemsRefractedModel.csv"

  # itemsAll:Item[]
  itemsAll = readItems(fileNameItems);
  #print("itemsAll: ", len(itemsAll))

  userIds = [u.uid for u in usersAll]
  

  for userIdI in userIds:
      # user:User
      user = [u for u in usersAll if u.uid == userIdI][0];
      user.printUser();
      user = user.exportUser2D();
      user.printUser();

      # ratings:Rating[]
      ratings = [r for r in ratingsAll if r.uid == userIdI]
      #print("ratings: ", len(ratings))

      # ratingsTrain:Rating[]
      ratingsTrain = [r for r in ratings if r.typ == 1]

      # ratingsTest:Rating[]
      ratingsTest = [r for r in ratings if r.typ == 2]


      # itemsTrain:Item[]
      itemsTrain = [i for i in itemsAll if i.iid in [r.iid for r in ratingsTrain]]
      # itemsTest:Item[]
      itemsTest = [i for i in itemsAll if i.iid in [r.iid for r in ratingsTest]]

      # pointsTrain:Point[]
      pointsTrain = [i.exportAsPoint() for i in itemsTrain]
      # pointsTest:Point[]
      pointsTest = [i.exportAsPoint() for i in itemsTest]
  
      # prefsTrain:float[]
      prefsTrain = [r.p2 for r in ratingsTrain]
      # prefsTest:float[]
      prefsTest = [r.p2 for r in ratingsTest]


      #userProfileModel1 = user.exportUserProfileTriangularModel(linPrefModelConf)
      userProfileModel1 = user.exportUserProfileRefractedModel(linPrefModelConf)

      # pointsPrefCubeTrain:Point[]
      pointsPrefCubeTrain = userProfileModel1.pointsDataCubeToPointsPrefCube(pointsTrain);
      pointsPrefCubeTest = userProfileModel1.pointsDataCubeToPointsPrefCube(pointsTest);

      # prefsPointsPrefCubeTrain:Point[]
      prefsPointsPrefCubeTrain = userProfileModel1.preferenceOfPointsInPC(pointsPrefCubeTrain, linPrefModelConf);
      prefsPointsPrefCubeTest = userProfileModel1.preferenceOfPointsInPC(pointsPrefCubeTest, linPrefModelConf);

  
      rmseTrainVal = rmse(prefsPointsPrefCubeTrain, prefsTrain)
      print("rmseTrain: ", rmseTrainVal);

      rmseTestVal = rmse(prefsPointsPrefCubeTest, prefsTest)
      print("rmseTest: ", rmseTestVal);

      # title:String
      title = 'Lin. pref. model'

      # painting:Painting
      painting = Painting(linPrefModelConf, title)
      painting.paintOnlyModel(userProfileModel1, aggrLevel, 'r')

      painting.paintPoints(pointsTrain, pointsPrefCubeTrain, labelsDataCube=[], labelsPrefCube=[], color="b", size=1)
      painting.paintPoints(pointsTest, pointsPrefCubeTest, labelsDataCube=[], labelsPrefCube=[], color="r", size=1)

      #painting.paint(userIdI);
      painting.save(userIdI);
      painting.close();

