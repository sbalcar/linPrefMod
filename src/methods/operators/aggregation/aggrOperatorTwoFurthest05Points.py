#!/usr/bin/python3

from methods.aMethod import AMethod #class

from methods.individual.individualEvaluated import IndividualEvaluated #class

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

class AggrOperatorTwoFurthest05Points:

    # pointsWithRatingDC:list<PointWithRating>, linPrefModelConf:LinPrefModelConfiguration
    def run(prefFncX, prefFncY, pointsWithRatingDC, linPrefModelConf):

        # selectedPointsWithRatingDC:list<PointWithRating>
        selectedPointsWithRatingDC = [pI for pI in pointsWithRatingDC if 0.45 < pI.rating and pI.rating < 0.55]

        # selectedPointsPC:list<Point>
        selectedPointsPC = [Point(prefFncX.functionalValue(p.point.x), prefFncY.functionalValue(p.point.y))
                                    for p in selectedPointsWithRatingDC]

        # selectedPointsWithOrigRatingPC:list<PointWithRating>
        selectedPointsWithOrigRatingPC = [PointWithRating(selectedPointsPC[i], selectedPointsWithRatingDC[i].rating)
                                      for i in range(len(selectedPointsWithRatingDC))]

        # (p1:PointWithRating, p2:PointWithRating)
        p1, p2 = PointsWithRating.twoFurthestPoints(selectedPointsWithOrigRatingPC)

        #p1.printPointWithRating()
        #p2.printPointWithRating()

        # xd:float
        xd = abs(p1.point.x - p2.point.x)
        # yd:float
        yd = abs(p1.point.y - p2.point.y)

        #print("xd: " + str(xd))
        #print("yd: " + str(yd))

        # wx:float
        wx = xd / (xd + yd)

        return wx
