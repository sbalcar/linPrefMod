#!/usr/bin/python3


class EvaluationResult:

    # fitnessRMSE:float
    fitnessRMSE = None
    # fitnessRMSE90:float
    fitnessRMSE90 = None
    # fitnessPrecision:float
    fitnessPrecision = None
    # fitnessRecall:float
    fitnessRecall = None


    def printEvaluationResult(self):
        print("RMSE: " + str(self.fitnessRMSE))
        print("RMSE90: " + str(self.fitnessRMSE90))
        print("Precision: " + str(self.fitnessPrecision))
        print("Recall: " + str(self.fitnessRecall))

    # evaluationResults:list<EvaluationResult>
    def exportAverageEvaluationResult(evaluationResults):
        # n:int
        n = len(evaluationResults)
        # sumRMSE:float
        sumRMSE = 0
        sumRMSE90 = 0
        sumPrecision = 0
        sumRecall = 0
        for eResultI in evaluationResults:
            eResultI.printEvaluationResult()
            if sumRMSE is None or eResultI.fitnessRMSE is None:
                sumRMSE = None
            else:
                sumRMSE = sumRMSE + eResultI.fitnessRMSE

            if sumRMSE90 is None or eResultI.fitnessRMSE90 is None:
                sumRMSE90 = None
            else:
                sumRMSE90 = sumRMSE90 + eResultI.fitnessRMSE90

            if sumPrecision is None or eResultI.fitnessPrecision is None:
                sumPrecision = None
            else:
                sumPrecision = sumPrecision + eResultI.fitnessPrecision

            if sumRecall is None or eResultI.fitnessRecall is None:
                sumRecall = None
            else:
                sumRecall = sumRecall + eResultI.fitnessRecall

        eResult = EvaluationResult()
        if sumRMSE is not None:
            eResult.fitnessRMSE = sumRMSE / n
        if sumRMSE90 is not None:
            eResult.fitnessRMSE90 = sumRMSE90 / n
        if sumPrecision is not None:
            eResult.fitnessPrecision = sumPrecision / n
        if sumRecall is not None:
            eResult.fitnessRecall = sumRecall / n

        return eResult