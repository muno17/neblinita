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
    # dry signal
    interface = Input().out()

    # get buffer
    buftime = s.getBufferSize() / s.getSamplingRate()

    og_wave = Scope(interface)

    n = Noise()

    
    # signal path, wet signal

    #path = harmonizer(interface)
    left, right = delay(interface, buftime)
    left.play().out()
    right.play().out(1)


    # run server with a small gui
    s.start()
    s.gui(locals())


    # If your final output uses less channels than the number of audio streams in an object, don’t 
    # forget to mix it down (call its mix() method) before applying effects on the sum of the signals.




def harmonizer(SIGNAL):
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
    snd = Delay(SIGNAL, delay=ind * wsize, mul=win).mix(1)

    # The transposed signal is sent to the right speaker.
    return snd


def delay(SIGNAL, buftime):
    # Delay parameters
    delay_time_l = Sig(0.5)  # Delay time for the left channel delay.
    delay_time_l.ctrl() # slider
    delay_feed = Sig(0.75)  # Feedback value for both delays.
    delay_feed.ctrl() # slider

    # Because the right delay gets its input sound from the left delay, while
    # it is computed before (to send its output sound to the left delay), it
    # will be one buffer size late. To compensate this additional delay on the
    # right, we substract one buffer size from the real delay time.
    delay_time_r = Sig(delay_time_l, add=-buftime)

    # Initialize the right delay with zeros as input because the left delay
    # does not exist yet.
    right = Delay(Sig(0), delay=delay_time_r)

    # Initialize the left delay with the original mono source and the right
    # delay signal (multiplied by the feedback value) as input.
    left = Delay(SIGNAL + right * delay_feed, delay=delay_time_l)

    # One issue with recursive cross-delay is if we set the feedback to
    # 0, the right delay never gets any signal. To resolve this, we add a
    # non-recursive delay, with a gain that is the inverse of the feedback,
    # to the right delay input.
    original_delayed = Delay(SIGNAL, delay_time_l, mul=1 - delay_feed)

    # Change the right delay input (now that the left delay exists).
    right.setInput(original_delayed + left * delay_feed)


    def playit():
        "Assign a sound to the player and start playback."
        which = random.randint(1, 4)
        path = SIGNAL % which
        #sf.path = path
        signal.play()


    # Call the function "playit" every second.
    pat = Pattern(playit, 1).play()

    return left, right































































if __name__ == "__main__":
    main()