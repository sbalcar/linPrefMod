from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen


class PaintPrefFncX:
    #c:CanvasDimensions
    def __init__(self, c):
      self.c = c

    #cmPrefFncX:CanvasModelOfPrefFncX
    def paint(self, qp, cmPrefFncX):
        #print(cmPrefFncX.prefFncX.toString())

        qp.setPen(QPen(cmPrefFncX.color, 2, Qt.SolidLine))

        #prefFncX:PrefFncX
        prefFncX = cmPrefFncX.prefFncX

        # lineSegmentI:LineSegment
        for lineSegmentI in prefFncX.lineSegments.lineSegments:
          point1 = lineSegmentI.point1
          point2 = lineSegmentI.point2
          x1, y1 = self.c.coorPrefFncX(point1.x, point1.y)
          x2, y2 = self.c.coorPrefFncX(point2.x, point2.y)
          qp.drawLine(x1, y1, x2, y2)