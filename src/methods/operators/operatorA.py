#!/usr/bin/python3

import random

from methods.individual.individualUserProfileModel import IndividualUserProfileModel #class

from userProfileModel.userProfileModel import UserProfileModel #class
from userProfileModel.model.prefFnc.model.prefFncRefractedModel import PrefFncRefractedModel #class
from userProfileModel.model.prefFnc.model.prefFncTriangularModel import PrefFncTriangularModel #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncX

from methods.operators.aggregation.aggrOperatorTwoFurthest05Points import AggrOperatorTwoFurthest05Points

from geometry.pointWithRating import PointWithRating #class
from geometry.pointsWithRating import PointsWithRating #class

from geometry.lineSegments import LineSegments #class
from geometry.lineSegment import LineSegment #class
from geometry.points import Points #class
from geometry.point import Point #class


# numberOfNeighbours:int, individual:IndividualUserProfileModel, pointsWithRatingTrain:list<PointWithRating>, currentPredicted:list<float>, linPrefModelConf:LinPrefModelConfiguration
def operatorA(numberOfNeighbours, individual, pointsWithRatingTrain, currentPredictions, linPrefModelConf):
    print("operatorA")
    # upModel:UserProfileModel
    upModel = individual.exportUserProfileModel(linPrefModelConf)

    # pWithRating:PointWithRating
    pWithRating = PointsWithRating(pointsWithRatingTrain).pointWithTheHighestError(currentPredictions)

    # upModel:UserProfileModel
    upModel = individual.exportUserProfileModel(linPrefModelConf)

    # upModels:list<UserProfileModel>
    upModels = __neighboursOfUserProfileModel(numberOfNeighbours, upModel, pointsWithRatingTrain, pWithRating.point, linPrefModelConf)

    # individuals:list<IndividualUserProfileModel>
    individuals = [IndividualUserProfileModel(upModelI) for upModelI in upModels]

    # list<IndividualUserProfileModel>
    return individuals

# numberOfNeighbours:int, upModel:UserProfileModel, theWorstPoint:Point, linPrefModelConf:LinPrefModelConfiguration
def __neighboursOfUserProfileModel(numberOfNeighbours, upModel, pointsWithRatingTrain, theWorstPoint, linPrefModelConf):
    # prefFncX:PrefFncX
    prefFncX = upModel.prefFncX
    prefFncY = upModel.prefFncY
    #aggrFnc = upModel.aggrFnc

    upModels = []
    for i in range(numberOfNeighbours):
        # prefFncXNew:PrefFncX
        prefFncXNewI = __neighboursOfPrefFncX(prefFncX, theWorstPoint.x)

        # aggrNew:float
        aggrNew = AggrOperatorTwoFurthest05Points.run(prefFncXNewI, prefFncY, pointsWithRatingTrain, linPrefModelConf)

        # upModel:UserProfileModel
        upModelNewI = UserProfileModel(prefFncXNewI, prefFncY, AggrFnc([aggrNew, 1 -aggrNew]))
        #upModelNewI = UserProfileModel(prefFncXNewI, prefFncY, aggrFnc)
        upModels.append(upModelNewI)

    return upModels

def __neighboursOfPrefFncX(prefFncX, theWorstX):

    # lineSegmentsX:LineSegments
    lineSegmentsX = prefFncX.lineSegments.clone()

    # points:list<point>
    points = lineSegmentsX.exportPoints()
    # point:Point
    point = Points(points).exportNearstPointX(theWorstX)

    #print("theWorstX: " + str(theWorstX))

    #if abs(point.x - theWorstX) < 0.1:
    if random.uniform(0, 1) < 0.5:
      # lineSegmentsNew:LineSegments
      lineSegmentsNew = __moveWithPoint(lineSegmentsX, theWorstX)
    else:
      # lineSegmentsNew:LineSegments
      lineSegmentsNew = __cutSegmentInTheMiddle(lineSegmentsX, theWorstX)
      #lineSegmentsNew = __cutSegmentInTheWorstX(lineSegmentsX, theWorstX)

    # prefFncXNew:PrefFncX
    prefFncXNew = PrefFncX.createFromLineSegments(lineSegmentsNew.lineSegments)

    return prefFncXNew

