#!/usr/bin/python3

from statistics import mean #function

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from geometry.pointWithRating import PointWithRating #class

from userProfileModel.user import User2D #class

from graphicModel.linPrefModel.painting_old import Painting #class

from methods.operators.evaluation.fitness_old import rmse #function

from datasets.datasets import readItems #function
from datasets.datasets import readUsers #function
from datasets.datasets import readRatings #function

from methods.operators.operatorGenerateTriangularModel import operatorGenerateTriangularModel #function


def cv03():

  # numberOfUsers:int
  numberOfUsers = 10

  #linPrefModelConf:LinPrefModelConfiguration
  linPrefModelConf = LinPrefModelConfiguration(1.0, 1.0, 1.0, 1.0)

  # fileNameUsers:String
  fileNameUsers = "../datasets/usersRefractedModel.csv"
  # fileNameRatings:String
  fileNameRatings = "../datasets/ratingsRefractedModel.csv"
  # fileNameItems:String
  fileNameItems = "../datasets/itemsRefractedModel.csv"

  # estimateUserFnc:function, testID:str
  estimateUserFnc = estimateUserByTheBestRating;          testID='theBestRating'
  #estimateUserFnc = estimateUserByMiddleOf23;             testID='middleOf23'
  #estimateUserFnc = estimateUserByCenterOfMassOf23;       testID='centerOfMassOf23'
  #estimateUserFnc = estimateUserBy10Random;               testID='10Random'

  print(estimateUserFnc)

  # usersAll:User[]
  usersAll = readUsers(fileNameUsers);
  #print("usersAll: ", len(usersAll))

  # ratingsAll:Rating[]
  ratingsAll = readRatings(fileNameRatings);
  #print("ratingsAll: ", len(ratingsAll))

  # itemsAll:Item[]
  itemsAll = readItems(fileNameItems);
  #print("itemsAll: ", len(itemsAll))

  # errors:float[]
  errors = []

  # user:User
  for user in usersAll:

      # user2DI:User2D
      user2DI = user.exportUser2D()
      user2DI.printUser();

      # ratings:Rating[]
      ratings = [r for r in ratingsAll if r.uid == user2DI.uid]
      #print("ratings: ", len(ratings))

      # ratingsTrain:Rating[]
      ratingsTrain = [r for r in ratings if r.typ == 1]
      # ratingsTest:Rating[]
      ratingsTest = [r for r in ratings if r.typ == 2]

      # itemsTrain:Item[]
      itemsTrain = [i for i in itemsAll if i.iid in [r.iid for r in ratingsTrain]]
      # itemsTest:Item[]
      itemsTest = [i for i in itemsAll if i.iid in [r.iid for r in ratingsTest]]

      # pointsTrain:PointWithRating[]
      pointsWithRatingTrain = [PointWithRating(itemsTrain[i].exportAsPoint(), ratingsTrain[i].p2) for i in range(len(ratingsTrain))]
      # pointsTest:PointWithRating[]
      pointsWithRatingTest = [PointWithRating(itemsTest[i].exportAsPoint(), ratingsTest[i].p2) for i in range(len(ratingsTest))]
    
      # user2D:User2D, error:float
      user2DNewI, errorI = process(user2DI, estimateUserFnc, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf, testID=testID)
      
      errors.append(errorI);

      if len(errors) == numberOfUsers:
        break;

  print("Mean: ", mean(errors))

# user2D:User2D, estimFnc:Fnc, pointsWithRatingTrain:PointWithRating[], pointsWithRatingTest:PointWithRating[], linPrefModelConf:LinPrefModelConfiguration, testID:str
def process(user2D, estimFnc, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf, testID='test'):

  # user2DNew:User2D, error:float
  user2DNew, error = estimFnc(user2D, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf)

  user2DNew.printUser();
  paint(user2D, user2DNew, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf, testID=testID)

  return (user2DNew, error)


# user2D:User2D, pointsWithRatingTrain:PointWithRating[], pointsWithRatingTest:PointWithRating[], linPrefModelConf:LinPrefModelConfiguration
def estimateUserByCenterOfMassOf23(user2D, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf):
  print("TODO");

# user2D:User2D, pointsWithRatingTrain:PointWithRating[], pointsWithRatingTest:PointWithRating[], linPrefModelConf:LinPrefModelConfiguration
def estimateUserByMiddleOf23(user2D, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf):
  # pointsWithRatingTrainSorted:PointWithRating[]
  pointsWithRatingTrainSorted = sorted(pointsWithRatingTrain, key=lambda x: x.rating)

  # pointWithRating2:PointWithRating
  pointWithRating2 = pointsWithRatingTrainSorted[-2]
  # pointWithRating3:PointWithRating
  pointWithRating3 = pointsWithRatingTrainSorted[-3]

  # p1:Point
  p1 = pointWithRating2.point
  # r1:float
  r1 = pointWithRating2.rating

  # p2:Point
  p2 = pointWithRating3.point
  # r2:float
  r2 = pointWithRating3.rating

  # ix:float
  ix = (p1.x + p2.x) /2
  iy = (p1.y + p2.y) /2

  # userd2DNew:User2D
  user2DNew = User2D(user2D.uid, ix, iy, 0.5)

  # error:float
  #error = evalUserIdealDiff(user2D, user2DNew)
  error = evalUserRMSE(user2DNew, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf)

  # tuple<user2D, float>
  return (user2DNew, error)


