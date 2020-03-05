#!/usr/bin/python3

import numpy as np

#from methods.individual import IndividualUser #class
from methods.individual.individualUserTrinity import IndividualUserTrinity #class


# individual:IndividualUser,
def operatorRandomMoveTriangularModel(uIndividual, multiplier=0.1):
    diff = np.random.uniform(0, 1*multiplier, 1)[0]
    if np.random.rand() < .5:
        diff *= -1;

    ix = uIndividual.ix + diff;
    iy = uIndividual.iy + diff;
    wx = uIndividual.wx + diff;

    value = np.random.randint(3, size=1)[0]
    if value == 0:
      ix += diff;
    if value == 1:
      iy += diff;
    if value == 2:
      wx += diff;
    
    return IndividualUserTrinity(ix, iy, wx);
    

