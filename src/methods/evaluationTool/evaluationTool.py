#!/usr/bin/python3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QHBoxLayout, QLayout, QGroupBox, QFormLayout, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QHBoxLayout, QLayout, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

from geometry.pointsWithRating import PointsWithRating #class

from methods.randomSearch import RandomSearch #class
from configuration.linPrefModelConfiguration import LinPrefModelConfiguration
from configuration.arguments import Arguments #class
from geometry.pointWithRating import PointWithRating

from methods.operators.evaluation.fitnessRMSE import fitnessRMSE #function
from methods.operators.evaluation.fitnessRMSE90 import fitnessRMSE90 #function
from methods.operators.operatorGenerateTriangularModel import operatorGenerateTriangularModel #function
from methods.operators.evaluation.fitnessPrecision import fitnessPrecision #function
from methods.operators.evaluation.fitnessRecall import fitnessRecall #function

from methods.evaluationTool.evaluationResult import EvaluationResult

class EvaluationTool:

    # individual:AIndividual, pointsWithRatingTest:list<PointWithRating>, linPrefModelConf:LinPrefModelConfiguration
    def evalIndividual(individual, pointsWithRatingTest, linPrefModelConf):

        points = [p.point for p  in pointsWithRatingTest]
        ratings = [p.rating for p in pointsWithRatingTest]

        ratingsPredicted = individual.preferenceOfPointsInDC(points, linPrefModelConf)

        # fitnessRMSETest:float
        fitnessRMSETest = fitnessRMSE(ratingsPredicted, ratings)

        # fitnessRMSE90Test:float
        fitnessRMSE90Test = fitnessRMSE90(ratingsPredicted, ratings)

        # fitnessPrecisionTest:float
        fitnessPrecisionTest = fitnessPrecision(ratingsPredicted, ratings)

        # fitnessRecallTest:float
        fitnessRecallTest = fitnessRecall(ratingsPredicted, ratings)

        # pWithRating:PointWithRating
        pWithRating = PointsWithRating(pointsWithRatingTest).pointWithTheHighestError(ratingsPredicted)
        print("theWorstX: " + str(pWithRating.point.x))

        # eResult:EvaluationResult
        eResult = EvaluationResult()
        eResult.fitnessRMSE = fitnessRMSETest
        eResult.fitnessRMSE90 = fitnessRMSE90Test
        eResult.fitnessPrecision = fitnessPrecisionTest
        eResult.fitnessRecall = fitnessRecallTest

        return eResult