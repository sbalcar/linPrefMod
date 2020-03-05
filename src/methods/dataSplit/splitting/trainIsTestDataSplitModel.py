#!/usr/bin/python3

from methods.dataSplit.splitting.aDataSplit import ADataSplit

class TrainIsTestDataSplitModel(ADataSplit):
    name = "train=test"

    def numberOfSplitting(self):
        return 1

    # pointsWithRating:list<PointWithRating>
    def split(self, pointsWithRating, numberOfSplit=0):
        return (pointsWithRating, pointsWithRating)