#!/usr/bin/python3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QHBoxLayout, QLayout, QGroupBox, QFormLayout, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QLabel, QComboBox, QPushButton, QLineEdit, QHBoxLayout, QLayout, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

from methods.randomSearch import RandomSearch #class
from configuration.linPrefModelConfiguration import LinPrefModelConfiguration
from configuration.arguments import Arguments #class
from geometry.pointWithRating import PointWithRating

from methods.operators.evaluation.fitnessRMSE import fitnessRMSE #function
from methods.operators.operatorGenerateTriangularModel import operatorGenerateTriangularModel #function
from methods.operators.evaluation.fitnessPrecision import fitnessPrecision #function
from methods.operators.evaluation.fitnessRecall import fitnessRecall #function
from methods.evaluationTool.evaluationTool import EvaluationTool #class
from methods.dataSplit.dataSplitModel import DataSplitModel #class

from methods.dataSplit.splitting.trainIsTestDataSplitModel import TrainIsTestDataSplitModel #class
from methods.dataSplit.splitting.train5Test1DataSplitModel import Train5Test1DataSplitModel #class
from methods.dataSplit.splitting.crossValidationDataSplit import CrossValidationDataSplitModel #class
from methods.evaluationTool.evaluationResult import EvaluationResult #class


class MethodsForm:

    METHOD_COLUMN_INDEX = 0
    METHODCLASS_COLUMN_INDEX = 1
    PARAMETERS_COLUMN_INDEX = 2
    DATASPLIT_COLUMN_INDEX = 3
    TRAINING_COLUMN_INDEX = 4
    DISPLAY_COLUMN_INDEX = 5
    RMSE_COLUMN_INDEX = 6
    RMSE90_COLUMN_INDEX = 7
    PRECISION_COLUMN_INDEX = 8
    RECALL_COLUMN_INDEX = 9

    NUMBER_OF_COLUMNS = 10

    # methodsModel:MethodsModel, pointsVisitedPC:List<PointWithRating>, linPrefModelConf:LinPrefModelConfiguration, updateModelFnc:Function
    def __init__(self, methodsModel, pointsWithRatingDC, linPrefModelConf, updateModelFnc):
        self.methodsModel = methodsModel
        self.pointsWithRatingDC = pointsWithRatingDC
        self.linPrefModelConf = linPrefModelConf
        self.updateModelFnc = updateModelFnc

        self.qTableWidget = QTableWidget(len(self.methodsModel.methods), self.NUMBER_OF_COLUMNS)
        self.qTableWidget.setHorizontalHeaderLabels(['Method Name', 'Method class', 'Parameters', 'DataSplit', 'Train', 'Display', 'RMSE', 'RMSE90', 'Precision', 'Recall'])
        self.qTableWidget.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        #self.qTableWidget
        self.qTableWidget.setColumnWidth(self.METHOD_COLUMN_INDEX, 140)
        self.qTableWidget.setColumnWidth(self.DATASPLIT_COLUMN_INDEX, 120)
        self.qTableWidget.setColumnWidth(self.TRAINING_COLUMN_INDEX, 80)
        self.qTableWidget.setColumnWidth(self.DISPLAY_COLUMN_INDEX, 80)
        self.qTableWidget.setColumnWidth(self.RMSE_COLUMN_INDEX, 70)
        self.qTableWidget.setColumnWidth(self.RMSE90_COLUMN_INDEX, 70)
        self.qTableWidget.setColumnWidth(self.PRECISION_COLUMN_INDEX, 70)
        self.qTableWidget.setColumnWidth(self.RECALL_COLUMN_INDEX, 70)

        for mId in range(len(self.methodsModel.methods)):
            methodI = self.methodsModel.methods[mId]
            self.__addMethod(methodI, mId)

        # layoutToolMethods:QFormLayout
        layoutToolMethods = QFormLayout()
        layoutToolMethods.addRow(self.qTableWidget)

        # qGroupBoxToolMethods:QGroupBox
        self.qGroupBoxToolMethods = QGroupBox("Methods")
        self.qGroupBoxToolMethods.setLayout(layoutToolMethods)


    # methodI:MethodModel, rowNumber:int
    def __addMethod(self, methodI, rowNumber):

        rmse = None
        rmse90 = None
        precision = None
        recall = None
        if methodI.evaluationResult is not None:
            eResult = methodI.evaluationResult
            if eResult.fitnessRMSE is not None:
               rmse = round(eResult.fitnessRMSE, 5)
            if eResult.fitnessRMSE90 is not None:
               rmse90 = round(eResult.fitnessRMSE90, 5)
            if eResult.fitnessPrecision is not None:
               precision = round(eResult.fitnessPrecision, 5)
            if eResult.fitnessRecall is not None:
               recall = round(eResult.fitnessRecall, 5)

        # index:int
        index = DataSplitModel.getIndex(methodI.dataSplitClass)

        qTableWidgetItemMethod = QTableWidgetItem(methodI.methodName)
        qTableWidgetItemMethod.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)

        qTableWidgetItemMethodClass = QTableWidgetItem(str(methodI.methodClass.__name__))
        qTableWidgetItemMethodClass.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)

        qLineEditParameters = QLineEdit()
        qLineEditParameters.setText(methodI.arguments.exportAsString())

        qComboBoxDataSplit = QComboBox()
        qComboBoxDataSplit.addItem(TrainIsTestDataSplitModel.name)
        qComboBoxDataSplit.addItem(Train5Test1DataSplitModel.name)
        qComboBoxDataSplit.addItem(CrossValidationDataSplitModel.name)
        qComboBoxDataSplit.setCurrentIndex(index)
        qComboBoxDataSplit.currentIndexChanged.connect(lambda: self.__dataSplitChanged(methodI, qComboBoxDataSplit.currentIndex()))

        qPushButtonTrain = QPushButton()
        qPushButtonTrain.clicked.connect(lambda: self.__trainByMethod(rowNumber))
        qPushButtonTrain.setText('Run')

        qPushButtonDisplay = QPushButton()
        qPushButtonDisplay.clicked.connect(lambda: self.__displayRandom(rowNumber))
        qPushButtonDisplay.setText('Show')

        qTableWidgetItemRMSE = QTableWidgetItem(str(rmse))
        qTableWidgetItemRMSE.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)

        qTableWidgetItemRMSE90 = QTableWidgetItem(str(rmse90))
        qTableWidgetItemRMSE90.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)

        qTableWidgetItemPrecision = QTableWidgetItem(str(precision))
        qTableWidgetItemPrecision.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)

        qTableWidgetItemRecall = QTableWidgetItem(str(recall))
        qTableWidgetItemRecall.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)

        self.qTableWidget.setItem(rowNumber, self.METHOD_COLUMN_INDEX, qTableWidgetItemMethod)
        self.qTableWidget.setItem(rowNumber, self.METHODCLASS_COLUMN_INDEX, qTableWidgetItemMethodClass)
        self.qTableWidget.setCellWidget(rowNumber, self.PARAMETERS_COLUMN_INDEX, qLineEditParameters)
        self.qTableWidget.setCellWidget(rowNumber, self.DATASPLIT_COLUMN_INDEX, qComboBoxDataSplit)

        self.qTableWidget.setCellWidget(rowNumber, self.TRAINING_COLUMN_INDEX, qPushButtonTrain)
        self.qTableWidget.setCellWidget(rowNumber, self.DISPLAY_COLUMN_INDEX, qPushButtonDisplay)
        self.qTableWidget.setItem(rowNumber, self.RMSE_COLUMN_INDEX, qTableWidgetItemRMSE)
        self.qTableWidget.setItem(rowNumber, self.RMSE90_COLUMN_INDEX, qTableWidgetItemRMSE90)
        self.qTableWidget.setItem(rowNumber, self.PRECISION_COLUMN_INDEX, qTableWidgetItemPrecision)
        self.qTableWidget.setItem(rowNumber, self.RECALL_COLUMN_INDEX, qTableWidgetItemRecall)

    # methodModel:MethodModel, currentIndex:int
    def __dataSplitChanged(self, methodModel, currentIndex):
        dataSplitClass = DataSplitModel.getDataSplitModel(currentIndex)

        methodModel.dataSplitClass = dataSplitClass


    def __trainByMethod(self, rowNumber):

        # methodModel:MethodModel
        methodModel = self.methodsModel.methods[rowNumber]
        # print("Method: " + methodModel.methodName)

        # qLineEditDataSplit:QComboBox
        qComboBoxDataSplit = self.qTableWidget.cellWidget(rowNumber, self.DATASPLIT_COLUMN_INDEX)
        # indexDataSplit:QComboBox
        indexDataSplit = qComboBoxDataSplit.currentIndex()

        # qLineEditParameters:QLineEdit
        qLineEditParameters = self.qTableWidget.cellWidget(rowNumber, self.PARAMETERS_COLUMN_INDEX)
        # arguments:Arguments
        arguments = Arguments.importAsString(qLineEditParameters.text())

        # dataSplitClass:class
        dataSplitClass = DataSplitModel.getDataSplitModel(indexDataSplit)
        #print("dataSplitClass: " + str(dataSplitClass))

        # methodClass:class
        methodClass = methodModel.methodClass


        # individual:Individual, eResult:EvaluationResult
        individual, eResult = self.__run(dataSplitClass, methodClass, arguments)
        #eResult.printEvaluationResult()


        methodModel.evaluationResult = eResult

        self.methodsModel.currentUserProfileModel = individual.exportUserProfileModel(self.linPrefModelConf)


    # dataSplitClass:class, methodClass:class, arguments:Arguments
    def __run(self, dataSplitClass, methodClass, arguments):

        # theBestIndividual:Individual
        theBestIndividual = None
        # theBestFitness:float
        theBestFitness = 100000
        # eResults:list<EvaluationResult>
        eResults = []

        # dataSplit:ADataSplit
        dataSplit = dataSplitClass()
        for runI in range(dataSplit.numberOfSplitting()):

            # pointsWithRatingTrain:list<PointWithRating>, pointsWithRatingTest:list<PointWithRating>
            pointsWithRatingTrain, pointsWithRatingTest = dataSplit.split(self.pointsWithRatingDC)

            # method:AMethod
            method = methodClass()
            # individualEval:IndividualEvaluation
            individualEval = method.search(pointsWithRatingTrain, arguments, self.linPrefModelConf)

            # individualI:Individual
            individualI = individualEval.individual
            fitnessI = individualEval.fitness

            if fitnessI < theBestFitness:
                theBestIndividual = individualI
                theBestFitness = fitnessI

            # eResultI:EvaluationResult
            eResultI = EvaluationTool.evalIndividual(individualI, pointsWithRatingTest, self.linPrefModelConf)
            eResults.append(eResultI)

        theBesteResult = EvaluationResult.exportAverageEvaluationResult(eResults)

        return (theBestIndividual, theBesteResult)



    # rowNumber:int
    def __displayRandom(self, rowNumber):
        self.updateModelFnc()

