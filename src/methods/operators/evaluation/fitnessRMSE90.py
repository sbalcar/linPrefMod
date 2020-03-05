#!/usr/bin/python3

from sklearn.metrics import mean_squared_error
from math import sqrt


# ratingsComputed:list<float>, ratingsOriginal:list<float>
def fitnessRMSE90(ratingsPredicted, ratingsOriginal):
    # itemIDs90:list<int>
    itemIDs90 = [itemID for itemID in range(len(ratingsOriginal)) if ratingsOriginal[itemID] >= 0.9]

    # ratingsPredicted90:list<float>
    ratingsPredicted90 = [ratingsPredicted[itemID] for itemID in range(len(ratingsPredicted)) if itemID in itemIDs90]
    ratingsOriginal90 = [ratingsOriginal[itemID] for itemID in range(len(ratingsOriginal)) if itemID in itemIDs90]

    if len(ratingsPredicted90) == 0:
        return None

    rmse = sqrt(mean_squared_error(ratingsPredicted90, ratingsOriginal90))
    # rmse:float
    return float(rmse);