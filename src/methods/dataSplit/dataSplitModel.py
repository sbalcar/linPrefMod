#!/usr/bin/python3

import enum

from methods.dataSplit.splitting.trainIsTestDataSplitModel import TrainIsTestDataSplitModel
from methods.dataSplit.splitting.train5Test1DataSplitModel import Train5Test1DataSplitModel
from methods.dataSplit.splitting.crossValidationDataSplit import CrossValidationDataSplitModel


class DataSplitModel(enum.Enum):
    trainIsTest = TrainIsTestDataSplitModel
    train5Test1 = Train5Test1DataSplitModel
    crossValidation = CrossValidationDataSplitModel

    def getDataSplitModel(index):
        if index == 0:
            return TrainIsTestDataSplitModel
        if index == 1:
            return Train5Test1DataSplitModel
        if index == 2:
            return CrossValidationDataSplitModel

    #dataSplitClass:class
    def getIndex(dataSplitClass):

        if dataSplitClass is TrainIsTestDataSplitModel:
            return 0
        if dataSplitClass is Train5Test1DataSplitModel:
            return 1
        if dataSplitClass is CrossValidationDataSplitModel:
            return 2