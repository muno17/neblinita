from pyo import *
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QDial, QStackedLayout, QComboBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor
import time
import random
import sys

# main window for gui
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

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
        self.wet_dry.setMinimum(1)
        self.wet_dry.setMaximum(100)
        self.wet_dry.setValue(1)
        self.wet_dry.valueChanged.connect(self.wet_dry_value)
        print(wet_dry.Value)

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
        self.melt.setMinimum(1)
        self.melt.setMaximum(100)
        self.melt.setValue(1)
        self.melt.valueChanged.connect(self.melt_value)

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
        self.fractals.setMinimum(1)
        self.fractals.setMaximum(100)
        self.fractals.setValue(50)
        self.fractals.valueChanged.connect(self.fractals_value)

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
        self.luz_delay.setMinimum(1)
        self.luz_delay.setMaximum(100)
        self.luz_delay.setValue(50)
        self.luz_delay.valueChanged.connect(self.luz_delay_value)

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
        self.luz_space.setMinimum(1)
        self.luz_space.setMaximum(100)
        self.luz_space.setValue(50)
        self.luz_space.valueChanged.connect(self.luz_space_value)

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
        self.haze.setMinimum(1)
        self.haze.setMaximum(100)
        self.haze.setValue(0)
        self.haze.valueChanged.connect(self.haze_value)

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
        self.sombra_delay.setMinimum(1)
        self.sombra_delay.setMaximum(100)
        self.sombra_delay.setValue(50)
        self.sombra_delay.valueChanged.connect(self.sombra_delay_value)

        ### knob for sombra space ###
        self.sspc = QLabel("space", self)
        sspc_font = self.sspc.font()
        sspc_font.setPointSize(10)
        sspc_font.setFamily('Monaco')
        self.sspc.setFont(sspc_font)
        self.sspc.move(344, 270)

        self.sombra_space = QDial(self)
        self.sombra_space.setNotchesVisible(True)
        self.sombra_space.setWrapping(False)
        self.sombra_space.move(309, 243)
        self.sombra_space.setMinimum(1)
        self.sombra_space.setMaximum(100)
        self.sombra_space.setValue(50)
        self.sombra_space.valueChanged.connect(self.sombra_space_value)

        self.show()

    def wet_dry_value(self):
        #print("wet/dry: ", self.wet_dry.value())
        return self.wet_dry.value()

    def melt_value(self):
        #print("melt: ", self.melt.value())
        return self.melt.value()

    def fractals_value(self):
        #print("fractals: ", self.fractals.value())
        return self.fractals.value()

    def luz_delay_value(self):
        #print("luz_delay: ", self.luz_delay.value())
        return self.luz_delay.value()

    def luz_space_value(self):
        #print("luz_space: ", self.luz_space.value())
        return self.luz_space.value()

    def haze_value(self):
        #print("haze: ", self.haze.value())
        return self.haze.value()

    def sombra_delay_value(self):
        #print("sombra_delay: ", self.sombra_delay.value())
        return self.sombra_delay.value()

    def sombra_space_value(self):
        #print("sombra_space: ", self.sombra_space.value())
        return self.sombra_space.value()


def main():

    app = QApplication(sys.argv)
    window = MainWindow()

    # initiate pyo server
    s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for headphones
    s.amp = 0.18
    # set the input device
    s.setInputDevice(1) # zoom
    # set the output device
    s.setOutputDevice(2) # headphones: when zoom is used 2 - headphones, 4 - speakers

    # boot server
    s.boot()
    # get buffer time
    buftime = s.getBufferSize() / s.getSamplingRate()
    # dry signal
    dry = Input()
    # create copy of input for fog reverb
    wet_path1 = dry
    # create copy of input for light reverb
    wet_path2 = dry

    ### signal chain for sombra reverb ###
    distortion_out = distortion(wet_path1)
    left_distdelay, right_distdelay = distdelay(distortion_out, buftime)
    left_dirtdelay, right_dirtdelay = dirtdelay(left_distdelay, right_distdelay, buftime)
    left_gv, right_gv = grimeverb(left_dirtdelay, right_dirtdelay)
    left_grimeverb = (left_gv * .5)
    right_grimeverb = (right_gv * .5)

    ### signal chain for luz reverb ###
    delay1_left, delay1_right = delay1(wet_path2, buftime)
    delay2_left, delay2_right = delay2(delay1_left, delay1_right, buftime)
    chorus_left, chorus_right = chorus(delay2_left, delay2_right)
    wet_left, wet_right = reverb(chorus_left, chorus_right)
    left_lightverb = (wet_left * .6)
    right_lightverb = (wet_right * .6)

    ### mixer ###
    master = mix(dry, left_grimeverb, right_grimeverb, left_lightverb, right_lightverb, window.wet_dry_value())
    master.out()

    # start the pyo server and execute the gui
    s.start()
    app.exec()


