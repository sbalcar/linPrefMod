#!/usr/bin/python3

from generator import *
import math

from geometry.point import Point #class

class LineSegment:
  # point1:Point, point2:Point
  def __init__(self, point1, point2):
     if type(point1) is not Point:
        raise ValueError("Argument point1 isn't type Point.")
     if type(point2) is not Point:
        raise ValueError("Argument point2 isn't type Point.")
     self.point1 = point1
     self.point2 = point2

  def clone(self):
    return LineSegment(self.point1.clone(), self.point2.clone());

  # line:Pair(Point, Point)
  def size(self):
      size = math.sqrt(pow(self.point1.x - self.point2.x, 2) + pow(self.point1.y - self.point2.y, 2))
      # float
      return size;

  def __eq__(self, other):
    if other is None:
        return False;
    return self.point1 == other.point1 and self.point2 == other.point2

  def __hash__(self):
    return hash(('p1', self.point1.__hash__(),
                 'p2', self.point2.__hash__()))

  def printLineSegment(self):
      print("LineSegment x1:", self.point1.x, " y1:", self.point1.y, " x2:", self.point2.x, " y2:", self.point2.y)

  def toString(self):
      return "[" + str(self.point1.x) + ", " + str(self.point1.y) + "], [" + str(self.point2.x) + ", " + str(self.point2.y) + "]";


  def midpoint(self):
      x = self.getMaxX() - self.getMinX()
      y = self.getMaxY() - self.getMinY()
      return Point(self.getMinX() + x/2, self.getMinY() + y/2)



  def getMinXPoint(self):
      if self.point1.x < self.point2.x:
          return self.point1;
      return self.point2;
  def getMaxXPoint(self):
      if self.point1.x > self.point2.x:
          return self.point1;
      return self.point2;

  def getMinYPoint(self):
      if self.point1.y < self.point2.y:
          return self.point1;
      return self.point2;
  def getMaxYPoint(self):
      if self.point1.y > self.point2.y:
          return self.point1;
      return self.point2;


  def getMinX(self):
    return min(self.point1.x, self.point2.x);
  def getMaxX(self):
    return max(self.point1.x, self.point2.x);

  def getMinY(self):
    return min(self.point1.y, self.point2.y);
  def getMaxY(self):
    return max(self.point1.y, self.point2.y);


  # x:float
  def deleteFromMinusInfinityToX(self, x):
    if x < self.getMinX():
        return self.clone();
    elif self.getMinX() <= x and x <= self.getMaxX():
        point = Point(x, self.intersectionWithTheAxisParallelToY(x));
        return LineSegment(point, self.getMaxXPoint().clone())
    else:
        return None;

  # x:float
  def deleteFromXToPlusInfinity(self, x):
    if x < self.getMinX():
        return None;
    elif self.getMinX() <= x and x <= self.getMaxX():
        point = Point(x, self.intersectionWithTheAxisParallelToY(x));
        return LineSegment(self.getMinXPoint().clone(), point)
    else:
        return self.clone();


  # y:float
  def deleteFromMinusInfinityToY(self, y):
    if y < self.getMinY():
        return self.clone();
    elif self.getMinY() <= y and y <= self.getMaxY():
        point = Point(self.intersectionWithTheAxisParallelToX(y), y);
        return LineSegment(point, self.getMaxYPoint().clone())
    else:
        return None;

  # y:float
  def deleteFromYToPlusInfinity(self, y):
    if y < self.getMinY():
        return None;
    elif self.getMinY() <= y and y <= self.getMaxY():
        point = Point(self.intersectionWithTheAxisParallelToX(y), y);
        return LineSegment(self.getMinYPoint().clone(), point)
    else:
        return self.clone();


  # point:Point
  def isOnLine(self, point):
    # x = ax + t * vx
    # y = ay + t * vy
    vx = self.point2.x - self.point1.x;
    vy = self.point2.y - self.point1.y;
    # t = (x - ax) / vx
    # t = (y - ay) / vy
    tx = (point.x - self.point1.x) / vx;
    ty = (point.y - self.point1.y) / vy;
   
    return tx - ty < 0.0001

  # point:Point
  def isOnLineSegment(self, point):
    if not self.isOnLine(point):
      return False;

    return (self.getMinX() <= point.x and point.x <= self.getMaxX()) and (
       (self.getMinY() <= point.y and point.y <= self.getMaxY));


  def isGrowingOnY(self):
    return self.point1.y > self.point2.y;
  def isGrowingOnX(self):
    return self.point1.x > self.point2.x;

  def isDecreasingOnY(self):
    return self.point1.y < self.point2.y;
  def isDecreasingOnX(self):
    return self.point1.x < self.point2.x;


  # valueX:float
  def intersectionWithTheAxisParallelToY(self, valueX):
    if self.point1.x == valueX:
            return self.point1.y
    if self.point2.x == valueX:
            return self.point2.y

    if self.getMinX() <= valueX and valueX <= self.getMaxX():
            width = self.point2.x - self.point1.x
            hight = self.point2.y - self.point1.y
            delta = hight / width * (valueX - self.point1.x);
            return self.point1.y + delta
    return None;

  # valueY:float
  def intersectionWithTheAxisParallelToX(self, valueY):
    if self.point1.y == valueY:
            return self.point1.x
    if self.point2.y == valueY:
            return self.point2.x

    if self.getMinY() <= valueY and valueY <= self.getMaxY():
            width = self.point2.x - self.point1.x
            hight = self.point2.y - self.point1.y
            delta = width / hight * (valueY - self.point1.y)
            return self.point1.x + delta
    return None

  # valueX:Float
  def isParalelToX(self):
    if self.point1.y == self.point2.y:
       return True;
    return False;
  
  # valueY:Float
  def isParalelToY(self):
    if self.point1.x == self.point2.x:
      return True;
    return False;

  # valueY:Float
  def exportLineParalelToX(self, valueY):
    lineClone = self.clone();
    lineClone.point1.y = valueY
    lineClone.point2.y = valueY
    return lineClone;

  # valueX:Float
  def exportLineParalelToY(self, valueX):
    lineClone = self.clone();
    lineClone.point1.x = valueX
    lineClone.point2.x = valueX
    return lineClone;


  # segmentation:Pair(int,int)[]
  def exportSegmentation(self, segmentation):
    # lineSegments:LineSegment[]
    lineSegments = []
    # pointStartI:Point
    pointStartI = self.point1
    spaceX = (self.point2.x - self.point1.x)
    spaceY = (self.point2.y - self.point1.y)
    for segmentI in segmentation:
       percentagesXI = segmentI.first
       percentagesYI = segmentI.second
       diffXI = spaceX / 100.0 * percentagesXI
       diffYI = spaceY / 100.0 * percentagesYI
       # pointEndI:Point
       pointEndI = Point(pointStartI.x + diffXI, pointStartI.y + diffYI)
       lineSegmentI = LineSegment(pointStartI, pointEndI);
       lineSegments.append(lineSegmentI)
       pointStartI = pointEndI;
    # lineSegments:LineSegment[]
    return lineSegments
