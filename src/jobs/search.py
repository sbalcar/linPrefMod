#!/usr/bin/python3

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from methods.hillClimbing import HillClimbing #class
from methods.operators.operatorRandomMoveTriangularModel import operatorRandomMoveTriangularModel #function
from methods.operators.evaluation.fitness_old import fitnessRMSE_ #function
from methods.operators.evaluation.fitness_old import rmse #function

from datasets.datasets import readItems #function
from datasets.datasets import readUsers #function
from datasets.datasets import readRatings #function


def search():
    aggrLevel = 0.95

    #modelConf:LinPrefModelConfiguration
    modelConf = LinPrefModelConfiguration(1.0, 1.0, 1.0, 1.0)

    # fileNameUsers:String
    fileNameUsers = "../datasets/usersRefractedModel.csv"

    # usersAll:User[]
    usersAll = readUsers(fileNameUsers);
    #print("usersAll: ", len(usersAll))

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

    userId = userIds[0]

    print("Input:")
    # user:User
    user = [u for u in usersAll if u.uid == userId][0];
    user.printUser();


    # ratings:Rating[]
    ratings = [r for r in ratingsAll if r.uid == userId]
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


    ix = user.ix;
    iy = user.iy;
    wx = user.exportNormalizedWX();
    wy = user.exportNormalizedWY();
    print("User ix: " + str(ix) + ", iy: " + str(iy) + ", wx: " + str(wx))

    ## searchAlg:RandomSearch
    #searchAlg = RandomSearch()
    ## theBestIndivEval:IndividualEvaluated = modelConf:LinPrefModelConfiguration, pointsTrain:Point[], prefsTrain:Point[], fitnessFnc:Function, generateFnc:Function
    #theBestIndivEval = searchAlg.search(modelConf, pointsTrain, prefsTrain, numberOfGenerations=10, fitnessFnc=fitnessRMSE, generateFnc=operatorGenerate)
    
    # searchAlg:HillClimbing
    searchAlg = HillClimbing()
    # theBestIndivEval:IndividualEvaluated = modelConf:LinPrefModelConfiguration, pointsTrain:Point[], prefsTrain:Point[], fitnessFnc:Function, generateFnc:Function, neighborFnc:Function
    theBestIndivEval = searchAlg.search(modelConf, pointsTrain, prefsTrain, numberOfGenerations=10000, fitnessFnc=fitnessRMSE_, generateFnc=operatorGenerate, neighborFnc=operatorRandomMoveTriangularModel)


    theBestIndiv = theBestIndivEval.individual

    # userProfileModel:UserProfileModel
    userProfileModel = theBestIndiv.exportUserProfileRefractedModel()
    print("");

    print("Result:");
    #userProfileModel.print()
    theBestIndiv.printIndividualUser()


    # pointsPrefCubeTrain:Point[]
    pointsPrefCubeTrain = userProfileModel.pointsDataCubeToPointsPrefCube(pointsTrain);
    pointsPrefCubeTest = userProfileModel.pointsDataCubeToPointsPrefCube(pointsTest);

    # prefsPointsPrefCubeTrain:Point[]
    prefsPointsPrefCubeTrain = userProfileModel.preferenceOfPointsInPC(pointsPrefCubeTrain, modelConf);
    prefsPointsPrefCubeTest = userProfileModel.preferenceOfPointsInPC(pointsPrefCubeTest, modelConf);


    fitnessRMSETrain = rmse(prefsPointsPrefCubeTrain, prefsTrain)
    print("fitnessRMSETrain: ", fitnessRMSETrain);

    fitnessRMSETest = rmse(prefsPointsPrefCubeTest, prefsTest)
    print("fitnessRMSETest: ", fitnessRMSETest);

    #a=operatorRandomMove;
    ##b=(5,5)
    #b=range(1, 3)
    #print(*range(1, 3))

    #params = {'first': 1, 'second': 2}
    #params = {1, 2}
    #print(*params)

    ##a(*b,1)

    #operatorRandomMove(theBestIndiv, multiplier=0.1)

