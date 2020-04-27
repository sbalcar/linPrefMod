#!/usr/bin/python3

import math
import matplotlib.pyplot as plt

from typing import List

from methods.aMethod import AMethod #class

from userProfileModel.model.prefFnc.prefFnc import PrefFnc #class

from methods.individual.individualEvaluated import IndividualEvaluated #class

from methods.operators.evaluation.fitnessRMSE import fitnessRMSE #function
from methods.operators.operatorGenerateTriangularModel import operatorGenerateTriangularModel #function
from methods.operators.operatorRandomMoveTriangularModel import operatorRandomMoveTriangularModel #function

from geometry.point import Point #class
from geometry.pointWithRating import PointWithRating #class

from geometry.lineSegment import LineSegment #class
from geometry.lineSegments import LineSegments #class

from configuration.argument import Argument
from configuration.arguments import Arguments
from configuration.linPrefModelConfiguration import LinPrefModelConfiguration #class

from methods.individual.individualUserProfileModel import IndividualUserProfileModel #class

from userProfileModel.userProfileModel import UserProfileModel #class

from userProfileModel.model.prefFnc.prefFncs import PrefFncX
from userProfileModel.model.prefFnc.prefFncs import PrefFncY
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class

import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np
import random


def transpose(A):
    return list(map(list,zip(*A)))

# Generuje n+1 polynomu stupne n jejihz soucet je 1
def polynomials(n, xs):
    def f(v,n,xs):
        math.factorial(5)
        #c = math.comb(n,v)
        c = math.factorial(n) / (math.factorial(v) * math.factorial(n - v))
        return [c * x ** v * (1-x) ** (n-v) for x in xs]
    return [f(v,n,xs) for v in range(n+1)]

# Generuje n+1 trojuhelniku jejihz soucet je 1
def triangles(n, xs):
	def triangle(v,n,x):
		if x < (v-1)/n:
			return 0
		elif x < v/n:
			return (x - (v-1)/n) * n
		elif x < (v+1)/n:
			return ((v+1)/n - x) * n
		else:
			return 0
	def trianglesMulti(v,n,xs):
		return [triangle(v,n,x) for x in xs]
	if n == 0:
		return []
	else:
		return [trianglesMulti(v,n,xs) for v in range(n+1)]

# Generuje n konstantnich binarnich funkci jejihz soucet je 1
def constants(n, xs):
	def constant(v,n,x):
		delkaUseku = 1/(n)
		usek = math.floor(x / delkaUseku)
		if v == usek:
			return 1
		else:
			return 0
	def constantsMulti(v,n,xs):
		return [constant(v,n,x) for x in xs]
	if n == 0:
		return []
	else:
		return [constantsMulti(v,n,xs) for v in range(n+1)]

# Vygeneruje hodnoty funkci v xs. Mnoztstvi dle zadanych poctu
def getRegressors(nConstants, nTriangles, nPolynomials, xs):
	return constants(nConstants,xs)[1:] + \
		triangles(nTriangles,xs)[1:] + \
		polynomials(nPolynomials,xs)[1:]


