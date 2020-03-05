#!/usr/bin/python3

from generator import *
from collections import OrderedDict

from geometry.lineSegment import LineSegment #class
from geometry.lineSegments import LineSegments #class


class PrefFncRestriction:
  # prefFncModel:class, fnc:Function, args:Dir
  def __init__(self, prefFncModel, fnc, args):
     self._prefFncModel = prefFncModel;
     self._fnc = fnc;
     self._args = args;

  def generate(self):
    method_to_call = getattr(self._prefFncModel, self._fnc)
    return method_to_call(self._args)


