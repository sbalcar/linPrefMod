#!/usr/bin/python3


class Rating:
  # userID:int, itemID:int, rating:float
  def __init__(self, userID, itemID, rating):
     if type(userID) is not int:
        raise ValueError("Argument userID isn't type int.")
     if type(itemID) is not int:
        raise ValueError("Argument itemID isn't type int.")
     if type(rating) is not float:
        raise ValueError("Argument rating isn't type float.")
     self.userID = userID
     self.itemID = itemID
     self.rating = rating


  def exportAsList(self):
     return [self.userID, self.itemID, self.rating]
