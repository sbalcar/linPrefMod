#!/usr/bin/python3

from geometry.point import Point #class
from geometry.pointWithID import PointWithID #class
from geometry.lineSegment import LineSegment

class PointsWithID:
    # pointsWithID:list<PointsWithID>
    def __init__(self, pointsWithID):
        if type(pointsWithID) is not list:
            raise ValueError("Argument pointsWithID isn't type list.")
        for pointI in pointsWithID:
            if type(pointI) is not PointWithID:
                raise ValueError("Argument pointsWithID don't contain PointsWithID.")
        self.pointsWithID = pointsWithID

    def exportPoint(self, pointID):
        pointsWithIdSelected = [p for p in self.pointsWithID if p.pointID is pointID]
        if len(pointsWithIdSelected) == 0:
            return None
        return pointsWithIdSelected[0]

    # point:Point
    def exportTheNearest(self, point, diameter):
        # pointIDsAndDistances:list<(float, float)>
        pointIDsAndDistances = [(pointWithIdI.pointID, LineSegment(pointWithIdI.point, point).size()) for pointWithIdI in self.pointsWithID]

        # pointIDsAndDistances:list<(float, float)>
        sortedPointIDsAndDistances = sorted(pointIDsAndDistances, key = lambda x: x[1])

        # pointIDAndDistance
        pointIDAndDistance = sortedPointIDsAndDistances[0]

        # pointID:float
        pointID = pointIDAndDistance[0]
        # distance:float
        distance = pointIDAndDistance[1]

        if distance < diameter:
            return pointID
        return None