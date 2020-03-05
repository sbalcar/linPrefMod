#!/usr/bin/python3

import numpy as np
from collections import namedtuple #pair

#from inputs import Input #class

from geometry.point import Point # class


Pair = namedtuple("Pair", ["first", "second"])

def generateData(inputIns, n): # Input, int
    generated=[]
    for i in range(1, n):
      x = np.random.rand() + inputIns.idealX
      y = np.random.rand() + inputIns.idealY
      generated.insert(len(generated), (Point(x, y)) )
    return generated;


def generateData2(inputIns, n): # Input, int
    x = np.random.rand(n) + ([inputIns.idealX] * n)
    y = np.random.rand(n) + ([inputIns.idealY] * n)
    return Pair(x, y)

