import sys
from random import *
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(500, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):

        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('grey'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Monaco')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(10, 50, 'neblina')
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()