#!/usr/bin/python3

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from geometry.point import Point #class

from graphicModel.linPrefModel.painting_old import Painting #class

from datasets.datasets import readUsers #function


def visualisationOfContourLines():
  #modelConf:LinPrefModelConfiguration
  modelConf = LinPrefModelConfiguration(1.0, 1.0, 1.0, 1.0)

  aggrLevel = 0.90

  # fileNameUsers:String
  fileNameUsers = "../datasets/usersRefractedModel.csv"

  # users:User[]
  users = readUsers(fileNameUsers);

  pointsDataCube = [Point(0.73, 0.755), Point(0.125, 0.45), Point(0.624, 0.15)]
  labels = ["A", "B", "C"]

  for indexI in range(len(users)):
    user = users[indexI]
    user.printUser()

    userProfileModel1 = user.exportUserProfileModel();
    #userProfileModel1 = user.exportUserProfileRefractedModel();
    
    # title:String
    title = 'Lin. pref. model'

    # painting:Painting
    painting = Painting(modelConf, title)
    painting.paintOnlyModel(userProfileModel1, aggrLevel, 'g')
    painting.paintPoints(pointsDataCube, [], labelsDataCube=[], labelsPrefCube=[], color="b", size=1)

    painting.paint(indexI);
    #painting.save(indexI);
    break;

