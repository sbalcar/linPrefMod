#!/usr/bin/python3

from typing import List

from methods.aMethod import AMethod #class

from methods.individual.individualEvaluated import IndividualEvaluated #class

from methods.operators.evaluation.fitnessRMSE import fitnessRMSE #function
from methods.operators.operatorGenerateTriangularModel import operatorGenerateTriangularModel #function
from methods.operators.operatorRandomMoveTriangularModel import operatorRandomMoveTriangularModel #function

from geometry.pointWithRating import PointWithRating #class

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from configuration.argument import Argument
from configuration.arguments import Arguments

class HillClimbing(AMethod):

    NUMBER_OF_RUN = "numberOfRun"
    NUMBER_OF_NEIGHBOURS = "numberOfNeighbours"
    NEIGHBOUR_OPR = "neighbourOpr"

    # pointsWithRatingTrain:list<PointWithRating>, argument:Arguments, linPrefModelConf:LinPrefModelConfiguration
    def search(self, pointsWithRatingTrain:List[PointWithRating], arguments:Arguments, linPrefModelConf:LinPrefModelConfiguration):
        # argNumberOfRun:Argument
        argNumberOfRun:Argument = arguments.exportArgument(self.NUMBER_OF_RUN)
        numberOfGenerations:int = argNumberOfRun.exportValueAsInt()

        # argNumberOfRun:Argument
        argNumberOfNeighbours:Argument = arguments.exportArgument(self.NUMBER_OF_NEIGHBOURS)
        numberOfNeighbours:int = argNumberOfNeighbours.exportValueAsInt()

        # argFitnessFnc:Argument
        argFitnessFnc:Argument = arguments.exportArgument(self.FITNESS_FNC)
        fitnessFnc = argFitnessFnc.exportValueAsFnc()

        # argGenerateFnc:Argument
        argGenerateFnc:Argument = arguments.exportArgument(self.GENERATE_OPR)
        generateFnc = argGenerateFnc.exportValueAsFnc()

        # argNeighbourOpr:Argument
        argNeighbourOpr:Argument = arguments.exportArgument(self.NEIGHBOUR_OPR)
        neighbourOpr = argNeighbourOpr.exportValueAsFnc()

        return self.__search(pointsWithRatingTrain, linPrefModelConf, numberOfGenerations=numberOfGenerations,
                             numberOfNeighbours=numberOfNeighbours,
                             fitnessFnc=fitnessFnc, generateFnc=generateFnc, neighborFnc=neighbourOpr)


    # pointsWithRatingTrain:list<PointWithRating>, linPrefModelConf:LinPrefModelConfiguration, numberOfGenerations:Float, fitnessFnc:Function, generateFnc:Function, neighborFnc:Function
    def __search(self, pointsWithRatingTrain, linPrefModelConf, numberOfGenerations=10, numberOfNeighbours=10,
                 fitnessFnc=fitnessRMSE, generateFnc=operatorGenerateTriangularModel, neighborFnc=operatorRandomMoveTriangularModel):

        print("HillClimbing")
        # print("numberOfGenerations: " + str(numberOfGenerations))
        # print("fitnessFnc: " + fitnessFnc.__name__)
        # print("generateFnc: " + generateFnc.__name__)

        # points:list<Point>
        points = [p.point for p in pointsWithRatingTrain]
        # rating:list<float>
        rating = [p.rating for p in pointsWithRatingTrain]

        # currentIndiv:AIndividual
        currentIndiv = generateFnc(linPrefModelConf)

        # currentPredicted:list<float>
        currentPredicted = currentIndiv.preferenceOfPointsInDC(points, linPrefModelConf)

        # currentFitness:float
        currentFitness = fitnessFnc(currentPredicted, rating)

        for i in range(numberOfGenerations):
           print("Generation: " + str(i))

           # individualNew:IndividualUser, pointsWithRatingTrain:list<PointWithRating>, currentPredicted:list<float>
           individualsNew = neighborFnc(numberOfNeighbours, currentIndiv, pointsWithRatingTrain, currentPredicted, linPrefModelConf)

           # individualNew:IndividualUserProfilemModel
           individualNew = self.__theBestNeighbour(individualsNew, pointsWithRatingTrain, fitnessFnc, linPrefModelConf)

           # ratingsPredicted:list<float>
           ratingsPredictedNew = individualNew.preferenceOfPointsInDC(points, linPrefModelConf)

           # fitnessNew:float
           fitnessNew = fitnessFnc(ratingsPredictedNew, rating)
           #print("fitnessRMSETrainNew: ", fitnessRMSETrainNew);

           if fitnessNew < currentFitness:
               print("Hop")
               currentIndiv = individualNew
               currentFitness = fitnessNew

           #print("currentFitness: ", currentFitness)

        return IndividualEvaluated(currentIndiv, currentFitness)

    # individuals:list<IndividualUserProfile>, pointsWithRatingTrain:list<PointWithRating>, fitnessFnc:Function, linPrefModelConf:LinPrefModelConfiguration
    def __theBestNeighbour(self, individuals, pointsWithRatingTrain, fitnessFnc, linPrefModelConf):

        # points:list<Point>
        points = [p.point for p in pointsWithRatingTrain]
        # rating:list<float>
        rating = [p.rating for p in pointsWithRatingTrain]

        individualTheBest = None
        fitnessTheBest = 1000

        for individualI in individuals:

            # ratingsPredictedNewI:list<float>
            ratingsPredictedNewI = individualI.preferenceOfPointsInDC(points, linPrefModelConf)

            # fitnessNew:float
            fitnessNewI = fitnessFnc(ratingsPredictedNewI, rating)

            if fitnessNewI < fitnessTheBest:
                individualTheBest = individualI
                fitnessTheBest = fitnessNewI

        return individualTheBest