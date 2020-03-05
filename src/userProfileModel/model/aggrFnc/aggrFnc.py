import numpy
import random

from generator import Pair
from geometry.geometry import getIntersection, getSizeOfLine
from geometry.line import Line
from geometry.lineSegment import LineSegment
from geometry.point import Point
from morphism.morphism import getMorphismToPrefCube


class AggrFnc:
  # weights:float[]
  def __init__(self, weights):
     if type(weights) is not list:
        raise ValueError("Argument weights isn't type list.")
     for weightI in weights:
       if type(weightI) is not float:
          raise ValueError("Argument weights don't contain float.")
     self.weights = weights;

  @staticmethod
  def generate():
      iw = random.uniform(0, 1)
      return AggrFnc([iw, 1-iw])

  def toString(self):
     return str(self.weights)

  # pointsInPrefCube:list<PointWithID>, linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointsWitIDInPC(self, pointsInPrefCube, linPrefModelConf):
     # pointsInPC:list<Point>
     pointsInPC = [p.point for p in pointsInPrefCube]
     return self.preferenceOfPointsInPC(pointsInPC, linPrefModelConf)

  # pointsInPC:Point[], linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointsInPC(self, pointsInPC, linPrefModelConf):
     preferences = []
     for pointInPCI in pointsInPC:
         preferenceI = self.preferenceOfPointInPC(pointInPCI, linPrefModelConf);
         preferences.append(preferenceI)
     # preferences:float[]
     return preferences;

  # prefPoint:Point. linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointInPC(self, prefPoint, linPrefModelConf):
     if (len(self.weights) != prefPoint.dimension()):
         print("Error")

     pref = 0
     for i in range(len(self.weights)):
       pref += self.weights[i] * prefPoint.exportValues()[i]

     return round(pref, 3)

  # point:Point
  def exportAsLine(self, point):
     line = Line()
     line.constructor2(self.weights[0], self.weights[1], point);
     #line.constructor2(self.weights[1], self.weights[0], point);
     return line;

  # point:Point, linPrefModelConf:LinPrefModelConfiguration
  def exportAsLineSegment(self, point, linPrefModelConf):
     aggrLine = self.exportAsLine(point);

     point1 = Point(linPrefModelConf.AXIS_X_BEGIN_PREF_CUBE,
             aggrLine.getFunctionValue(linPrefModelConf.AXIS_X_BEGIN_PREF_CUBE));
     point2 = Point(linPrefModelConf.AXIS_X_END_PREF_CUBE,
             aggrLine.getFunctionValue(linPrefModelConf.AXIS_X_END_PREF_CUBE));
     point3 = Point(aggrLine.getDomainValue(linPrefModelConf.AXIS_Y_BEGIN_PREF_CUBE),
             linPrefModelConf.AXIS_Y_BEGIN_PREF_CUBE);
     point4 = Point(aggrLine.getDomainValue(linPrefModelConf.AXIS_Y_END_PREF_CUBE),
             linPrefModelConf.AXIS_Y_END_PREF_CUBE);

     pointsOnAxes = getMorphismToPrefCube([point1, point2, point3, point4],
             linPrefModelConf.AXIS_X_BEGIN_PREF_CUBE, linPrefModelConf.AXIS_Y_BEGIN_PREF_CUBE,
             linPrefModelConf.AXIS_X_END_PREF_CUBE, linPrefModelConf.AXIS_Y_END_PREF_CUBE);

     # LineSegment
     return LineSegment(pointsOnAxes[0], pointsOnAxes[1])


  # pointPrefCube:Point[], linPrefModelConf:LinPrefModelConfiguration
  def preferenceOfPointInPrefCube_(self, pointPrefCube, linPrefModelConf):
     # aggrLine:Point[]
     aggrLinePoints = self.getAggregationFunction(linPrefModelConf);

     diagBeginPoint = Point(linPrefModelConf.AXIS_X_BEGIN_PREF_CUBE, linPrefModelConf.AXIS_Y_BEGIN_PREF_CUBE);
     diagEndPoint = Point(linPrefModelConf.AXIS_X_END_PREF_CUBE, linPrefModelConf.AXIS_Y_END_PREF_CUBE);

     # intersection:Point
     intersection = getIntersection(Pair(aggrLinePoints[0], aggrLinePoints[1]), Pair(diagBeginPoint, diagEndPoint))
     # distanceFromBeginning:float
     distanceFromBeginning = getSizeOfLine(Pair(intersection, diagBeginPoint))
     # sizeOfDiagonal:float
     sizeOfDiagonal = getSizeOfLine(Pair(diagBeginPoint, diagEndPoint))

     preference = distanceFromBeginning / sizeOfDiagonal
     #print("sizeOfDiagonal: ", sizeOfDiagonal)

     if np.isinf(preference):
        return 1.0
     # preference:float
     return preference