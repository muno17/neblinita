from pyo import *
import time
import random

def main():
    # initiate server
    s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for ob-6
    # set the input device
    s.setInputDevice(1) # zoom
    # set the output device
    s.setOutputDevice(2) # headphones: when zoom is used 2 - headphones, 4 - speakers

    # boot server
    s.boot()
    interface = Input().play().out()

    #og_wave = Scope(interface)

    n = Noise()



    # run server with a small gui
    s.start()
    s.gui(locals())


    # If your final output uses less channels than the number of audio streams in an object, don’t 
    # forget to mix it down (call its mix() method) before applying effects on the sum of the signals.







































































if __name__ == "__main__":
    main()