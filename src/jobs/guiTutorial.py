from PyQt5 import QtWidgets

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *



def gui1():
  app = QtWidgets.QApplication([])

  button = QtWidgets.QPushButton("Click to Exit")
  button.setWindowTitle("Goodbye World")
  button.clicked.connect(app.quit)

  button.show()

  app.exec()

def gui2():
  app = QtWidgets.QApplication([])

  # Hlavní okno
  main = QtWidgets.QWidget()
  main.setWindowTitle('Hello Qt')

  # Layout pro hlavní okno
  layout = QtWidgets.QHBoxLayout()
  main.setLayout(layout)

  # Nápis
  label = QtWidgets.QLabel('Click the button to change me')
  # Přidáním do layoutu se nápis automaticky stane potomkem hlavního okna
  layout.addWidget(label)

#  l1 = QLabel()
#  l1.setPixmap(QPixmap("/home/stepan/workspaceJup/LinPrefMod/python.jpg"))
#  layout.addWidget(l1)
#  vbox = QVBoxLayout()
#  vbox.addWidget(l1)
#  layout.addWidget(vbox)

  # Tlačítko
  button = QtWidgets.QPushButton('Click me')
  layout.addWidget(button)

  # Funkcionalita
  def change_label():
    label.setText('Good job. +100 points.')

  button.clicked.connect(change_label)

  label2 = QtWidgets.QLabel('Click the button to change me')
  layout.addWidget(label2)

  # Spuštění
  main.show()
  app.exec()


def gui3():
   app = QApplication(sys.argv)
   win = QWidget()
   l1 = QLabel()
   l1.setPixmap(QPixmap("/home/stepan/workspaceJup/LinPrefMod/python.jpg"))

   vbox = QVBoxLayout()
   vbox.addWidget(l1)
   win.setLayout(vbox)
   win.setWindowTitle("QPixmap Demo")
   win.show()
   sys.exit(app.exec_())




class Example(QWidget):

   def __init__(self):
      super(Example, self).__init__()
      self.initUI()

   def initUI(self):
      self.text = "hello world"
      self.setGeometry(100,100, 400,300)
      self.setWindowTitle('Draw Demo')
      self.show()

   def paintEvent(self, event):
      qp = QPainter()
      qp.begin(self)
      qp.setPen(QColor(Qt.red))
      qp.setFont(QFont('Arial', 20))

      qp.drawText(10,50, "hello Python")
      qp.setPen(QColor(Qt.blue))
      qp.drawLine(10,100,100,100)
      qp.drawRect(10,150,150,100)

      qp.setPen(QColor(Qt.yellow))
      qp.drawEllipse(100,50,100,50)
      qp.drawPixmap(220,10,QPixmap("../python.jpg"))
      qp.fillRect(200,175,150,100,QBrush(Qt.SolidPattern))
      qp.end()

def gui():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
