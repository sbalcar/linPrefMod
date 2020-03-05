from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPen, QBrush


class PaintLinPrefModelSkelet:
    # c:CanvasDimensions, title:str
    def __init__(self, c, title):
      self.c = c

    def paint(self, qp):

        qp.setFont(QFont("Arial", 8));
        qp.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        self.createPreferenceCube(qp, self.c)
        self.createDataCube(qp, self.c)
        self.createPrefFncXCube(qp, self.c)
        self.createPrefFncYCube(qp, self.c)

    def createPreferenceCube(self, qp, c):
        labels = c.getLegendOfPreferenceCube()

        prefCubeEndX = c.getPrefCubeEndX()
        prefCubeEndY = c.getPrefCubeEndY()
        prefCubeStartX = c.getPrefCubeStartX()
        prefCubeStartY = c.getPrefCubeStartY()

        # create preference cube
        self.__createRectangle(qp, prefCubeEndX, prefCubeEndY, prefCubeStartX, prefCubeStartY, c)

        # arrows to right, down
        self.__arrowToTheLeft(qp, prefCubeEndX, prefCubeEndY, c)
        self.__arrowToTheDown(qp, prefCubeEndX, prefCubeEndY, c)

        self.__createHorizontalLegend(qp, prefCubeStartX, prefCubeEndX, prefCubeEndY, labels, c, position="up")
        self.__createHorizontalLegend(qp, prefCubeStartX, prefCubeEndX, prefCubeStartY, [""]*len(labels), c, position="down")

        self.__createVerticalLegend(qp, prefCubeEndX, prefCubeStartY, prefCubeEndY, labels, c, position="left")
        self.__createVerticalLegend(qp, prefCubeStartX, prefCubeStartY, prefCubeEndY, [""]*len(labels), c, position="right")


    def createDataCube(self, qp, c):
        labels = c.getLegendOfDataCube()

        dataCubeStartX = c.getDataCubeStartX()
        dataCubeStartY = c.getDataCubeStartY()
        dataCubeEndX = c.getDataCubeEndX()
        dataCubeEndY = c.getDataCubeEndY()

        # create data cube
        self.__createRectangle(qp, dataCubeStartX, dataCubeStartY, dataCubeEndX, dataCubeEndY, c)

        # arrows to right, up
        self.__arrowToTheRight(qp, dataCubeEndX, dataCubeStartY, c)
        self.__arrowToTheUp(qp, dataCubeStartX, dataCubeEndY, c)

        self.__createHorizontalLegend(qp, dataCubeStartX, dataCubeEndX, dataCubeStartY, [""]*len(labels), c, position="up")
        self.__createHorizontalLegend(qp, dataCubeStartX, dataCubeEndX, dataCubeEndY, [""]*len(labels), c, position="down")

        self.__createVerticalLegend(qp, dataCubeStartX, dataCubeStartY, dataCubeEndY, [""]*len(labels), c, position="left")
        self.__createVerticalLegend(qp, dataCubeEndX, dataCubeStartY, dataCubeEndY, [""]*len(labels), c, position="right")


    def createPrefFncXCube(self, qp, c):
        labels = c.getLegendOfPrefFncXCube()

        prefFncXCubeStartX = c.getPrefFncXCubeStartX()
        prefFncXCubeStartY = c.getPrefFncXCubeStartY()
        prefFncXCubeEndX = c.getPrefFncXCubeEndX()
        prefFncXCubeEndY = c.getPrefFncXCubeEndY()

        # create pref fncX cube
        self.__createRectangle(qp, prefFncXCubeStartX, prefFncXCubeStartY, prefFncXCubeEndX, prefFncXCubeEndY, c)

        self.__arrowToTheRight(qp, prefFncXCubeEndX, prefFncXCubeEndY, c)

        self.__createHorizontalLegend(qp, prefFncXCubeStartX, prefFncXCubeEndX, prefFncXCubeEndY, labels, c, position="up")
        self.__createHorizontalLegend(qp, prefFncXCubeStartX, prefFncXCubeEndX, prefFncXCubeStartY, [""]*len(labels), c, position="down")

        self.__createVerticalLegend(qp, prefFncXCubeStartX, prefFncXCubeStartY, prefFncXCubeEndY, [""]*len(labels), c, position="left")
        self.__createVerticalLegend(qp, prefFncXCubeEndX, prefFncXCubeStartY, prefFncXCubeEndY, [""]*len(labels), c, position="right")


    def createPrefFncYCube(self, qp, c):
        labels = c.getLegendOfPrefFncYCube()

        prefFncYCubeStartX = c.getPrefFncYCubeStartX()
        prefFncYCubeStartY = c.getPrefFncYCubeStartY()
        prefFncYCubeEndX = c.getPrefFncYCubeEndX()
        prefFncYCubeEndY = c.getPrefFncYCubeEndY()

        # create pref fncY cube
        self.__createRectangle(qp, prefFncYCubeStartX, prefFncYCubeStartY, prefFncYCubeEndX, prefFncYCubeEndY, c)

        self.__arrowToTheUp(qp, prefFncYCubeEndX, prefFncYCubeEndY, c)

        self.__createHorizontalLegend(qp, prefFncYCubeStartX, prefFncYCubeEndX, prefFncYCubeEndY, [""]*len(labels), c, position="down")
        self.__createHorizontalLegend(qp, prefFncYCubeStartX, prefFncYCubeEndX, prefFncYCubeStartY, [""]*len(labels), c, position="up")

        self.__createVerticalLegend(qp, prefFncYCubeEndX, prefFncYCubeStartY, prefFncYCubeEndY, labels, c, position="left")
        self.__createVerticalLegend(qp, prefFncYCubeStartX, prefFncYCubeStartY, prefFncYCubeEndY, [""]*len(labels), c, position="right")


    def __createRectangle(self, qp, x1, y1, x2, y2, c):
        qp.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        qp.drawRect(min(x1,x2), max(y1,y2), abs(x1-x2), -abs(y1-y2))

        ## down line of data cube
        #qp.drawLine(x1, y1, x2, y1)
        ## left line of data cube
        #qp.drawLine(x1, y1, x1, y2)
        ## upper line of data cube
        #qp.drawLine(x1, y2, x2, y2)
        ## right line of data cube
        #qp.drawLine(x2, y1, x2, y2)

    # qp, x:int, y1:int, y2:int, labels:list<str>
    def __createVerticalLegend(self, qp, x, y1, y2, labels, c, position="right"):
        sizeOfInterval = (y2 - y1) / (len(labels) -1)
        for i in range(len(labels)):
           y = y1 + i * sizeOfInterval
           if position == "right":
              shiftOfLine = 5;
              shiftOfLabel = 25;
           if position == "left":
              shiftOfLine = -5;
              shiftOfLabel = -25;
           qp.drawLine(x, y, x +shiftOfLine, y)
           qp.drawText(x +shiftOfLabel, y, str(labels[i]))

    # qp, x1:int, x2:int, y:int labels:list<str>
    def __createHorizontalLegend(self, qp, x1, x2, y, labels, c, position="up"):
        sizeOfInterval = (x2 - x1) / (len(labels) -1)
        for i in range(len(labels)):
           x = x1 + i * sizeOfInterval
           if position == "up":
              shiftOfLine = 5;
              shiftOfLabel = 15;
           if position == "down":
              shiftOfLine = -5;
              shiftOfLabel = -15;
           qp.drawLine(x, y, x, y +shiftOfLine)
           qp.drawText(x, y +shiftOfLabel, str(labels[i]))

    def __arrowToTheLeft(self, qp, x, y, c):
        qp.drawLine(x, y, x -c.getLengthOfArrow(), y)
        qp.drawLine(x -c.getLengthOfArrow(), y,
            x -c.getLengthOfArrow() +c.getWingOfArrow(), y -c.getWingOfArrow())
        qp.drawLine(x -c.getLengthOfArrow(), y,
            x -c.getLengthOfArrow() +c.getWingOfArrow(), y +c.getWingOfArrow())

    def __arrowToTheRight(self, qp, x, y, c):
        qp.drawLine(x, y, x +c.getLengthOfArrow(), y)
        qp.drawLine(x +c.getLengthOfArrow(), y,
            x +c.getLengthOfArrow() -c.getWingOfArrow(), y -c.getWingOfArrow())
        qp.drawLine(x +c.getLengthOfArrow(), y,
            x +c.getLengthOfArrow() -c.getWingOfArrow(), y +c.getWingOfArrow())

    def __arrowToTheDown(self, qp, x, y, c):
        qp.drawLine(x, y +c.getLengthOfArrow(), x, y)
        qp.drawLine(x, y +c.getLengthOfArrow(),
            x -c.getWingOfArrow(), y +c.getLengthOfArrow() -c.getWingOfArrow())
        qp.drawLine(x, y +c.getLengthOfArrow(),
            x +c.getWingOfArrow(), y +c.getLengthOfArrow() -c.getWingOfArrow())

    def __arrowToTheUp(self, qp, x, y, c):
        qp.drawLine(x, y, x, y -c.getLengthOfArrow())
        qp.drawLine(x, y -c.getLengthOfArrow(),
            x -c.getWingOfArrow(), y -c.getLengthOfArrow() +c.getWingOfArrow())
        qp.drawLine(x, y -c.getLengthOfArrow(),
            x +c.getWingOfArrow(), y -c.getLengthOfArrow() +c.getWingOfArrow())