class LinearRegression(AMethod):

    # pointsWithRatingTrain:list<PointWithRating>, argument:Arguments, linPrefModelConf:LinPrefModelConfiguration
    def search(self, pointsWithRatingTrain:List[PointWithRating], arguments:Arguments, linPrefModelConf:LinPrefModelConfiguration):
        print("LineaRegression")

        # argFitnessFnc:Argument
        argFitnessFnc:Argument = arguments.exportArgument(self.FITNESS_FNC)
        # fitnessFnc:Function
        fitnessFnc = argFitnessFnc.exportValueAsFnc()

        configs:List[List[int]] = [[7, 4, 0], [7, 7, 1]]
        (preferenceFunctionsCoefs, agregationFunctionCoefs) = self.__trainModel(pointsWithRatingTrain, configs)

        N:int = 100
        rangeN:List[float] = [i / N for i in list(range(0, N))]

        prefFncsPoints:List[List[Point]] = []
        for (preferenceFunctionCoefsI, configI) in zip(preferenceFunctionsCoefs, configs):
            #print(f"Model pro dimenzi:")
            #print(preferenceFunctionCoefs)
            (interceptI, noveKoeficienty) = preferenceFunctionCoefsI
            y:List[float] = interceptI + np.dot(noveKoeficienty, np.array(getRegressors(*configI, rangeN)))

            pointsI:List[Point] = [Point(float(pI[0]), float(pI[1])) for pI in list(zip(rangeN, y))]
            prefFncsPoints.append(pointsI)

            #plt.plot(rangeN, np.array([pI.point.y for pI in pointsWithRatingTrain]), 'b.', rangeN, y, 'r.');
            #plt.show()

        #print(f"Model pro kombinaci:")
        #print(agregationFunctionCoefs)

        lineSegmentsX:LineSegments = LineSegments.createPointToPoint(prefFncsPoints[0])
        lineSegmentsY:LineSegments = LineSegments.createPointToPoint([Point(pI.y, pI.x) for pI in prefFncsPoints[1]])

        prefFncX:PrefFncX = PrefFncX.createFromLineSegments(lineSegmentsX.lineSegments)
        prefFncY:PrefFncY = PrefFncY.createFromLineSegments(lineSegmentsY.lineSegments)
        #prefFncX: PrefFncX = PrefFncX.createFromLineSegments([LineSegment(Point(0.0, 0.0), Point(1.0, 1.0))])
        #prefFncY: PrefFncY = PrefFncY.createFromLineSegments([LineSegment(Point(0.1, 0.0), Point(1.0, 1.0))])
        aggrFnc:AggrFnc = AggrFnc([0.5, 0.5])

        upModel:UserProfileModel = UserProfileModel(prefFncX, prefFncY, aggrFnc)
        individual = IndividualUserProfileModel(upModel)




        # points:list<Point>
        points:List[Point] = [p.point for p in pointsWithRatingTrain]
        # rating:list<float>
        rating:List[float] = [float(p.rating) for p in pointsWithRatingTrain]

        # ratingsPredicted:list<float>
        ratingsPredicted: List[float] = individual.preferenceOfPointsInDC(points, linPrefModelConf)

        # fitnessRMSETrain:float
        fitnessRMSETrain: float = fitnessFnc(ratingsPredicted, rating)

        return IndividualEvaluated(individual, fitnessRMSETrain)



    def __trainModel(self, pointsWithRating:List[PointWithRating], configs:List[List[int]]):

        xs:List[float] = [pWithRatingI.point.x for pWithRatingI in pointsWithRating]
        ys:List[float] = [pWithRatingI.point.y for pWithRatingI in pointsWithRating]
        ratings:List[float] = [pWithRatingI.rating for pWithRatingI in pointsWithRating]

        nDims:int = 2
        features:List[List[float]] = [xs, ys]
        target:List[float] = ratings

        regressors = []
        regressorsPerDim = []
        nSplits:int = 7
        for dim in range(nDims):
            regressorsForDimI = getRegressors(*configs[dim], features[dim])
            regressors = regressors + regressorsForDimI
            regressorsPerDim.append(regressorsForDimI)

        x = np.array(transpose(regressors))
        model = sklearn.linear_model.LinearRegression().fit(x, target)

        start = 0
        predictions = []
        preferenceFunctionsCoefs = []
        for dim in range(nDims):
            end = start + len(regressorsPerDim[dim])
            A = model.coef_[start:end]
            B = np.array(regressorsPerDim[dim])
            start = end
            C = np.dot(A,B)
            C = C.reshape(-1,1)
            m = sklearn.linear_model.LinearRegression().fit(C,target)
            predictions.append(m.predict(C))
            noveKoeficienty = m.coef_*A
            preferenceFunctionsCoefs.append((m.intercept_,noveKoeficienty))
            #plt.plot(y); plt.show()

        X = np.transpose(np.array(predictions))
        combinationModel = sklearn.linear_model.LinearRegression().fit(X, target)

        agregationFunctionCoefs = (combinationModel.intercept_,combinationModel.coef_)
        return (preferenceFunctionsCoefs,agregationFunctionCoefs)
