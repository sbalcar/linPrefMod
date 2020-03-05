#!/usr/bin/python3

from generator import *

from graphicModel.preferenceCubeModel.paintingPreferenceCubeModel import PaintingPreferenceCubeModel #class

from userProfileModel.model.threshold.threshold import Threshold #class

from geometry.pointWithID import PointWithID #class

class ItemWithRating:
  # itemID:String, rating:Float
  def __init__(self, itemID, rating):
     self.itemID = itemID
     self.rating = rating

  def __eq__(self, other):
    if other == None:
        return False;
    return self.itemID == other.itemID and self.rating == other.rating

  def __hash__(self):
    return hash(('itemID', self.itemID, 'rating', self.rating))

  def printItemWithRating(self):
     print(self.itemID + ", " + str(self.rating))

class QueueOfItems:
    # itemsWithRatings:ItemWithRating[]
    def __init__(self, itemsWithRatings):
       #itemsWithRatings:ItemWithRating[]
       self.itemsWithRatings = sorted(itemsWithRatings, key=lambda itemWithRating: itemWithRating.rating)
       self.itemsWithRatings.reverse()

    # index:Integer
    def get(self, index):
      # ItemWithRating
      return self.itemsWithRatings[index];

    # itemID:Integer
    def getRatingOfItemID(self, itemID):
        selectedItemsWithRatings = [itemWithRatingI for itemWithRatingI in itemsWithRatings if itemWithRatingI.itemID == itemID]
        if len(selectedItemsWithRatings) == 0:
           return None;
        return selectedItemsWithRatings[0].rating;

    def printQueueOfItems(self):
        for itemI in self.itemsWithRatings:
          itemI.printItemWithRating()

class ModelOfFoundItems:
    def __init__(self):
       # itemsWithRatings:ItemWithRating[]
       self.itemsWithRatings = []

    # itemID:String, rating:float
    def add(self, itemID, rating):
       if type(itemID) is not str:
          raise ValueError("Argument itemID isn't type String.")
       if type(rating) is not float:
          raise ValueError("Argument rating isn't type float.")

       newItem = ItemWithRating(itemID, rating)
       self.itemsWithRatings.append(newItem);

    # itemID:String
    def contains(self, itemID):
       # selectedItems:ItemWithRating[]
       selectedItems = [itemWithRatingI for itemWithRatingI in self.itemsWithRatings if itemWithRatingI.itemID is itemID]
       if len(selectedItems) > 0:
          return True;
       return False;

    # rating:float
    def getItemIDsBetterThan(self, rating):
       
       #selectedItemsIDs:String[]
       selectedItemsIDs = [str(itemWithRatingI.itemID) for itemWithRatingI in self.itemsWithRatings if itemWithRatingI.rating > rating]
       
       #String[]
       return selectedItemsIDs;

    def printModel(self):
      print("ModelOfFoundItems: " + str(len(self.itemsWithRatings)));

    def getItems(self):
        return [itemWithRaitingI.itemID for itemWithRaitingI in self.itemsWithRatings]

