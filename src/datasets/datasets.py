#!/usr/bin/python3

from userProfileModel.userProfileModel import UserProfileModel #class

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class
from userProfileModel.user import User2D #class


from geometry.point import Point #class

import csv

class Item:
  # x:float, y:float, z:float
  def __init__(self, iid, x, y, z):
    self.iid = int(iid)
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  def printItem(self):
    print("Item iid:", self.iid, " x:", self.x,  " y:", self.y, " z:", self.z)

  def exportAsPoint(self):
    return Point(self.x, self.y)

class User:
  # uid:int, ix:float, iy:float, iz:float, wx:float, wy:float
  def __init__(self, uid, ix, iy, iz, wx, wy):
    self.uid = int(uid)
    self.ix = float(ix)
    self.iy = float(iy)
    self.iz = float(iz)
    self.wx = float(wx)
    self.wy = float(wy)

  def printUser(self):
    print("User uid:", self.uid, " ix:", self.ix,  " iy:", self.iy, " iz:", self.iz, " wx:", self.wx, " wy:", self.wy)

  def exportUser2D(self):
    return User2D(self.uid, self.ix, self.iy, 1 - self.exportNormalizedWX())

  def exportNormalizedWX(self):
    return self.wy / (self.wx + self.wy);

  def exportNormalizedWY(self):
     return self.wx / (self.wx + self.wy);

  def exportUserProfileTriangularModel(self):
    # prefFncX:PrefFncX
    prefFncX = self.exportPrefFncX();
    # prefFncY:PrefFncY
    prefFncY = self.exportPrefFncY();

    #aggregation = AggrFnc(Line(-a.a/a.b, -1.0, 1.0), [self.wy / (self.wx + self.wy), self.wx / (self.wx + self.wy)])
    #aggregation = AggrFnc([self.wy / (self.wx + self.wy), self.wx / (self.wx + self.wy)])
    aggrFnc = AggrFnc([self.exportNormalizedWX(), self.exportNormalizedWY()])

    # UserProfileModel
    return UserProfileModel(prefFncX, prefFncY, aggrFnc);


  def exportUserProfileRefractedModel(self):
    up3Model = self.exportUserProfileTriangularModel();
    up3Model.prefFncX = up3Model.prefFncX.exportRefractedPrefFncX()
    up3Model.prefFncY = up3Model.prefFncY.exportRefractedPrefFncY()

    # up3Model:UserProfileRefractedModel
    return up3Model;

  def exportPrefFncX(self):
    return PrefFncX([Point(0, 0), Point(self.ix, 1), Point(1, 0)])

  def exportPrefFncY(self):
    return PrefFncY([Point(0, 0), Point(1, self.iy), Point(0, 1)])


class Rating:
  # uid:int, iid:int, p2:float, p3:float, typ:int
  def __init__(self, uid, iid, p2, p3, typ):
    self.uid = int(uid)
    self.iid = int(iid)
    self.p2 = float(p2)
    self.p3 = float(p3)
    self.typ = int(typ)

  def printRating(self):
    print("Rating uid:", self.uid, " iid:", self.iid, " p2:", self.p2, " p3:", self.p3, "typ:", self.typ);

  def clone(self):
      return Rating(self.uid, self.iid, self.p2, self.p3, self.typ)


def readItems(fileName):
    #filename = "../datasets/itemsRefractedModel.csv"
    #filename = "adbis_items.csv"
    #items:Item[]
    items = []
    with open(fileName, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        next(csvreader)

        for lineI in csvreader:
          iid, x, y, z = lineI
          items.append(Item(iid, x, y, z))
    #items:Item[]
    return items

# fileName:String
def readUsers(fileName):
    #fileName = "../datasets/usersRefractedModel.csv"
    users = []
    with open(fileName, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        next(csvreader)

        for lineI in csvreader:
          uid, ix, iy, iz, wx, wy = lineI
          users.append(User(uid, ix, iy, iz, wx, wy))
    #users:User[]
    return users

# fileName:String
def readRatings(fileName):
    ratings = []
    with open(fileName, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        next(csvreader)

        for lineI in csvreader:
          uid, iid, p2, p3, typ = lineI
          ratings.append(Rating(uid, iid, p2, p3, typ))
    #ratings:Rating[]
    return ratings

# ratings:Rating[], fileName:String
def writeRatings(ratings, fileName):
  
    # writing to csv file 
    with open(fileName, 'w') as csvfile: 
       # creating a csv writer object 
       csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
       csvwriter.writerow(['"UID"','"IID"','"P2"','"P3"','"TYP"'])

       for ratingI in ratings:
         csvwriter.writerow([ratingI.uid, ratingI.iid, '"'+str(ratingI.p2)+'"', '"'+str(ratingI.p3)+'"', ratingI.typ])



