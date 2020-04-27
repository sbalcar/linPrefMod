#!/usr/bin/python3

from typing import List

from methods.individual.individualEvaluated import IndividualEvaluated #class

from methods.operators.evaluation.fitness_old import fitnessRMSE_ #function

from methods.operators.operatorRandomMoveTriangularModel import operatorRandomMoveTriangularModel #function

from geometry.pointWithRating import PointWithRating #class

from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from configuration.argument import Argument
from configuration.arguments import Arguments


class AMethod:

    FITNESS_FNC = "fitnessFnc"
    GENERATE_OPR = "generateOpr"

    AGGR_OPR = "aggrOpr"


    # pointsWithRatingTrain:list<PointWithRating>, argument:Arguments, linPrefModelConf:LinPrefModelConfiguration
    def search(self, pointsWithRatingTrain:List[PointWithRating], arguments:Arguments, linPrefModelConf:LinPrefModelConfiguration):
        pass