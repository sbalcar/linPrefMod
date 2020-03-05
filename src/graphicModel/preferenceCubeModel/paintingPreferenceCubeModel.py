#!/usr/bin/python3

#from graphic.morphism import getMorphismOfPrefCubePointToPreferenceCubePoint #function

from graphicModel.preferenceCubeModel.graphicalPreferenceCubeModel import GraphicalPreferenceCubeModel #class


class PaintingPreferenceCubeModel:
  def __init__(self, linPrefModelConf, title):
     self._linPrefModelConf = linPrefModelConf;

     #_graphicalModel:GraphicalPreferenceCubeModel
     self.graphicalModel = GraphicalPreferenceCubeModel(linPrefModelConf)
     self.graphicalModel.initFigure(title);

  #points:Points[], pointsWithIDs:PointWithID[]
  def paintPreferenceCube(self, pointsWithIDs):
     
     #points:Point[]
     points = [pointWithID.point for pointWithID in pointsWithIDs]

     #labels:Point[]
     labels = [pointWithID.pointID for pointWithID in pointsWithIDs]

     self.graphicalModel.paintPrefCubePoints(points, labels=labels, marker="o", color="y")
     self.graphicalModel.paintPrefCubeDiagonal(color="y", linewidth=0.8);

     #self.graphicalModel.paintPrefCubePoints([Point(0.5, 0.0),Point(0.7, 0.0)], labels=["A", "B"], marker='o', color="r")
     #self.graphicalModel.paintPrefCubePoints([Point(0.0, 0.5),Point(0.0, 0.7)], labels=["C", "D"], marker='o', color="r")


  # linPrefModelConf:LinPrefModelConf, aggregation:AggrFnc, point:Point
  def paintAggregationFnc(self, linPrefModelConf, aggrFnc, point, color="r", linewidth=1.0):

     # pointsOnAxes:LineSegment
     pointsOnAxes = aggrFnc.exportAsLineSegment(point, linPrefModelConf);

     self.graphicalModel.paintPrefCubeAggregationFnc(pointsOnAxes.point1, pointsOnAxes.point2, color=color, linewidth=linewidth)


  # linPrefModelConf:LinPrefModelConf, thresholds:Threshold[]
  def paintThreshold(self, linPrefModelConf, thresholds, color="r", linewidth=1.0):
     for thresholdI in thresholds:
        self.paintAggregationFnc(linPrefModelConf, thresholdI.aggrFnc, thresholdI.point, color=color, linewidth=linewidth)
        self.graphicalModel.perpendicularsToPoint(thresholdI.point);

  # id:int
  def save(self, id):
    self.graphicalModel.save(id);

  # id:int
  def paint(self, id):
    self.graphicalModel.paint(id);

  def close(self):
    self.graphicalModel.close();

