#!/usr/bin/python3

from methods.individual.individualEvaluated import IndividualEvaluated #class

from methods.operators.evaluation.fitness_old import fitnessRMSE_ #function

#from methods.operators.operator import operatorGenerate #function
from methods.operators.operatorRandomMoveTriangularModel import operatorRandomMoveTriangularModel #function


class AMethod:

    FITNESS_FNC = "fitnessFnc"
    GENERATE_OPR = "generateOpr"

    AGGR_OPR = "aggrOpr"


    # pointsTrain:Point[], prefsTrain:Point[], arguments:Arguments, linPrefModelConf:LinPrefModelConfiguration,
    def search(self, pointsTrain, prefsTrain, arguments, linPrefModelConf):
        pass