def mix(dry, left_grimeverb, right_grimeverb, left_lightverb, right_lightverb, wet_dry_val):
    wet_dry = wet_dry_val / 100

    dry_val = 1 - (wet_dry - 0.01)
    lgv_val = wet_dry - 0.01
    rgv_val = wet_dry - 0.01
    llv_val = wet_dry - 0.01
    rlv_val = wet_dry - 0.01

    mix = Mixer(chnls=5, mul=.55)
    mix.addInput(0, dry)
    mix.addInput(1, left_grimeverb)
    mix.addInput(2, right_grimeverb)
    mix.addInput(3, left_lightverb)
    mix.addInput(4, right_lightverb)
    mix.setAmp(0, 0, dry_val) # dry  - .25 50% wet
    mix.setAmp(1, 0, lgv_val) # left_grimeverb - .5 50% wet
    mix.setAmp(2, 0, rgv_val) # right_grimeverb - .5 50% wet
    mix.setAmp(3, 0, llv_val) # left_lightverb - .6 50% wet
    mix.setAmp(4, 0, rlv_val) # right_lightverb - .6 50% wet

    return mix


def distortion(wet_path1):
    # Distortion parameters
    BP_CENTER_FREQ = 400  # Bandpass filter center frequency.
    BP_Q = 3  # Bandpass Q (center_freq / Q = bandwidth).
    BOOST = 25  # Pre-boost (linear gain).
    LP_CUTOFF_FREQ = 3000  # Lowpass filter cutoff frequency.
    BALANCE = 0.9  # Balance dry - wet.


    # The transfert function is build in two phases.
    # 1. Transfert function for signal lower than 0.
    table = ExpTable([(0, -0.25), (4096, 0), (8192, 0)], exp=30)
    # 2. Transfert function for signal higher than 0.
    # First, create an exponential function from 1 (at the beginning of the table)
    # to 0 (in the middle of the table).
    high_table = ExpTable([(0, 1), (2000, 1), (4096, 0), (4598, 0), (8192, 0)], exp=5, inverse=False)
    # Then, reverse the table’s data in time, to put the shape in the second
    # part of the table.
    high_table.reverse()
    # Finally, add the second table to the first, point by point.
    table.add(high_table)

    # Bandpass filter and boost gain applied on input signal.
    bp = ButBP(wet_path1, freq=BP_CENTER_FREQ, q=BP_Q)
    boost = Sig(bp, mul=BOOST)

    # Apply the transfert function.
    sig = Lookup(table, boost)

    # Lowpass filter on the distorted signal.
    lp = ButLP(sig, freq=LP_CUTOFF_FREQ, mul=0.6)

    # Balance between dry and wet signals.
    mixed = Interp(wet_path1, lp, interp=BALANCE)

    return mixed


def distdelay(distortion_out, buftime):
    noise = BrownNoise(0.4)
    
    # Delay parameters
    delay_time_l = Sig(0.08)  # Delay time for the left channel delay.
    delay_feed = Sig(0.3)  # Feedback value for both delays.

    # Because the right delay gets its input sound from the left delay, while
    # it is computed before (to send its output sound to the left delay), it
    # will be one buffer size late. To compensate this additional delay on the
    # right, we substract one buffer size from the real delay time.
    delay_time_r = Sig(delay_time_l, add=-buftime)

    # Initialize the right delay with zeros as input because the left delay
    # does not exist yet.
    right = Delay(Sig(0), delay=delay_time_r)

    # Initialize the left delay with the original mono source and the right
    # delay signal (multiplied by the feedback value) as input.
    left = Delay(distortion_out + right * delay_feed, delay=delay_time_l)

    # One issue with recursive cross-delay is if we set the feedback to
    # 0, the right delay never gets any signal. To resolve this, we add a
    # non-recursive delay, with a gain that is the inverse of the feedback,
    # to the right delay input.
    original_delayed = Delay(distortion_out, delay_time_l, mul=1 - delay_feed)

    # Change the right delay input (now that the left delay exists).
    right.setInput(original_delayed + left * delay_feed)

    dleft = Disto(left, drive=0.0, slope=.8)
    dright = Disto(left, drive=0.0, slope=.8)

    dleft.setDrive(0.0) # controlled by haze
    dright.setDrive(0.0) # controlled by haze

    return dleft, dright

    
