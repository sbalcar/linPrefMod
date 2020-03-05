#!/usr/bin/python3

from methods.dataSplit.splitting.aDataSplit import ADataSplit

class Train5Test1DataSplitModel(ADataSplit):
    name = "train/test=5/1"

    def numberOfSplitting(self):
        return 1

    # pointsWithRating:list<PointWithRating>
    def split(self, pointsWithRating, numberOfSplit=0):

        test = pointsWithRating[0::5]
        train = [p for p in pointsWithRating if p not in test]

        return (train, test)