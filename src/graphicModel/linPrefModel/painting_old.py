#!/usr/bin/python3

#from graphicModel.linPrefModel.graphicalModel import GraphicalModel #class

from geometry.point import Point #class


class Painting:
  # modelConf:LinPrefModelConfiguration, title:str
  def __init__(self, modelConf, title):
    # modelConf:LinPrefModelConfiguration
    self.modelConf = modelConf;
    #graphicalModel:GraphicalModel
    self.graphicalModel = GraphicalModel(modelConf)
    self.graphicalModel.initFigure(title);


  # upModel:UserProfileModel, pointsDataCube:Point[], gModelConf:LinPrefModelConfiguration
  def paintModel(self, upModel, pointsDataCube, color="b"):

    for pointDataCubeI in pointsDataCube:
      self.graphicalModel.paintDataCubePoint(pointDataCubeI);
      self.graphicalModel.paintDataCubeAuxiliaryLines(pointDataCubeI)

      #pointPrefCubeI:Point
      pointPrefCubeI = upModel.pointDataCubeToPointPrefCube(pointDataCubeI);
      self.graphicalModel.paintPrefCubePoints([pointPrefCubeI])
      self.graphicalModel.paintPrefCubeAuxiliaryLines(pointPrefCubeI)

      #pointPrefCubeY:Point
      pointPrefCubeX = upModel.pointDataCubeToPointPrefFncX(pointDataCubeI);
      self.graphicalModel.paintPrefFncXAuxiliaryLines(pointPrefCubeX)

      #pointPrefCubeY:Point
      pointPrefCubeY = upModel.pointDataCubeToPointPrefFncY(pointDataCubeI);
      self.graphicalModel.paintPrefFncYAuxiliaryLines(pointPrefCubeY)

      #aggrLineI:Point[]
      aggrLineI = upModel.aggregationFncLine(pointPrefCubeI, self.modelConf)
      self.graphicalModel.paintPrefCubeAggregationFnc(aggrLineI[0], aggrLineI[1])

    self.graphicalModel.paintPrefCubeDiagonal();
    self.graphicalModel.paintPrefCubeDiagonal();

    self.graphicalModel.paintPrefFncX(upModel.prefFncX, color);
    self.graphicalModel.paintPrefFncY(upModel.prefFncY, color);

  # upModel:UserProfileModel, pointsDataCube:Point[], pointsPrefCube:Point[]
  def paintModelOnlyPoints(self, upModel, pointsDataCube, pointsPrefCube, color="b", size=1):

    self.graphicalModel.paintDataCubePoints(pointsDataCube, color="y", size=size);
    self.graphicalModel.paintPrefCubePoints(pointsPrefCube, color=color, size=size);

    self.graphicalModel.paintPrefCubeDiagonal();

    self.graphicalModel.paintPrefFncX(upModel.prefFncX, color);
    self.graphicalModel.paintPrefFncY(upModel.prefFncY, color);

  # upModel:UserProfileModel, aggrLevel:float
  def paintOnlyModel(self, upModel, aggrLevel, color="b"):

    #aggrFncPoints:Point[]
    aggrFncPoints = upModel.aggrFnc.exportAsLineSegment(Point(aggrLevel,aggrLevel), self.modelConf);
    self.graphicalModel.paintPrefCubeAggregationFnc(aggrFncPoints[0], aggrFncPoints[1], color=color)

    contorLines = upModel.getMorphismOfAggregationFncToDataCubeLines(aggrLevel, self.modelConf)
    self.graphicalModel.paintDataCubeContorLines(contorLines, color=color);

    self.graphicalModel.paintPrefFncX(upModel.prefFncX, color);
    self.graphicalModel.paintPrefFncY(upModel.prefFncY, color);

  # pointsDataCube:Point[], pointsPrefCube:Point[]
  def paintPoints(self, pointsDataCube, pointsPrefCube, labelsDataCube=[], labelsPrefCube=[], color="b", size=1):
    
    self.graphicalModel.paintDataCubePoints(pointsDataCube, labelsDataCube, color=color, size=size);
    self.graphicalModel.paintPrefCubePoints(pointsPrefCube, labelsPrefCube, color=color, size=size);

  # pointsWithRating:PointWithRating[]
  def paintPointsInPrefFncCubes(self, pointsWithRating, color="b", size=1):

    # pointsPrefX:Point[]
    points = [pI.point for pI in pointsWithRating]
    pointsPrefX = [Point(pI.point.x, pI.rating) for pI in pointsWithRating]
    pointsPrefY = [Point(pI.rating, pI.point.y) for pI in pointsWithRating]

    self.graphicalModel.paintDataCubePoints(points, labels=[], color=color, size=size);
    self.graphicalModel.paintpPrefCubeXPoints(pointsPrefX, labels=[], color=color, marker='o', size=size);
    self.graphicalModel.paintpPrefCubeYPoints(pointsPrefY, labels=[], color=color, marker='o', size=size);

  # id:int
  def save(self, id, testID=""):
    self.graphicalModel.save(id, testID=testID);

  # id:int
  def paint(self, id):
    self.graphicalModel.paint(id);

  def close(self):
    self.graphicalModel.close();

