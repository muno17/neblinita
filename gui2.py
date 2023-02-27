import sys
from random import *
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QDial,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor

# class to create color for window
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("neblina")
        self.setFixedSize(QSize(500,300))

        label1_layout = QHBoxLayout

        self.stacklayout = QStackedLayout()
        self.stacklayout.addWidget(Color("grey"))
        self.stacklayout.setCurrentIndex(0)

        title = QLabel("neblina")
        title_font = title.font()
        title_font.setPointSize(30)
        title.setFont(title_font)
        title.setAlignment

        self.setCentralWidget(self)

    # create title
    #def name()

    # create input dropdown
    #def input()

    # create output dropdown
    #def output()

    #create wet/dry knob
    #def wet_dry()

    # create melt (disintegrate) knob
    #def melt

    # create luz subsection
    #def luz()

    # create fractals knob
    #def fractals()

    # create luz delay knob
    #def luz_delay()

    # create luz space knob
    #def luz_space()

    # create oscuridad subsection
    #def oscuridad()

    # create haze knob
    #def haze()

    # create oscuridad delay knob
    #def osc_delay()

    # create oscuridad space knob
    #def osc_space()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()