from geometry.point import Point

class Points:
  # points:Point[]
  def __init__(self, points):
      if type(points) is not list:
          raise ValueError("Argument points isn't type list.")
      for pointI in points:
          if type(pointI) is not Point:
              raise ValueError("Argument points don't contain Point.")
      self.points = points

  def exportAsPair(self):
      pointsX = [self.points[i].x for i in range(0, len(self.points))]
      pointsY = [self.points[i].y for i in range(0, len(self.points))]
      # (double[], double[])
      return (pointsX, pointsY)

  def exportAsString(self):
      string = ""
      for p in self.points:
          string = string + "(" + str(p.x) + "," + str(p.y) + "), "
      return string[:-2]

  # sting:str
  def importAsString(sting):
      pairsOfValues = [x.strip()[1:] for x in str(sting + ",").split("),")]

      try:
        points = []
        for pvJ in pairsOfValues[:-1]:
            pointJ = Point.create([float(vI) for vI in pvJ.split(",")])
            points.append(pointJ)

        return Points(points)
      except:
        return None

  def exportNearstPointX(self, coordinateX):
      dinstance = 100
      point =  self.points[0]
      for pointI in self.points:
          distanceI = abs(pointI.x -coordinateX)
          if distanceI < dinstance:
              dinstance = distanceI
              point = pointI
      return point

  def size(self):
      return len(self.points)