from pyo import *
import random

s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for ob-6
# set the input device
s.setInputDevice(1) # zoom
# set the output device
s.setOutputDevice(2) # headphones: 2 when zoom is used, 0 when not

s.boot()
interface = Input().play().out()

# Half-sine window used as the amplitude envelope of the overlaps.
env = WinTable(8)

# Length of the window in seconds.
wsize = 0.1

# Amount of transposition in semitones.
trans = -7

# Compute the transposition ratio.
ratio = pow(2.0, trans / 12.0)

# Compute the reading head speed.
rate = -(ratio - 1) / wsize

# Two reading heads out-of-phase.
ind = Phasor(freq=rate, phase=[0, 0.5])

# Each head reads the amplitude envelope...
win = Pointer(table=env, index=ind, mul=0.7)

# ... and modulates the delay time (scaled by the window size) of a delay line.
# mix(1) is used to mix the two overlaps on a single audio stream.
snd = Delay(interface, delay=ind * wsize, mul=win).mix(1)

# The transposed signal is sent to the right speaker.
snd.out(1)


s.gui(locals())