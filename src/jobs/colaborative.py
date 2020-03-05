#!/usr/bin/python3

import math

import pandas as pd
import matplotlib.pyplot as plt

from datasets.datasets import readUsers #function
from datasets.datasets import readRatings #function


def colaborative():

  # fileNameUsers:String
  fileNameUsers = "../datasets/usersRefractedModel.csv"

  # users:User[]
  users = readUsers(fileNameUsers);

  # fileNameRatings:String
  fileNameRatings = "../datasets/ratingsRefractedModel.csv"

  # ratingsAll:Rating[]
  ratingsAll = readRatings(fileNameRatings);

  userIds = [userI.uid for userI in users] 
  #print("UserIds: ", userIds)

  # numberOfCommonItems:int[]
  numberOfCommonItems = []

  for userIdI in userIds:
     for userIdJ in userIds:
        if userIdI == userIdJ:
          break;
        #print("UserIdI: " + str(userIdI) + " userIdJ " + str(userIdJ))
        intersectionI = intersectionOfUsers(userIdI, userIdJ, users, ratingsAll)
        intersectionIa = euclideanDistanceOfUsers(userIdI, userIdJ, users)

        numberOfCommonItems.append(intersectionI)
     if len(numberOfCommonItems) > 100:
         break;

  commutes = pd.Series(numberOfCommonItems)
  commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
  plt.title('Common ratings of two users')
  plt.xlabel('Number of common items')
  plt.ylabel('Counts')
  plt.grid(axis='y', alpha=0.75)

  plt.savefig('../images/commonItems.png')
  plt.show()


# userId1:int, userId2:int, users:User[], ratingsAll:Rating[]
def intersectionOfUsers(userId1, userId2, users, ratingsAll):
  # user1:User
  user1 = [userI for userI in users if userI.uid == userId1][0]
  # user2:User
  user2 = [userI for userI in users if userI.uid == userId2][0]

  #userProfileModel1 = user1.exportUserProfileTriangularModel();
  #userProfileModel2 = user2.exportUserProfileTriangularModel();

  # ratingsOfUser1:Rating[]
  ratingsOfUser1 = [ratingI for ratingI in ratingsAll if ratingI.uid == userId1]
  # ratingsOfUser2:raitng[]
  ratingsOfUser2 = [ratingI for ratingI in ratingsAll if ratingI.uid == userId2]
  
  # ratedItemIdsOfUser1:int[]
  ratedItemIdsOfUser1 = [ratingI.iid for ratingI in ratingsOfUser1]
  # ratedItemIdsOfUser2:int[]
  ratedItemIdsOfUser2 = [ratingI.iid for ratingI in ratingsOfUser2]
  #print("RatingsOfUser1: ", len(ratingsOfUser1))
  #print("RatingsOfUser2: ", len(ratingsOfUser2))
  
  intersectionOfItemIds = list(set(ratedItemIdsOfUser1) & set(ratedItemIdsOfUser2))
  #print("IntersectionOfItemIds: ", len(intersectionOfItemIds))
 
  return len(intersectionOfItemIds);


# userId1:int, userId2:int, users:User[]
def euclideanDistanceOfUsers(userId1, userId2, users):
  # user1:User
  user1 = [userI for userI in users if userI.uid == userId1][0]
  # user2:User
  user2 = [userI for userI in users if userI.uid == userId2][0]

  return math.sqrt((user1.ix - user2.ix)**2 + (user1.iy - user2.iy)**2)

