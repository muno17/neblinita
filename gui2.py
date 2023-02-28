import sys
from random import *
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QDial, QStackedLayout, QComboBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor



class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setStyleSheet("background-color: grey")
        self.setWindowTitle("neblina")
        self.setFixedSize(QSize(450,300))

        self.input = QComboBox(self)
        self.input.move(55, 175)

        self.wet_dry = QDial(self)
        self.wet_dry.setNotchesVisible(True)
        self.wet_dry.setWrapping(False)
        self.wet_dry.move(55, 175)

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

        # label - title - neblina - find way to have font not cut off
        self.title = QLabel("neblina", self)
        title_font = self.title.font()
        title_font.setPointSize(24)
        title_font.setFamily('Monaco')
        self.title.setFont(title_font)
        self.title.move(15, 10)


        # label - luz
        self.luz = QLabel("luz", self)
        luz_font = self.luz.font()
        luz_font.setPointSize(20)
        luz_font.setFamily('Monaco')
        self.luz.setFont(luz_font)
        self.luz.move(210, 60)

        # label - sombra
        self.sombra = QLabel("sombra", self)
        sombra_font = self.sombra.font()
        sombra_font.setPointSize(20)
        sombra_font.setFamily('Monaco')
        self.sombra.setFont(sombra_font)
        self.sombra.move(325, 60)

        # label - input
        self.inpt = QLabel("input", self)
        inpt_font = self.inpt.font()
        inpt_font.setPointSize(10)
        inpt_font.setFamily('Monaco')
        self.inpt.setFont(inpt_font)
        self.inpt.move(60, 45)

        # label - output
        self.outpt = QLabel("output", self)
        outpt_font = self.outpt.font()
        outpt_font.setPointSize(10)
        outpt_font.setFamily('Monaco')
        self.outpt.setFont(outpt_font)
        self.outpt.move(59, 95)

        # label - wet/dry
        self.wtdry = QLabel("wet/dry", self)
        wtdry_font = self.wtdry.font()
        wtdry_font.setPointSize(10)
        wtdry_font.setFamily('Monaco')
        self.wtdry.setFont(wtdry_font)
        self.wtdry.move(55, 202)

        # label - melt
        self.mlt = QLabel("melt", self)
        mlt_font = self.mlt.font()
        mlt_font.setPointSize(10)
        mlt_font.setFamily('Monaco')
        self.mlt.setFont(mlt_font)
        self.mlt.move(63, 270)

        # label - fractals
        self.frctls = QLabel("fractals", self)
        frctls_font = self.frctls.font()
        frctls_font.setPointSize(10)
        frctls_font.setFamily('Monaco')
        self.frctls.setFont(frctls_font)
        self.frctls.move(205, 120)

        # label - luz delay
        self.ldly = QLabel("delay", self)
        ldly_font = self.ldly.font()
        ldly_font.setPointSize(10)
        ldly_font.setFamily('Monaco')
        self.ldly.setFont(ldly_font)
        self.ldly.move(213, 202)

        # label - luz space
        self.lspc = QLabel("space", self)
        lspc_font = self.lspc.font()
        lspc_font.setPointSize(10)
        lspc_font.setFamily('Monaco')
        self.lspc.setFont(lspc_font)
        self.lspc.move(213, 270)

        # label - haze
        self.hze = QLabel("haze", self)
        hze_font = self.hze.font()
        hze_font.setPointSize(10)
        hze_font.setFamily('Monaco')
        self.hze.setFont(hze_font)
        self.hze.move(350, 120)

        # label - sombra delay
        self.sdly = QLabel("delay", self)
        sdly_font = self.sdly.font()
        sdly_font.setPointSize(10)
        sdly_font.setFamily('Monaco')
        self.sdly.setFont(sdly_font)
        self.sdly.move(345, 202)

        # label - sombra space
        self.sspc = QLabel("space", self)
        sspc_font = self.sspc.font()
        sspc_font.setPointSize(10)
        sspc_font.setFamily('Monaco')
        self.sspc.setFont(sspc_font)
        self.sspc.move(344, 270)

        #self.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()