def dirtdelay(left_distdelay, right_distdelay, buftime):
    delay_time_l = Sig(0.3)  # Delay time for the left channel delay.
    delay_feed = Sig(0.8)  # Feedback value for both delays.

    # buffer compensation
    delay_time_r = Sig(delay_time_l, add=-buftime)

    # Initialize the right delay with zeros as input because the left delay
    # does not exist yet.
    right = Delay(Sig(0), delay=delay_time_r)

    # Initialize the left delay with the original mono source and the right
    # delay signal (multiplied by the feedback value) as input.
    left = Delay(left_distdelay + right_distdelay + right * delay_feed, delay=delay_time_l)

    # non-recursive delay fed to right output
    original_delayed = Delay(left_distdelay + right_distdelay, delay_time_l, mul=1 - delay_feed)

    # Change the right delay input (now that the left delay exists).
    right.setInput(original_delayed + left * delay_feed)

    def playit():
        "Assign a sound to the player and start playback."
        which = random.randint(1, 4)
        path = wet_path % which
        #sf.path = path
        signal.play()

    # Call the function "playit" every second.
    pat = Pattern(playit, 1).play()

    lout = (left * .1)
    rout = (right * .1)

    return lout, rout


def grimeverb(left_dirtdelay, right_dirtdelay):
    # The delay times are chosen to be as uncorrelated as possible.
    # Prime numbers are a good choice for delay lengths in samples.
    # left channel
    comb1 = Delay(left_dirtdelay, delay=[0.0997, 0.4277], feedback=0.50)
    comb2 = Delay(left_dirtdelay, delay=[0.7371, 0.0393], feedback=0.65)
    comb3 = Delay(left_dirtdelay, delay=[0.5411, 0.0409], feedback=0.5)
    comb4 = Delay(left_dirtdelay, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_left = left_dirtdelay + comb1 + comb2 + comb3 + comb4

    #right channel
    comb5 = Delay(right_dirtdelay, delay=[0.0997, 0.4277], feedback=0.50)
    comb6 = Delay(right_dirtdelay, delay=[0.7371, 0.0393], feedback=0.65)
    comb7 = Delay(right_dirtdelay, delay=[0.5411, 0.0409], feedback=0.5)
    comb8 = Delay(right_dirtdelay, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_right = right_dirtdelay + comb5 + comb6 + comb7 + comb8

    # The sum of the original signal and the comb filters
    # feeds two serial allpass filters.
    left_all1 = Allpass(combsum_left, delay=[0.005, 0.00507], feedback=0.75)
    left_all2 = Allpass(left_all1, delay=[0.0117, 0.0123], feedback=0.61)
    right_all1 = Allpass(combsum_right, delay=[0.005, 0.00507], feedback=0.75)
    right_all2 = Allpass(right_all1, delay=[0.0117, 0.0123], feedback=0.61)

    # Brightness control.
    left_lowp = Tone(left_all2, freq=3500, mul=0.25)
    right_lowp = Tone(right_all2, freq=3500, mul=0.25)

    return left_lowp, right_lowp


def delay1(wet_path, buftime):
    # Delay parameters
    delay_time_l = Sig(0.1)  # Delay time for the left channel delay.
    #delay_time_l.ctrl() # slider
    delay_feed = Sig(0.6)  # Feedback value for both delays.
    #delay_feed.ctrl() # slider

    # buffer compensation
    delay_time_r = Sig(delay_time_l, add=-buftime)

    # Initialize the right delay with zeros as input because the left delay
    # does not exist yet.
    right = Delay(Sig(0), delay=delay_time_r)

    # Initialize the left delay with the original mono source and the right
    # delay signal (multiplied by the feedback value) as input.
    left = Delay(wet_path + right * delay_feed, delay=delay_time_l)

    # non-recursive delay fed to right output
    original_delayed = Delay(wet_path, delay_time_l, mul=1 - delay_feed)

    # Change the right delay input (now that the left delay exists).
    right.setInput(original_delayed + left * delay_feed)

    def playit():
        "Assign a sound to the player and start playback."
        which = random.randint(1, 4)
        path = wet_path % which
        #sf.path = path
        signal.play()

    # Call the function "playit" every second.
    pat = Pattern(playit, 1).play()

    return left, right


def delay2(delay1_left, delay1_right, buftime):
    # Delay parameters
    delay_time_l = Sig(0.4)  # Delay time for the left channel delay.
    #delay_time_l.ctrl() # slider
    delay_feed = Sig(0.8)  # Feedback value for both delays.
    #delay_feed.ctrl() # slider

    # buffer compensation
    delay_time_r = Sig(delay_time_l, add=-buftime)

    # Initialize the right delay with zeros as input because the left delay
    # does not exist yet.
    right = Delay(Sig(0), delay=delay_time_r)

    # Initialize the left delay with the original mono source and the right
    # delay signal (multiplied by the feedback value) as input.
    left = Delay(delay1_left + delay1_right + right * delay_feed, delay=delay_time_l)

    # non-recursive delay fed to right output
    original_delayed = Delay(delay1_left + delay1_right, delay_time_l, mul=1 - delay_feed)

    # Change the right delay input (now that the left delay exists).
    right.setInput(original_delayed + left * delay_feed)

    def playit():
        "Assign a sound to the player and start playback."
        which = random.randint(1, 4)
        path = wet_path % which
        #sf.path = path
        signal.play()

    # Call the function "playit" every second.
    pat = Pattern(playit, 1).play()

    return left, right


def chorus(delay_left, delay_right):
    # Sets values for 8 LFO'ed delay lines (you can add more if you want!).
    # LFO frequencies.
    freqs = [0.254, 0.465, 0.657, 0.879, 1.23, 1.342, 1.654, 1.879]
    # Center delays in seconds.
    cdelay = [0.0087, 0.0102, 0.0111, 0.01254, 0.0134, 0.01501, 0.01707, 0.0178]
    # Modulation depths in seconds.
    adelay = [0.001, 0.0012, 0.0013, 0.0014, 0.0015, 0.0016, 0.002, 0.0023]

    # Create 8 sinusoidal LFOs with center delays "cdelay" and depths "adelay".
    lfos = Sine(freqs, mul=adelay, add=cdelay)

    # Create 8 modulated delay lines with a little feedback
    left_chorus = Delay(delay_left, lfos, feedback=0.3, mul=0.3)
    right_chorus = Delay(delay_right, lfos, feedback=0.4, mul=0.3)

    return left_chorus, right_chorus


def  reverb(chorus_left, chorus_right):
    # The delay times are chosen to be as uncorrelated as possible.
    # Prime numbers are a good choice for delay lengths in samples.
    # left channel
    comb1 = Delay(chorus_left, delay=[0.0997, 0.4277], feedback=0.90)
    comb2 = Delay(chorus_left, delay=[0.7371, 0.0393], feedback=0.85)
    comb3 = Delay(chorus_left, delay=[0.5411, 0.0409], feedback=0.5)
    comb4 = Delay(chorus_left, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_left = chorus_left + comb1 + comb2 + comb3 + comb4

    #right channel
    comb5 = Delay(chorus_right, delay=[0.0997, 0.4277], feedback=0.90)
    comb6 = Delay(chorus_right, delay=[0.7371, 0.0393], feedback=0.85)
    comb7 = Delay(chorus_right, delay=[0.5411, 0.0409], feedback=0.5)
    comb8 = Delay(chorus_right, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_right = chorus_right + comb5 + comb6 + comb7 + comb8

    # The sum of the original signal and the comb filters
    # feeds two serial allpass filters.
    left_all1 = Allpass(combsum_left, delay=[0.005, 0.00507], feedback=0.75)
    left_all2 = Allpass(left_all1, delay=[0.0117, 0.0123], feedback=0.61)
    right_all1 = Allpass(combsum_right, delay=[0.005, 0.00507], feedback=0.75)
    right_all2 = Allpass(right_all1, delay=[0.0117, 0.0123], feedback=0.61)

    # Brightness control.
    left_lowp = Tone(left_all2, freq=3500, mul=0.25)
    right_lowp = Tone(right_all2, freq=3500, mul=0.25)

    return left_lowp, right_lowp


if __name__ == "__main__":
    main()