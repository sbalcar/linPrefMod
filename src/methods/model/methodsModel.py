#!/usr/bin/python3

from PyQt5.QtCore import Qt, QPoint

from configuration.arguments import Arguments
from configuration.argument import Argument


from geometry.lineSegment import LineSegment #class
from geometry.lineSegments import LineSegments #class
from geometry.point import Point #class
from geometry.pointWithID import PointWithID #class

from methods.randomSearch import RandomSearch #class
from methods.hillClimbing import HillClimbing #class
from methods.theHighestRating import TheHighestRating #class
from methods.linearRegression import LinearRegression #class

from methods.operators.evaluation.fitnessRMSE import fitnessRMSE #function
from methods.operators.operatorGenerateTriangularModel import operatorGenerateTriangularModel #function
from methods.operators.operatorGenerateRefractedModel import operatorGenerateRefractedModel #function
from methods.operators.operatorA import operatorA #function

from methods.operators.aggregation.aggrOperatorTwoFurthest05Points import AggrOperatorTwoFurthest05Points

from methods.dataSplit.splitting.trainIsTestDataSplitModel import TrainIsTestDataSplitModel
from methods.dataSplit.splitting.train5Test1DataSplitModel import Train5Test1DataSplitModel
from methods.dataSplit.splitting.crossValidationDataSplit import CrossValidationDataSplitModel


class MethodsModel:
    def __init__(self):
        # methods:list<MethodModel>
        self.methods = []
        # currentUserProfileModel:UserProfileModel
        self.currentUserProfileModel = None

    # methodModel:MethodModel
    def addModel(self, methodModel):
        if type(methodModel) is not MethodModel:
            raise ValueError("Argument methodModel isn't type MethodModel.")
        self.methods.append(methodModel)


    @staticmethod
    def getModel():

        # argumentsRandomTriagular:Arguments
        argumentsRandomTriagular:Arguments = Arguments([Argument(RandomSearch.NUMBER_OF_RUN, 30),
                                              Argument(RandomSearch.GENERATE_OPR, operatorGenerateTriangularModel.__name__),
                                              Argument(RandomSearch.FITNESS_FNC, fitnessRMSE.__name__)])
        # methodRandomTriagular:MethodModel
        methodRandomTriagular:MethodModel = MethodModel("Random Triangular", RandomSearch, TrainIsTestDataSplitModel, argumentsRandomTriagular)


        # argumentsRandomRefracted:Arguments
        argumentsRandomRefracted = Arguments([Argument(RandomSearch.NUMBER_OF_RUN, 300),
                                              Argument(RandomSearch.GENERATE_OPR, operatorGenerateRefractedModel.__name__),
                                              Argument(RandomSearch.FITNESS_FNC, fitnessRMSE.__name__)])
        # methodRandomRefracted:MethodModel
        methodRandomRefracted:MethodModel = MethodModel("Random Refracted", RandomSearch, Train5Test1DataSplitModel, argumentsRandomRefracted)


        # argumentsTheHighestRating:Arguments
        argumentsTheHighestRating:Arguments = Arguments([Argument(RandomSearch.FITNESS_FNC, fitnessRMSE.__name__),
                                               Argument(RandomSearch.AGGR_OPR, AggrOperatorTwoFurthest05Points.__name__)])

        # methodRandomRefracted:MethodModel
        methodTheHighestRating:MethodModel = MethodModel("The Highest Rating", TheHighestRating, CrossValidationDataSplitModel, argumentsTheHighestRating)


        # argumentsHillClimbing:Arguments
        argumentsHillClimbing:Arguments = Arguments([Argument(HillClimbing.NUMBER_OF_RUN, 30),
                                           Argument(HillClimbing.NUMBER_OF_NEIGHBOURS, 10),
                                           Argument(HillClimbing.FITNESS_FNC, fitnessRMSE.__name__),
                                           Argument(HillClimbing.GENERATE_OPR, operatorGenerateTriangularModel.__name__),
                                           Argument(HillClimbing.NEIGHBOUR_OPR, operatorA.__name__),
                                           Argument(HillClimbing.AGGR_OPR, AggrOperatorTwoFurthest05Points.__name__)])

        # methodRandomRefracted:MethodModel
        methodHillClimbing:MethodModel = MethodModel("HillClimbing", HillClimbing, TrainIsTestDataSplitModel, argumentsHillClimbing)


        # argumentsLineaRegression:Arguments
        argumentsLineaRegression:Arguments = Arguments([Argument(LinearRegression.FITNESS_FNC, fitnessRMSE.__name__)])

        # methodRandomRefracted:MethodModel
        methodLineaRegression:MethodModel = MethodModel("LineaRegression", LinearRegression, Train5Test1DataSplitModel, argumentsLineaRegression)

        methodsModel = MethodsModel()
        methodsModel.addModel(methodRandomTriagular)
        methodsModel.addModel(methodRandomRefracted)
        methodsModel.addModel(methodTheHighestRating)
        methodsModel.addModel(methodHillClimbing)
        methodsModel.addModel(methodLineaRegression)


        return methodsModel


class MethodModel:
    def __init__(self, methodName, methodClass, dataSplitClass, arguments):
        self.methodName = methodName
        self.methodClass = methodClass
        self.dataSplitClass = dataSplitClass
        self.arguments = arguments
        self.evaluationResult = None