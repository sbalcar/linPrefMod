#!/usr/bin/python3

from matplotlib.backends.qt_compat import is_pyqt5
if is_pyqt5():
    pass
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


from gui.frame.modelTypes import ModelTypes #class


# user2D:User2D, linPrefModelConf:LinPrefModelConfiguration, modelType:ModelTypes
def getUserProfileModel(user2D, linPrefModelConf, modelType):

  # userProfileModel:
  userProfileModel = None;
  if modelType == ModelTypes.TRIANGULAR:
     userProfileModel = user2D.exportUserProfileModel(linPrefModelConf);
  if modelType == ModelTypes.REFRACTED:
     userProfileModel = user2D.exportUserProfileRefractedModel(linPrefModelConf);
  if modelType == ModelTypes.TROUGH:
     userProfileModel = user2D.exportUserProfileNewModel(linPrefModelConf);

  return userProfileModel;

