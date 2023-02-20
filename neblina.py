from pyo import *
import time


s = Server().boot()



s.start()
# small gui
s.gui(locals())