# lineSegmentsX:LineSegments, theWorstX:float
def __cutSegmentInTheMiddle(lineSegmentsX, theWorstX):
    #print("__cutSegmentInTheMiddle")

    # lineSegmentDontIntersect:list<LineSegment>
    lineSegmentIntersect = lineSegmentsX.lineSegmentsWhichIntersectAxisParallelToY(theWorstX)
    lineSegmentDontIntersect = lineSegmentsX.lineSegmentsWhichDontIntersectAxisParallelToY(theWorstX)

    # midpoint:Point
    midpoint = lineSegmentIntersect.midpoint()
    # functionValueMidpoint:float
    functionValueMidpoint = lineSegmentIntersect.intersectionWithTheAxisParallelToY(midpoint.x)
    # fncValue:float
    fncValue = functionValueMidpoint + 0.1 * random.uniform(-1, 1)
    if fncValue < 0.0:
        fncValue = 0.0
    if fncValue > 1.0:
        fncValue = 1.0

    #print("functionValueMidpoint: " + str(functionValueMidpoint))
    #print("functionValueNew       : " + str(fncValue))

    # lineSegmentsNew:list<LineSegment>
    lineSegmentsNew = list(lineSegmentDontIntersect)
    lineSegmentsNew.append(LineSegment(lineSegmentIntersect.point1, Point(midpoint.x, fncValue)))
    lineSegmentsNew.append(LineSegment(Point(midpoint.x, fncValue), lineSegmentIntersect.point2))

    return LineSegments(lineSegmentsNew)


# lineSegmentsX:LineSegments, theWorstX:float
def __cutSegmentInTheWorstX(lineSegmentsX, theWorstX):
    #print("__cutSegmentInTheWorstX")

    # lineSegmentDontIntersect:list<LineSegment>
    lineSegmentIntersect = lineSegmentsX.lineSegmentsWhichIntersectAxisParallelToY(theWorstX)
    lineSegmentDontIntersect = lineSegmentsX.lineSegmentsWhichDontIntersectAxisParallelToY(theWorstX)

    # fncValue:float
    fncValue = random.uniform(0, 1)

    # lineSegmentsNew:list<LineSegment>
    lineSegmentsNew = list(lineSegmentDontIntersect)
    lineSegmentsNew.append(LineSegment(lineSegmentIntersect.point1, Point(theWorstX, fncValue)))
    lineSegmentsNew.append(LineSegment(Point(theWorstX, fncValue), lineSegmentIntersect.point2))

    return LineSegments(lineSegmentsNew)


# lineSegmentsX:LineSegments, theWorstX:float
def __moveWithPoint(lineSegmentsX, theWorstX):
    #print("__moveWithPoint")
    #print("theWorstX: " + str(theWorstX))

    # points:Points
    points = Points(lineSegmentsX.exportPoints())
    # point:Point
    point = points.exportNearstPointX(theWorstX)
    if point == points.points[0]:
        point = points.points[1]
    if point == points.points[points.size()-1]:
        point = points.points[points.size()-2]

    # point1:Point
    point1 = [lineSegmentI.point1 for lineSegmentI in lineSegmentsX.lineSegments if lineSegmentI.point2 == point]
    # point2:Point
    point2 = [lineSegmentI.point2 for lineSegmentI in lineSegmentsX.lineSegments if lineSegmentI.point1 == point]
    if len(point1) == 0 or len(point2) == 0:
        print("chyba")
        return lineSegmentsX
    point1 = point1[0]
    point2 = point2[0]

    # sizeInterval:float
    sizeInterval = abs(point1.x - point2.x)

    # valX:float
    valX = min(point1.x, point2.x) + sizeInterval * random.uniform(0, 1)
    print("Move: " + str(theWorstX) + " -> " + str(valX))

    # pointNew:Point
    pointNew = Point(valX, point.y)
    #pointNew.printPoint()

    # lineSegmentsXNew:LineSegments
    lineSegmentsXNew = lineSegmentsX.clone()
    lineSegmentsXNew.replacePointByPoint(point, pointNew)
    #lineSegmentsXNew.printLineSegments()

    return lineSegmentsXNew