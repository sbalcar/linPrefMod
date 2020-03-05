#!/usr/bin/python3

from geometry.point import Point #class

from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class


class Threshold:

  # aggregation:AggrFnc, point:Point
  def __init__(self, aggrFnc, point):

     if type(aggrFnc) is not AggrFnc:
        raise ValueError("Argument aggregation isn't type AggrFnc.")
     if type(point) is not Point:
        raise ValueError("Argument point isn't type Point.")

     self.aggrFnc = aggrFnc;
     self.point = point;


