from pyo import *
import random

s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for ob-6
# set the input device
s.setInputDevice(1) # zoom
# set the output device
s.setOutputDevice(2) # headphones: 2 when zoom is used, 0 when not

s.boot()
interface = Input().play().out()



# Distortion parameters
BP_CENTER_FREQ = 400  # Bandpass filter center frequency.
BP_Q = 3  # Bandpass Q (center_freq / Q = bandwidth).
BOOST = 25  # Pre-boost (linear gain).
LP_CUTOFF_FREQ = 3000  # Lowpass filter cutoff frequency.
BALANCE = 0.7  # Balance dry - wet.


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

# Show the transfert function.
table.view(title="Transfert function")

# Bandpass filter and boost gain applied on input signal.
bp = ButBP(interface, freq=BP_CENTER_FREQ, q=BP_Q)
boost = Sig(bp, mul=BOOST)

# Apply the transfert function.
sig = Lookup(table, boost)

# Lowpass filter on the distorted signal.
lp = ButLP(sig, freq=LP_CUTOFF_FREQ, mul=0.7)

# Balance between dry and wet signals.
mixed = Interp(interface, lp, interp=BALANCE)

# Send the signal to the outputs.
out = (mixed * 0.3).out()

s.gui(locals())