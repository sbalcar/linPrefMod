#!/usr/bin/python3

from typing import List

from methods.aMethod import AMethod #class

from methods.individual.individualEvaluated import IndividualEvaluated #class

from methods.operators.evaluation.fitness_old import fitnessRMSE_ #function

from methods.operators.operatorGenerateTriangularModel import operatorGenerateTriangularModel #function
from methods.operators.operatorRandomMoveTriangularModel import operatorRandomMoveTriangularModel #function
from methods.individual.individualUserTrinity import IndividualUserTrinity #class

from userProfileModel.model.prefFnc.model.prefFncTriangularModel import PrefFncTriangularModel
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc
from userProfileModel.userProfileModel import UserProfileModel
from userProfileModel.userProfileModelStructured import UserProfileModelStructured

from geometry.pointsWithRating import PointsWithRating
from geometry.pointWithRating import PointWithRating
from geometry.point import Point

from methods.operators.aggregation.aggrOperatorTwoFurthest05Points import AggrOperatorTwoFurthest05Points

from geometry.pointWithRating import PointWithRating #class

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from configuration.argument import Argument
from configuration.arguments import Arguments

class TheHighestRating(AMethod):

    # pointsWithRatingTrain:list<PointWithRating>, argument:Arguments, linPrefModelConf:LinPrefModelConfiguration
    def search(self, pointsWithRatingTrain:List[PointWithRating], arguments:Arguments, linPrefModelConf:LinPrefModelConfiguration):

        # argFitnessFnc:Argument
        argFitnessFnc:Argument = arguments.exportArgument(self.FITNESS_FNC)
        # argAgregationClass:Argument
        argAgregationClass:Argument = arguments.exportArgument(self.AGGR_OPR)

        # fitnessFnc:Function
        fitnessFnc = argFitnessFnc.exportValueAsFnc()
        # agregationClass:class
        agregationClass = argAgregationClass.exportValueAsClass()

        # points:list<Point>
        points = [p.point for p in pointsWithRatingTrain]
        # rating:list<float>
        rating = [p.rating for p in pointsWithRatingTrain]

        # pointsSorted:list<PointWithRating>
        pointsSorted = sorted(pointsWithRatingTrain, key=lambda p: p.rating, reverse=True)
        # point:Point
        point = pointsSorted[0].point

        # prefFncX:PrefFncTriangularModel
        prefFncX = PrefFncTriangularModel(point.x)
        prefFncY = PrefFncTriangularModel(point.y)

        # wx:float
        wx = agregationClass.run(
            prefFncX.exportAsPrefFncX(linPrefModelConf),
            prefFncY.exportAsPrefFncY(linPrefModelConf),
            pointsWithRatingTrain,
            linPrefModelConf)

        # individual:AIndividual
        individual = IndividualUserTrinity(prefFncX.iCoordinate, prefFncY.iCoordinate, wx)

        # ratingsPredicted:list<float>
        ratingsPredicted = individual.preferenceOfPointsInDC(points, linPrefModelConf)

        # fitnessRMSETrain:float
        fitnessRMSETrain = fitnessFnc(ratingsPredicted, rating)
        #print("fitnessRMSETrain: ", fitnessRMSETrain);

        return IndividualEvaluated(individual, fitnessRMSETrain)
