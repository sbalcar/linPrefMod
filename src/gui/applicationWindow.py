#!/usr/bin/python3
import sys

from matplotlib.backends.qt_compat import QtWidgets, is_pyqt5
if is_pyqt5():
    pass
else:
    pass

from gui.frame.simpleShowFrame.simpleShowFrame_old import SimpleShowFrame_old
from gui.frame.simpleShowFrame.simpleShowFrame import SimpleShowFrame
from gui.frame.twoUsersFrame.modelTwoUsersFrame import ModelTwoUsersFrame

from gui.frame.tresholdFrame.thresholdFrame import ThresholdFrame #class

from gui.frame.ndFrame.ndFrame import NdFrame #class

from PyQt5.QtWidgets import (QAction)



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Linear Monotone Preference Model')

        self.width = 100
        self.height = 100

        self.menu()

        self._main = QtWidgets.QWidget()

        self.setCentralWidget(self._main)
        self.layout = QtWidgets.QGridLayout(self._main)
        
        #simpleShowFrame_old:ModelOneUserFrame
        #self.simpleShowFrame_old = SimpleShowFrame_old(self.layout)
        #simpleShowFrame:ModelOneUserFrame
        self.simpleShowFrame = SimpleShowFrame(self.layout)

        #modelTwoUsersFrame:ModelTwoUsersFrame
        self.modelTwoUsersFrame = ModelTwoUsersFrame(self.layout)

        #thresholdFrame:ThresholdFrame
        self.thresholdFrame = ThresholdFrame(self.layout)

        #ndFrame:OneUserFrame
        self.ndFrame = NdFrame(self.layout)

        self.currentFrame = self.simpleShowFrame
        self.currentFrame.show(self.width, self.height)
        #self.actionShowOneUser();

    def clearLayout(self):
         self.__clearLayout(self.layout)

    def __clearLayout(self, layout):
        if layout == None:
           return
        while layout.count():
           child = layout.takeAt(0)
           if child.widget() is not None:
              child.widget().deleteLater()
              child.widget().close()
           elif child.layout() is not None:
              self.__clearLayout(child.layout())

    def menu(self):
        menubar = self.menuBar()
        modelsMenu = menubar.addMenu('Models')
        menuThreshold = menubar.addMenu('Threshold')
        menuND = menubar.addMenu('ND')
        menuExit = menubar.addMenu('Exit')

        pActionSimpleShow = QAction('Simple show', self)
        pActionSimpleShow.triggered.connect(self.actionSimpleShow)

        pActionTwoUser = QAction('With two user', self)
        #pActionTwoUser.triggered.connect(self.actionShowTwoUserModel)

        modelsMenu.addAction(pActionSimpleShow)
        modelsMenu.addAction(pActionTwoUser)

        thresholdAction = QAction("&Threshold", self)
        thresholdAction.setShortcut("Ctrl+T")
        thresholdAction.setStatusTip('Threshold')
        thresholdAction.triggered.connect(self.actionShowThreshold)

        menuThreshold.addAction(thresholdAction)

        nDAction = QAction("&ND", self)
        nDAction.setShortcut("Ctrl+N")
        nDAction.setStatusTip('ND')
        #nDAction.triggered.connect(self.actionShowNd)

        menuND.addAction(nDAction)

        closeAction = QAction("&Quit", self)
        closeAction.setShortcut("Ctrl+Q")
        closeAction.setStatusTip('Leave The App')
        closeAction.triggered.connect(self.actionCloseApplication)

        menuExit.addAction(closeAction)

    def actionSimpleShow(self):
        self.clearLayout()
        self.currentFrame = self.simpleShowFrame
        self.simpleShowFrame.show(self.width, self.height)

    def actionShowTwoUserModel(self):
        self.clearLayout()
        self.currentFrame = self.modelTwoUsersFrame
        self.modelTwoUsersFrame.show(self.width, self.height)

    def actionShowThreshold(self):
        self.clearLayout()
        self.currentFrame = self.thresholdFrame
        self.thresholdFrame.show(self.width, self.height)

    def actionShowNd(self):
        self.clearLayout()
        self.currentFrame = self.ndFrame
        self.ndFrame.show(self.width, self.height)

    def resizeEvent(self, event):
        #print("resizeEvent")
        self.width = event.size().width()
        self.height = event.size().height()

        self.clearLayout()
        self.currentFrame.show(self.width, self.height)


    def actionCloseApplication(self):
        sys.exit()