# user2D:User2D, pointsWithRatingTrain:PointWithRating[], pointsWithRatingTest:PointWithRating[], linPrefModelConf:LinPrefModelConfiguration
def estimateUserByTheBestRating(user2D, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf):
   
  # pointsWithRatingTrainSorted:PointWithRating[]
  pointsWithRatingTrainSorted = sorted(pointsWithRatingTrain, key=lambda x: x.rating)

  # pointWithRating1:PointWithRating
  pointWithRating1 = pointsWithRatingTrainSorted[-1]
  #print(pointWithRating1.rating)

  # ix:float
  ix = pointWithRating1.point.x
  iy = pointWithRating1.point.y

  # userd2DNew:User2D
  user2DNew = User2D(user2D.uid, ix, iy, 0.5)
  # user2DNew = user2D;

  # error:float
  #error = evalUserIdealDiff(user2D, user2DNew)
  error = evalUserRMSE(user2DNew, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf)

  # tuple<user2D, float>
  return (user2DNew, error)


# user2D:User2D, pointsWithRatingTrain:PointWithRating[], pointsWithRatingTest:PointWithRating[], linPrefModelConf:LinPrefModelConfiguration
def estimateUserBy10Random(user2D, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf):

  # numberOfTests:int
  numberOfTests = 10

  # ratings:(User2D, float)[]
  ratings = []

  for i in range(numberOfTests):
    # uIndividualI:IndividualUser
    uIndividualI = operatorGenerate();
    # user2D:User2D
    user2DNewI = uIndividualI.exportUser2D(user2D.uid)

    # errorI:float
    #errorI =  evalUserIdealDiff(user2D, user2DNewI)
    errorI = evalUserRMSE(user2DNewI, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf)
    ratings.append((user2DNewI, errorI))

  # ratingsSorted:float[]
  ratingsSorted = sorted(ratings, key=lambda user2DAndErrorI: user2DAndErrorI[1])

  # tuple<user2D, float>
  return ratingsSorted[0]


# user2D:User2D, pointsWithRatingTrain:PointWithRating[], pointsWithRatingTest:PointWithRating[], linPrefModelConf:LinPrefModelConfiguration
def evalUserRMSE(user2D, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf):

  # pointsTrain:Point[]
  pointsTrain = [p.point for p in pointsWithRatingTrain] 
  # prefsTrain:float[]
  prefsTrain = [p.rating for p in pointsWithRatingTrain]

  # pointsTest:Point[]
  pointsTest = [p.point for p in pointsWithRatingTest] 
  # prefsTest:float[]
  prefsTest = [p.rating for p in pointsWithRatingTest]

  #userProfileModel1 = user2D.exportUserProfileTriangularModel(linPrefModelConf)
  userProfileModel1 = user2D.exportUserProfileRefractedModel(linPrefModelConf)

  # pointsPrefCubeTrain:Point[]
  #pointsPrefCubeTrain = userProfileModel1.pointsDataCubeToPointsPrefCube(pointsTrain);
  pointsPrefCubeTest = userProfileModel1.pointsDataCubeToPointsPrefCube(pointsTest);

  # prefsPointsPrefCubeTrain:Point[]
  #prefsPointsPrefCubeTrain = userProfileModel1.preferenceOfPointsInPrefCube(pointsPrefCubeTrain, linPrefModelConf);
  prefsPointsPrefCubeTest = userProfileModel1.preferenceOfPointsInPC(pointsPrefCubeTest, linPrefModelConf);


  #rmseTrainVal = rmse(prefsPointsPrefCubeTrain, prefsTrain)
  #print("rmseTrain: ", rmseTrainVal);

  rmseTestVal = rmse(prefsPointsPrefCubeTest, prefsTest)
  #print("rmseTest: ", rmseTestVal);

  return rmseTestVal;


# user2D:User2D, userd2DNew:User2D
def evalUserIdealDiff(user2D, user2DNew):

   diffX = abs(user2D.ix - user2DNew.ix)
   diffY = abs(user2D.iy - user2DNew.iy)
   diff = diffX + diffY

   return diff

# user:User2D, user2DEstim:User2D, pointsWithRatingTrain:List<PointWithRating>, pointsWithRatingTest:List<PointWithRating>, linPrefModelConf:LinPrefModelConfiguration, testID:str
def paint(user2D, user2DEstim, pointsWithRatingTrain, pointsWithRatingTest, linPrefModelConf, testID="test"):

  #userProfileModel1 = user2D.exportUserProfileTriangularModel()
  userProfileModel1 = user2D.exportUserProfileRefractedModel(linPrefModelConf)

  #userProfileModel2 = user2DEstim.exportUserProfileTriangularModel()
  userProfileModel2 = user2DEstim.exportUserProfileRefractedModel(linPrefModelConf)

  #aggrLevel:float
  aggrLevel = 0.95

  # title:String
  title = 'Lin. pref. model'

  # painting:Painting
  painting = Painting(linPrefModelConf, title)
  painting.paintOnlyModel(userProfileModel1, aggrLevel, 'g')
  painting.paintOnlyModel(userProfileModel2, aggrLevel, 'r')

  painting.paintPointsInPrefFncCubes(pointsWithRatingTest, color="g", size=1)
  painting.paintPointsInPrefFncCubes(pointsWithRatingTrain, color="r", size=1)

  #painting.paint(user2D.uid);
  painting.save(user2D.uid, testID=testID);
  painting.close();