# linPrefModelConf:LinPrefModelConfiguration, pointsWithIDs:PointWithID[], aggregation:AggrFnc, numberOfThresholds:Integer
def countThreshold(linPrefModelConf, pointsWithIDs, aggrFnc, numberOfThresholds):
   
   if numberOfThresholds == 0:
     return ([],[],[])

   # lx:ItemWithRating[]
   lx = [ItemWithRating(pointWithID.pointID, pointWithID.point.x) for pointWithID in pointsWithIDs]
   # ly:ItemWithRating[]
   ly = [ItemWithRating(pointWithID.pointID, pointWithID.point.y) for pointWithID in pointsWithIDs]

   # lModelX:QueueOfItems
   lModelX = QueueOfItems(lx)
   #lModelX.printQueueOfItems()
   #print("------------------")

   # lModelY:QueueOfItems
   lModelY = QueueOfItems(ly)
   #lModelY.printQueueOfItems()

   # modelOfFoundItems:ModelOfFoundItems
   modelOfFoundItems = ModelOfFoundItems()

   # thresholds:Threshold[]
   thresholds = []

   # thresholdPoints:Threshold[]
   candidatesForThreshold = []

   # numberOfThresholdI:Integer
   for numberOfThresholdI in range(numberOfThresholds):
     
     # xItemWithRatingI:ItemWithRating
     xItemWithRatingI = lModelX.get(numberOfThresholdI);
     # yItemWithRatingI:ItemWithRating
     yItemWithRatingI = lModelY.get(numberOfThresholdI);

     # candidateForThresholdPoint:Point
     candidateForThresholdPoint = Point(xItemWithRatingI.rating, yItemWithRatingI.rating)
     candidatesForThreshold.append(Threshold(aggrFnc, candidateForThresholdPoint))

     #candidateForThresholdRating:float
     candidateForThresholdRating = aggrFnc.preferenceOfPointInPC(candidateForThresholdPoint, linPrefModelConf)
     #print("candidateForThresholdRating: " + str(candidateForThresholdRating));

     # itemIDsBetterThanCandidateI:String[]
     itemIDsBetterThanCandidateI = modelOfFoundItems.getItemIDsBetterThan(candidateForThresholdRating);
     #print("itemIDsBetterThanCandidateI: " + str(len(itemIDsBetterThanCandidateI)))

     # thresholdsPointsI:Point[]
     thresholdsPointsI = [pointsWithIDI.point for pointsWithIDI in pointsWithIDs if pointsWithIDI.pointID in itemIDsBetterThanCandidateI];
     #print("thresholdsPointsI: " + str(len(thresholdsPointsI)))

     # thresholdsI:Threshold[]
     thresholdsI = [Threshold(aggrFnc, pointI) for pointI in thresholdsPointsI]
     thresholds.extend(thresholdsI);

     #print("xItemWithRatingI.itemID" + str(xItemWithRatingI.itemID))
     if not modelOfFoundItems.contains(xItemWithRatingI.itemID):
        # point1:Point
        point1 = [pointsWithIDI.point for pointsWithIDI in pointsWithIDs if pointsWithIDI.pointID in xItemWithRatingI.itemID][0];
        # rating1:Float
        rating1 = aggrFnc.preferenceOfPointInPC(point1, linPrefModelConf);
        modelOfFoundItems.add(xItemWithRatingI.itemID, rating1);

     if not modelOfFoundItems.contains(yItemWithRatingI.itemID):
        # point1:Point
        point1 = [pointsWithIDI.point for pointsWithIDI in pointsWithIDs if pointsWithIDI.pointID in yItemWithRatingI.itemID][0];
        # rating1:Float
        rating1 = aggrFnc.preferenceOfPointInPC(point1, linPrefModelConf);
        modelOfFoundItems.add(yItemWithRatingI.itemID, rating1);

   #modelOfFoundItems.printModel()

   # (Threshold[], Threshold[])
   return (candidatesForThreshold, thresholds, modelOfFoundItems.getItems());


# linPrefModelConf:LinPrefModelConfiguration, title:String, pointsWithIDs:PointWithID[], aggregation:AggrFnc, numberOfThresholds:Integer
def paintPreferenceCube(linPrefModelConf, title, pointsWithIDs, aggrFnc, numberOfThresholds):

   # thresholds:(Threshold[], Threshold[])
   candidatesForThresholds, thresholds, itemsFound = countThreshold(linPrefModelConf, pointsWithIDs, aggrFnc, numberOfThresholds);

   # pointnsOnX:PointWithID[]
   pointnsOnX = [PointWithID(Point(pointWithID.point.x, 0), pointWithID.pointID) for pointWithID in pointsWithIDs]

   # pointnsOnY:PointWithID[]
   pointnsOnY = [PointWithID(Point(0, pointWithID.point.y), pointWithID.pointID) for pointWithID in pointsWithIDs]

   pointFound = [pointsWithIDI for pointsWithIDI in pointsWithIDs if pointsWithIDI.pointID in itemsFound]

   # painting:PaintingPreferenceCubeModel
   painting = PaintingPreferenceCubeModel(linPrefModelConf, title)
   #painting.paintPreferenceCube(pointsWithIDs)
   painting.paintPreferenceCube(pointFound)
   painting.paintPreferenceCube(pointnsOnX)
   painting.paintPreferenceCube(pointnsOnY)
   painting.paintThreshold(linPrefModelConf, candidatesForThresholds, color="y", linewidth=0.5)
   painting.paintThreshold(linPrefModelConf, thresholds, color="r", linewidth=1.0)

   return painting.graphicalModel.figure

