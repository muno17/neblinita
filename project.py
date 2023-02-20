from pyo import *
import time
import random

# initiate server
s = Server()
# set the input device
s.setInputDevice(1)
# set the output device
s.setOutputDevice(2)
# boot server
s.boot()

# To be sure that the audio callback will run smoothly all the time, it is better 
# to create all audio objects at the program’s initialization and call their stop(), 
# play(), out() methods when needed.

# run server with a small gui
s.start()
s.gui(locals())
