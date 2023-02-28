import sys
from random import *
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QDial, QStackedLayout, QComboBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setStyleSheet("background-color: grey")
        self.setWindowTitle("neblina")
        self.setFixedSize(QSize(450,300))
                

        ### label - neblina ###
        self.title = QLabel("neblina", self)
        title_font = self.title.font()
        title_font.setPointSize(24)
        title_font.setFamily('Monaco')
        self.title.setFont(title_font)
        self.title.move(15, 10)

        ### label - muno ###
        self.muno = QLabel("muno audio", self)
        muno_font = self.muno.font()
        muno_font.setPointSize(16)
        muno_font.setFamily('Monaco')
        self.muno.setFont(muno_font)
        self.muno.move(330, 10)

        ### label - luz ###
        self.luz = QLabel("luz", self)
        luz_font = self.luz.font()
        luz_font.setPointSize(18)
        luz_font.setFamily('Monaco')
        self.luz.setFont(luz_font)
        self.luz.move(214, 65)

        ### label - sombra ###
        self.sombra = QLabel("sombra", self)
        sombra_font = self.sombra.font()
        sombra_font.setPointSize(18)
        sombra_font.setFamily('Monaco')
        self.sombra.setFont(sombra_font)
        self.sombra.move(325, 65)

        ### input dropdown ###
        self.inpt = QLabel("input", self)
        inpt_font = self.inpt.font()
        inpt_font.setPointSize(10)
        inpt_font.setFamily('Monaco')
        self.inpt.setFont(inpt_font)
        self.inpt.move(80, 45)

        self.input = QComboBox(self)
        self.input.addItems(["one, two, three"])
        self.input.move(47, 75)

        ### output dropdown ###
        self.outpt = QLabel("output", self)
        outpt_font = self.outpt.font()
        outpt_font.setPointSize(10)
        outpt_font.setFamily('Monaco')
        self.outpt.setFont(outpt_font)
        self.outpt.move(79, 107)

        self.output = QComboBox(self)
        self.output.addItems(["one, two, three"])
        self.output.move(47, 132)

        ### knob for wet/dry ###
        self.wtdry = QLabel("wet/dry", self)
        wtdry_font = self.wtdry.font()
        wtdry_font.setPointSize(10)
        wtdry_font.setFamily('Monaco')
        self.wtdry.setFont(wtdry_font)
        self.wtdry.move(75, 202)

        self.wet_dry = QDial(self)
        self.wet_dry.setNotchesVisible(True)
        self.wet_dry.setWrapping(False)
        self.wet_dry.move(45, 175)

        ### knob for melt ###
        self.mlt = QLabel("melt", self)
        mlt_font = self.mlt.font()
        mlt_font.setPointSize(10)
        mlt_font.setFamily('Monaco')
        self.mlt.setFont(mlt_font)
        self.mlt.move(83, 270)

        self.melt = QDial(self)
        self.melt.setNotchesVisible(True)
        self.melt.setWrapping(False)
        self.melt.move(45, 243)

        ### knob for fractals ###
        self.frctls = QLabel("fractals", self)
        frctls_font = self.frctls.font()
        frctls_font.setPointSize(10)
        frctls_font.setFamily('Monaco')
        self.frctls.setFont(frctls_font)
        self.frctls.move(208, 134)

        self.fractals = QDial(self)
        self.fractals.setNotchesVisible(True)
        self.fractals.setWrapping(False)
        self.fractals.move(180, 107)

        ### knob for luz delay ###
        self.ldly = QLabel("delay", self)
        ldly_font = self.ldly.font()
        ldly_font.setPointSize(10)
        ldly_font.setFamily('Monaco')
        self.ldly.setFont(ldly_font)
        self.ldly.move(215, 202)

        self.luz_delay = QDial(self)
        self.luz_delay.setNotchesVisible(True)
        self.luz_delay.setWrapping(False)
        self.luz_delay.move(180, 175)

        ### knob for luz space ###
        self.lspc = QLabel("space", self)
        lspc_font = self.lspc.font()
        lspc_font.setPointSize(10)
        lspc_font.setFamily('Monaco')
        self.lspc.setFont(lspc_font)
        self.lspc.move(215, 270)

        self.luz_space = QDial(self)
        self.luz_space.setNotchesVisible(True)
        self.luz_space.setWrapping(False)
        self.luz_space.move(180, 243)

        ### knob for haze ###
        self.hze = QLabel("haze", self)
        hze_font = self.hze.font()
        hze_font.setPointSize(10)
        hze_font.setFamily('Monaco')
        self.hze.setFont(hze_font)
        self.hze.move(348, 134)

        self.haze = QDial(self)
        self.haze.setNotchesVisible(True)
        self.haze.setWrapping(False)
        self.haze.move(309, 107)

        ### knob for sombra delay ###
        self.sdly = QLabel("delay", self)
        sdly_font = self.sdly.font()
        sdly_font.setPointSize(10)
        sdly_font.setFamily('Monaco')
        self.sdly.setFont(sdly_font)
        self.sdly.move(345, 202)

        self.sombra_delay = QDial(self)
        self.sombra_delay.setNotchesVisible(True)
        self.sombra_delay.setWrapping(False)
        self.sombra_delay.move(309, 175)

        ### knob for sombra space ###
        self.sspc = QLabel("space", self)
        sspc_font = self.sspc.font()
        sspc_font.setPointSize(10)
        sspc_font.setFamily('Monaco')
        self.sspc.setFont(sspc_font)
        self.sspc.move(344, 270)

        self.luz_space = QDial(self)
        self.luz_space.setNotchesVisible(True)
        self.luz_space.setWrapping(False)
        self.luz_space.move(309, 243)

        self.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()