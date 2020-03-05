#!/usr/bin/python3

from matplotlib.backends.qt_compat import is_pyqt5
if is_pyqt5():
    pass
else:
    pass
from matplotlib.figure import Figure

from graphicModel.linPrefModel.painting_old import Painting #class

from geometry.pointWithRating import PointWithRating #class


# user:UserProfileModel, aggrLevel:Float, pointsDataCube:Point[], labels:String[], ratings:List<float>, linPrefModelConf:LinPrefModelConfiguration
def visualisationOfContourLinesOneUser(userProfileModel, aggrLevel, pointsDataCube, labels, ratings, linPrefModelConf):
  
  if userProfileModel == None:
      return Figure()

  #title:String
  title = 'Lin. pref. model';

  #painting:Painting
  painting = Painting(linPrefModelConf, title)
  painting.paintOnlyModel(userProfileModel, aggrLevel, 'g')
  painting.paintPoints(pointsDataCube, [], labelsDataCube=[], labelsPrefCube=[], color="b", size=1)

  # pointsWithRating:List<PointWithRating>
  pointsWithRating = [PointWithRating(tupleI[0], float(tupleI[1])) for tupleI in zip(pointsDataCube, ratings)]
  painting.paintPointsInPrefFncCubes(pointsWithRating, color="g", size=1)

  return painting.graphicalModel.fig1;

