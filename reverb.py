from pyo import *
import random

s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for ob-6
# set the input device
s.setInputDevice(1) # zoom
# set the output device
s.setOutputDevice(2) # headphones: 2 when zoom is used, 0 when not

s.boot()
interface = Input().play().out()





s.gui(locals())