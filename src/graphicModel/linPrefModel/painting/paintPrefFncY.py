from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen


class PaintPrefFncY:
    #c:CanvasDimensions
    def __init__(self, c):
      self.c = c

    # prefFncY:CanvasModelOfPrefFncY
    def paint(self, qp, cmPrefFncY):
        #print(cmPrefFncY.prefFncY.toString())
        qp.setPen(QPen(cmPrefFncY.color, 2, Qt.SolidLine))

        #prefFncY:PrefFncY
        prefFncY = cmPrefFncY.prefFncY

        # lineSegmentI:LineSegment
        for lineSegmentI in prefFncY.lineSegments.lineSegments:
          point1 = lineSegmentI.point1
          point2 = lineSegmentI.point2
          x1, y1 = self.c.coorPrefFncY(point1.x, point1.y)
          x2, y2 = self.c.coorPrefFncY(point2.x, point2.y)
          qp.drawLine(x1, y1, x2, y2)