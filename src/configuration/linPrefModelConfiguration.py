#!/usr/bin/python3

class LinPrefModelConfiguration:

   def __init__(self):
      self.SIZE_X_DATA_CUBE = 1.0;
      self.SIZE_Y_DATA_CUBE = 1.0;

      self.SIZE_X_PREF_CUBE = 1.0;
      self.SIZE_Y_PREF_CUBE = 1.0;

      self.compute();

   def __init__(self, xSizeDataCube, ySizeDataCube, xSizePrefCube, ySizePrefCube):
      self.SIZE_X_DATA_CUBE = xSizeDataCube;
      self.SIZE_Y_DATA_CUBE = ySizeDataCube;

      self.SIZE_X_PREF_CUBE = xSizePrefCube;
      self.SIZE_Y_PREF_CUBE = ySizePrefCube;

      self.compute();


   def compute(self):
      self.AXIS_X_BEGIN_DATA_CUBE = 0.0;
      self.AXIS_X_END_DATA_CUBE = self.AXIS_X_BEGIN_DATA_CUBE + self.SIZE_X_DATA_CUBE;

      self.AXIS_Y_BEGIN_DATA_CUBE = 0.0;
      self.AXIS_Y_END_DATA_CUBE = self.AXIS_Y_BEGIN_DATA_CUBE + self.SIZE_Y_DATA_CUBE;


      self.AXIS_X_BEGIN_PREF_CUBE = 0.0;
      self.AXIS_X_END_PREF_CUBE = self.AXIS_X_BEGIN_PREF_CUBE + self.SIZE_X_PREF_CUBE;

      self.AXIS_Y_BEGIN_PREF_CUBE = 0.0;
      self.AXIS_Y_END_PREF_CUBE = self.AXIS_Y_BEGIN_PREF_CUBE + self.SIZE_Y_PREF_CUBE;
