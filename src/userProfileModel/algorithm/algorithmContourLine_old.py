
class AlgorithmContourLine_old:

 # aggrLevel:float, modelConf:ModelConfiguration
  def getMorphismOfAggregationFncToDataCubeLines(self, aggrLevel, modelConf):
    print("getMorphismOfAggregationFncToDataCubeLines")
#    aggrFncPoints = self.aggregation.exportAsLineSegment(Point(aggrLevel, aggrLevel), modelConf);
#    print("aggrFncPoints: ", len(aggrFncPoints))
#
#    aggrFncPint1 = aggrFncPoints[0];
#    aggrFncPint2 = aggrFncPoints[1];
#
#    # intersectionsOfFncXAndPrefPoint1:float[]
#    intersectionsOfFncXAndPrefPoint1 = self.prefFncX.inverseValue(aggrFncPint1.y)
#    print("intersectionsOfFncXAndPrefPoint1: ", len(intersectionsOfFncXAndPrefPoint1))
#    # intersectionsOfFncYAndPrefPoint1:float[]
#    intersectionsOfFncYAndPrefPoint1 = self.prefFncY.inverseValue(aggrFncPint1.x)
#    print("intersectionsOfFncYAndPrefPoint1: ", len(intersectionsOfFncYAndPrefPoint1))
#
#    for pI in intersectionsOfFncXAndPrefPoint1:
#        print(pI)
#
#    # intersectionsOfFncXAndPrefPoint2:float[]
#    intersectionsOfFncXAndPrefPoint2 = self.prefFncX.inverseValue(aggrFncPint2.y)
#    print("intersectionsOfFncXAndPrefPoint2: ", len(intersectionsOfFncXAndPrefPoint2))
#    # intersectionsOfFncYAndPrefPoint2:float[]
#    intersectionsOfFncYAndPrefPoint2 = self.prefFncY.inverseValue(aggrFncPint2.x)
#    print("intersectionsOfFncYAndPrefPoint2: ", len(intersectionsOfFncYAndPrefPoint2))
#
#    # polygonLineSegments:LineSegment[]
#    polygonLineSegments = []
#    for indexOfFncXInterval in range(self.prefFncX.numberOfIntervals()):
#        for indexOfFncYInterval in range(self.prefFncY.numberOfIntervals()):
#            # point1OfFncX:Point
#            point1OfFncX = intersectionsOfFncXAndPrefPoint1[indexOfFncXInterval]
#            point1OfFncY = intersectionsOfFncYAndPrefPoint1[indexOfFncYInterval]
#
#            point2OfFncX = intersectionsOfFncXAndPrefPoint2[indexOfFncXInterval]
#            point2OfFncY = intersectionsOfFncYAndPrefPoint2[indexOfFncYInterval]
#
#            if point1OfFncX == None or point1OfFncY == None:
#                continue;
#            if point2OfFncX == None or point2OfFncY == None:
#                continue;
#
#            #dataPoint1 = Point(point1OfFncX.x, point1OfFncY.y);
#            #dataPoint2 = Point(point2OfFncX.x, point2OfFncY.y);
#
#            dataPoint1 = Point(point1OfFncX, point1OfFncY);
#            dataPoint2 = Point(point2OfFncX, point2OfFncY);
#
#            lineSegmentI = LineSegment(dataPoint1, dataPoint2);
#            polygonLineSegments.append(lineSegmentI);
#
#    print("polygonLineSegments: ", len(polygonLineSegments))
#    for p in polygonLineSegments:
#        p.printLineSegment();
#
#    # polygonLineSegments:LineSegment[]
#    return polygonLineSegments;
