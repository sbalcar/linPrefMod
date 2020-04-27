#!/usr/bin/python3

import sys
from typing import List

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration

from methods.aMethod import AMethod #class

from methods.individual.aIndividual import AIndividual #class
from methods.individual.individualEvaluated import IndividualEvaluated #class

from methods.operators.evaluation.fitnessRMSE import fitnessRMSE #function
from methods.operators.operatorGenerateTriangularModel import operatorGenerateTriangularModel #function

from geometry.point import Point #class
from geometry.pointWithRating import PointWithRating #class

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from configuration.argument import Argument
from configuration.arguments import Arguments


class RandomSearch(AMethod):

    NUMBER_OF_RUN = "numberOfRun"


    # pointsWithRatingTrain:list<PointWithRating>, argument:Arguments, linPrefModelConf:LinPrefModelConfiguration
    def search(self, pointsWithRatingTrain:List[PointWithRating], arguments:Arguments, linPrefModelConf:LinPrefModelConfiguration):
        # argNumberOfRun:Argument
        argNumberOfRun:Argument = arguments.exportArgument(self.NUMBER_OF_RUN)
        numberOfGenerations:int = argNumberOfRun.exportValueAsInt()

        # argFitnessFnc:Argument
        argFitnessFnc:Argument = arguments.exportArgument(self.FITNESS_FNC)
        fitnessFnc = argFitnessFnc.exportValueAsFnc()

        # argGenerateFnc:Argument
        argGenerateFnc:Argument = arguments.exportArgument(self.GENERATE_OPR)
        generateFnc = argGenerateFnc.exportValueAsFnc()

        return self.__search(pointsWithRatingTrain, linPrefModelConf, numberOfGenerations=numberOfGenerations, fitnessFnc=fitnessFnc, generateFnc=generateFnc)

    # pointsWithRatingTrain:list<PointWithRating>, linPrefModelConf:LinPrefModelConfiguration, numberOfGenerations:Float, fitnessFnc:Function, generateFnc:Function
    def __search(self, pointsWithRatingTrain:List[PointWithRating], linPrefModelConf:LinPrefModelConfiguration,
                 numberOfGenerations:int=10, fitnessFnc=fitnessRMSE, generateFnc=operatorGenerateTriangularModel):

        #print("RandomSearch")
        #print("numberOfGenerations: " + str(numberOfGenerations))
        #print("fitnessFnc: " + fitnessFnc.__name__)
        #print("generateFnc: " + generateFnc.__name__)

        # points:list<Point>
        points:List[Point] = [p.point for p in pointsWithRatingTrain]
        # rating:list<float>
        rating:List[float] = [p.rating for p in pointsWithRatingTrain]

        theBestIndiv:AIndividual = None
        theBestFitness:float = 1000

        for i in range(numberOfGenerations):

            # individual:AIndividual
            individual:AIndividual = generateFnc(linPrefModelConf)
            # ratingsPredicted:list<float>
            ratingsPredicted:List[float] = individual.preferenceOfPointsInDC(points, linPrefModelConf)

            # fitnessRMSETrain:float
            fitnessRMSETrain:float = fitnessFnc(ratingsPredicted, rating)
            #print("fitnessRMSETrain: ", fitnessRMSETrain);

            if fitnessRMSETrain < theBestFitness:
                theBestIndiv:AIndividual = individual;
                theBestFitness:float = fitnessRMSETrain;

        return IndividualEvaluated(theBestIndiv, theBestFitness)


