from pyo import *
import random

s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for ob-6
# set the input device
s.setInputDevice(1) # zoom
# set the output device
s.setOutputDevice(2) # headphones: 2 when zoom is used, 0 when not

s.boot()
interface = Input().play().out()


# Four parallel stereo comb filters. The delay times are chosen
# to be as uncorrelated as possible. Prime numbers are a good
# choice for delay lengths in samples.
comb1 = Delay(interface, delay=[0.0997, 0.4277], feedback=0.90)
comb2 = Delay(interface, delay=[0.7371, 0.0393], feedback=0.85)
comb3 = Delay(interface, delay=[0.5411, 0.0409], feedback=0.5)
comb4 = Delay(interface, delay=[0.1137, 0.7155], feedback=0.73)

combsum = interface + comb1 + comb2 + comb3 + comb4

# The sum of the original signal and the comb filters
# feeds two serial allpass filters.
all1 = Allpass(combsum, delay=[0.005, 0.00507], feedback=0.75)
all2 = Allpass(all1, delay=[0.0117, 0.0123], feedback=0.61)

# Brightness control.
lowp = Tone(all2, freq=3500, mul=0.25).out()



s.gui(locals())