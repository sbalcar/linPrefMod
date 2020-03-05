#!/usr/bin/python3

from userProfileModel.model.prefFnc.prefFncs import PrefFncX
from userProfileModel.model.prefFnc.prefFncs import PrefFncY
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class

from geometry.lineSegment import LineSegment #class

from morphism.morphism import getMorphismOfPrefCubePointToDataCubePoint #function

from generator import *


class AlgorithmContourLine:

    # prefFncX:PrefFncX, prefFncY:PrefFncY, aggregation:AggrFnc, aggrLevel:float, linPrefModelConf:LinPrefModelConfiguration
    def getMorphismOfAggregationFncToDataCubeLines(prefFncX, prefFncY, aggrFnc, aggrLevel, linPrefModelConf):
        # aggrLineSegment:LineSegment
        aggrLineSegment = aggrFnc.exportAsLineSegment(Point(aggrLevel, aggrLevel), linPrefModelConf);

        # intervalsX:LineSegments
        intervalsX = prefFncX.exportIntervals()
        # intervalsY:LineSegments
        intervalsY = prefFncY.exportIntervals()

        # aggrFncPoints:Point[]
        aggrFncPoints = aggrFnc.exportAsLineSegment(Point(aggrLevel, aggrLevel), linPrefModelConf);
        # aggregation:LineSegment
        aggrFnc = LineSegment(aggrLineSegment.point1, aggrLineSegment.point2);

        # polygonLineSegments:LineSegment[]
        polygonLineSegments = [];
        for intervalXI in intervalsX.lineSegments:
            for intervalYI in intervalsY.lineSegments:
                minX = intervalYI.getMinX();
                maxX = intervalYI.getMaxX();

                minY = intervalXI.getMinY();
                maxY = intervalXI.getMaxY();

                # aggrFncII:LineSegment
                aggrFncII = aggrFnc.deleteFromMinusInfinityToX(minX);
                if aggrFncII == None:
                    # print("MinusInfinityToX")
                    continue;
                aggrFncII = aggrFncII.deleteFromXToPlusInfinity(maxX);
                if aggrFncII == None:
                    # print("FromXToPlusInfinity")
                    continue;

                aggrFncII = aggrFncII.deleteFromMinusInfinityToY(minY);
                if aggrFncII == None:
                    # print("MinusInfinityToY")
                    continue;
                aggrFncII = aggrFncII.deleteFromYToPlusInfinity(maxY);
                if aggrFncII == None:
                    # print("FromYToPlusInfinity")
                    continue;

                point1 = aggrFncII.point1;
                point2 = aggrFncII.point2;

                # print("point1.y=" + str(point1.y))
                # intervalXI.printLineSegment();

                x1 = intervalXI.intersectionWithTheAxisParallelToX(point1.y)
                y1 = intervalYI.intersectionWithTheAxisParallelToY(point1.x)

                x2 = intervalXI.intersectionWithTheAxisParallelToX(point2.y)
                y2 = intervalYI.intersectionWithTheAxisParallelToY(point2.x)

                # print("x1=" + str(x1) + " y1=" + str(y1))
                # print("x2=" + str(x2) + " y2=" + str(y2))

                if x1 == None or y1 == None or x2 == None or y2 == None:
                    continue;

                if intervalXI.isParalelToX():
                    lineA = intervalXI.exportLineParalelToX(y2)
                    polygonLineSegments.append(lineA);
                    continue;

                if intervalYI.isParalelToY():
                    lineA = intervalYI.exportLineParalelToY(x2)
                    polygonLineSegments.append(lineA);
                    continue;

                pLineSegmentI = LineSegment(Point(x1, y1), Point(x2, y2));
                polygonLineSegments.append(pLineSegmentI);

        # print("polygonLineSegments: ", len(polygonLineSegments))

        # polygonLineSegments:LineSegment[]
        return polygonLineSegments;



    # polygonLineSegments:LineSegment[]
    def sortDataCubePolygon(polygonLineSegments):

      #for polygonLineSegmentI in polygonLineSegments:
      #    polygonLineSegmentI.printLineSegment();

      # polygon:Point[]
      polygon = []
      if len(polygonLineSegments) > 0:
          polygon.append(polygonLineSegments[0].point1)

      #while len(polygon) < numberOfVerticesOfPolygon:
      for insertI in range(len(polygonLineSegments)):
          #print("len(polygon): ", len(polygon))
          lastPointOfPolygonI = polygon[len(polygon) -1]
          for polygonLineSegmentI in polygonLineSegments:
              if polygonLineSegmentI.point1 == lastPointOfPolygonI:
                  polygon.append(polygonLineSegmentI.point2);
                  polygonLineSegments.remove(polygonLineSegmentI);
                  break;
              if polygonLineSegmentI.point2 == lastPointOfPolygonI:
                  polygon.append(polygonLineSegmentI.point1);
                  polygonLineSegments.remove(polygonLineSegmentI);
                  break;

      if len(polygon) < len(polygonLineSegments):
          return [];

      # polygon:Point[]
      return polygon;

