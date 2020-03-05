#!/usr/bin/python3

from geometry.point import Point #class
from geometry.pointWithID import PointWithID #class
from geometry.lineSegment import LineSegment

class PointsWithRating:
    def __init__(self, pointsWithRating):
        self.pointsWithRating = pointsWithRating

    # pointsWithRating:list<PointWithRating>
    def twoFurthestPoints(pointsWithRating):

        rDistance = 0
        rPoint1 = None
        rPoint2 = None

        for i in range(len(pointsWithRating)):
            for j in range(len(pointsWithRating)):
                pI = pointsWithRating[i]
                pJ = pointsWithRating[j]
                if i == j:
                    break
                distanceIJ = pI.point.distance(pJ.point)
                #print(distanceIJ)
                if distanceIJ > rDistance:
                    rDistance = distanceIJ
                    rPoint1 = pI
                    rPoint2 = pJ
        #print("Distance Result: " + str(rPoint1.point.distance(rPoint2.point)))
        return (rPoint1, rPoint2)


    # pointsWithRating:list<PointWithRating>
    def pointWithTheHighestError(self, ratingPredicted):

        if self.pointsWithRating == None or len(self.pointsWithRating) == 0:
           return None

        diff = 0
        pWithRating = self.pointsWithRating[0]

        for i in range(len(self.pointsWithRating)):
            # pWithRatingI:PointWithRating
            pWithRatingI = self.pointsWithRating[i]
            # diffI:float
            diffI = abs(pWithRatingI.rating - ratingPredicted[i])
            if diffI > diff:
                diff = diffI
                pWithRating = pWithRatingI
        # pWithRating:PointWithRating
        return pWithRating