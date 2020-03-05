#!/usr/bin/python3

from methods.dataSplit.splitting.aDataSplit import ADataSplit

class CrossValidationDataSplitModel(ADataSplit):
    name = "cross-valid."

    def numberOfSplitting(self):
        return 5

    # pointsWithRating:list<PointWithRating>, numberOfSplit:int
    def split(self, pointsWithRating, numberOfSplit=0):

        pointsWithRatingCopy = pointsWithRating.copy()
        for i in range(numberOfSplit +1):
           pointsWithRatingCopy.pop(0)

        test = pointsWithRatingCopy[0::5]
        train = [p for p in pointsWithRating if p not in test]

        return (train, test)