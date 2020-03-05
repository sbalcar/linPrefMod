#!/usr/bin/python3

from sklearn.metrics import mean_squared_error
from math import sqrt


# ratingsComputed:list<float>, ratingsOriginal:list<float>
def fitnessRMSE(ratingsPredicted, ratingsOriginal):
  rmse = sqrt(mean_squared_error(ratingsPredicted, ratingsOriginal))
  # rmse:float
  return float(rmse);
