#!/usr/bin/python3

from geometry.point import Point #class

from generator import *

class Line:
  # a:double, b:double, c:double
  def constructor1(self, a, b, c):
    # ax + by + c = 0
    self.a = a
    self.b = b
    self.c = c

  # a:double, b:double, point:Point
  def constructor2(self, a, b, point):
    # ax + by + c = 0
    self.a = a
    self.b = b
    self.c = -1 * (a * point.x + b * point.y)


  def getPoint1(self):
    # x = -c / a
    return Point(-self.c/self.a, 0.0)

  def getPoint2(self):
    # y = -c / b
    return Point(0.0, -self.c/self.b)

  def getFunctionValue(self, x):
    # y = -ax/b -c/b
    return -self.a * x / self.b  -self.c / self.b

  def getDomainValue(self, y):
    # x = -by/a -c/a
    return -self.b * y / self.a  -self.c /self.a
