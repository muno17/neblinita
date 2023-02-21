from pyo import *
import time
import random


# initiate server
s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for ob-6
# set the input device
s.setInputDevice(1) # zoom
# set the output device
s.setOutputDevice(2) # headphones: 2 when zoom is used, 0 when not

# boot server
s.boot()
interface = Input().play().out()

og_wave = Scope(interface)

n = Noise()

h1 = Harmonizer(interface).out()
h2 = Harmonizer(h1).out()
h3 = Harmonizer(h2).out()
h4 = Harmonizer(h3).out()
ch = Chorus(h4).out()

#distortion()


# run server with a small gui
new_wave = Scope()
s.start()
s.gui(locals())


# If your final output uses less channels than the number of audio streams in an object, don’t 
# forget to mix it down (call its mix() method) before applying effects on the sum of the signals.