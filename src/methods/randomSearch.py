#!/usr/bin/python3

import sys

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration

from methods.aMethod import AMethod #class

from methods.individual.individualEvaluated import IndividualEvaluated #class

from methods.operators.evaluation.fitnessRMSE import fitnessRMSE #function
from methods.operators.operatorGenerateTriangularModel import operatorGenerateTriangularModel #function


class RandomSearch(AMethod):

    NUMBER_OF_RUN = "numberOfRun"


    # pointsWithRatingTrain:list<PointWithRating>, argument:Arguments, modelConf:LinPrefModelConfiguration
    def search(self, pointsWithRatingTrain, arguments, linPrefModelConf):
        # argNumberOfRun:Argument
        argNumberOfRun = arguments.exportArgument(self.NUMBER_OF_RUN)
        numberOfGenerations = argNumberOfRun.exportValueAsInt()

        # argFitnessFnc:Argument
        argFitnessFnc = arguments.exportArgument(self.FITNESS_FNC)
        fitnessFnc = argFitnessFnc.exportValueAsFnc()

        # argGenerateFnc:Argument
        argGenerateFnc = arguments.exportArgument(self.GENERATE_OPR)
        generateFnc = argGenerateFnc.exportValueAsFnc()

        return self.__search(pointsWithRatingTrain, linPrefModelConf, numberOfGenerations=numberOfGenerations, fitnessFnc=fitnessFnc, generateFnc=generateFnc)

    # pointsWithRatingTrain:list<PointWithRating>, linPrefModelConf:LinPrefModelConfiguration, numberOfGenerations:Float, fitnessFnc:Function, generateFnc:Function
    def __search(self, pointsWithRatingTrain, linPrefModelConf, numberOfGenerations=10, fitnessFnc=fitnessRMSE, generateFnc=operatorGenerateTriangularModel):

        #print("RandomSearch")
        #print("numberOfGenerations: " + str(numberOfGenerations))
        #print("fitnessFnc: " + fitnessFnc.__name__)
        #print("generateFnc: " + generateFnc.__name__)

        # points:list<Point>
        points = [p.point for p in pointsWithRatingTrain]
        # rating:list<float>
        rating = [p.rating for p in pointsWithRatingTrain]

        theBestIndiv = None;
        theBestFitness = 1000;

        for i in range(numberOfGenerations):

            # individual:AIndividual
            individual = generateFnc(linPrefModelConf)
            # ratingsPredicted:list<float>
            ratingsPredicted = individual.preferenceOfPointsInDC(points, linPrefModelConf)

            # fitnessRMSETrain:float
            fitnessRMSETrain = fitnessFnc(ratingsPredicted, rating)
            #print("fitnessRMSETrain: ", fitnessRMSETrain);

            if fitnessRMSETrain < theBestFitness:
                theBestIndiv = individual;
                theBestFitness = fitnessRMSETrain;

        return IndividualEvaluated(theBestIndiv, theBestFitness)


