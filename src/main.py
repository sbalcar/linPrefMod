#!/usr/bin/python3


from jobs.paintData import paintData #function
from jobs.paintContourLines import paintContourLinesExample #function
from jobs.visualisationOfDataset import visualisationOfContourLines #function
from jobs.testDatasetRMSE import testDatasetRMSE #function
from jobs.colaborative import colaborative #function
from jobs.search import search #function
from jobs.convertDataset import convertDataset #function
from jobs.paintPreferenceCube import paintPreferenceCube #function

from jobs.gui import gui #function
#from graphicModel.linPrefModel.graphicalModel import main4 # function
from jobs.cv03 import cv03 #function

from datasets.generator.generator import generate #function

if __name__== "__main__":
  #paintData()
  #paintContourLinesExample()
  #visualisationOfContourLines();
  #testDatasetRMSE();
  #colaborative();
  #search();
  #convertDataset();
  #paintPreferenceCube()
  gui();
  #main4();

  #cv03()
  #generate()

