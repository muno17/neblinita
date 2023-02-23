# test using built in effects objects

from pyo import *
import time
import random

def main():
    # initiate server
    s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for ob-6
    # set the input device
    s.setInputDevice(1) # zoom
    # set the output device
    s.setOutputDevice(2) # headphones: 2 when zoom is used, 0 when not

    # boot server
    s.boot()
    interface = Input()

    h = Harmonizer(interface).out()
    #distortion
    dist = Disto(h).out()
    #delay
    delay = Delay(dist).out()
    #chorus
    c = Chorus(delay).out()
    #reverb
    reverb = Freeverb(c)


    og_wave = Scope(interface)

    #n = Noise()



    # run server with a small gui
    s.start()
    s.gui(locals())



if __name__ == "__main__":
    main()