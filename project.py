from pyo import *
import time
import random


# initiate server
s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for ob-6
# set the input device
s.setInputDevice(1) # zoom
# set the output device
s.setOutputDevice(2) # headphones

# To be sure that the audio callback will run smoothly all the time, it is better to create all 
# audio objects at the program’s initialization and call their stop(), play(), out() methods when needed.

# boot server
s.boot()
interface = Input().play().out()

# run server with a small gui
s.start()
s.gui(locals())
# Don’t use the Server’s GUI if you don’t need to see the meters or use the volume slider. Instead, you 
# could start the script from command line with -i flag to leave the interpreter alive: $ python -i myscript.py


# If your final output uses less channels than the number of audio streams in an object, don’t 
# forget to mix it down (call its mix() method) before applying effects on the sum of the signals.