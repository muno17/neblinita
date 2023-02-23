from pyo import *
import time
import random

def main():
    # initiate server
    s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for headphones
    # set the input device
    s.setInputDevice(1) # zoom
    # set the output device
    s.setOutputDevice(2) # headphones: 2 when zoom is used, 0 when not

    # boot server
    s.boot()
    # dry signal
    interface = Input()
    wet_path = interface

    #output dry signal
    interface.play().out()

    # get buffer
    buftime = s.getBufferSize() / s.getSamplingRate()

    og_wave = Scope(interface)

    n = Noise()

    
    # signal path for wet signal

    harmonizer_out = harmonizer(wet_path)
    #harmonizer_out.out()  ###DECIDE IF WE WANT THIS ON OR NOT###
    delay_left, delay_right = delay(harmonizer_out, buftime)###DECIDE IF WE WANT HARMONIZER GOING IN OR NOT###
    #delay_left.play().out()  #----- delay left channel
    #delay_right.play().out(1) #----- delay right channel
    chorus_left, chorus_right = chorus(delay_left, delay_right)
    chorus_left.play().out() #---- chorus left channel
    chorus_right.play().out() #---- chorus right channel




    # run server with a small gui
    s.start()
    s.gui(locals())

    # If your final output uses less channels than the number of audio streams in an object, don’t 
    # forget to mix it down (call its mix() method) before applying effects on the sum of the signals.

def harmonizer(wet_path):
    # Half-sine window used as the amplitude envelope of the overlaps.
    env = WinTable(8)

    # Length of the window in seconds.
    wsize = 0.3

    # Amount of transposition in semitones.
    trans = -7

    # Compute the transposition ratio.
    ratio = pow(2.0, trans / 12.0)

    # Compute the reading head speed.
    rate = -(ratio - 1) / wsize

    # Two reading heads out-of-phase.
    ind = Phasor(freq=rate, phase=[0, 0.5])

    # Each head reads the amplitude envelope...
    win = Pointer(table=env, index=ind, mul=0.9)

    # ... and modulates the delay time (scaled by the window size) of a delay line.
    # mix(1) is used to mix the two overlaps on a single audio stream.
    snd = Delay(wet_path, delay=ind * wsize, mul=win).mix(1)

    # The transposed signal is sent to the right speaker.
    return snd


def delay(wet_path, buftime):
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
    left = Delay(wet_path + right * delay_feed, delay=delay_time_l)

    # One issue with recursive cross-delay is if we set the feedback to
    # 0, the right delay never gets any signal. To resolve this, we add a
    # non-recursive delay, with a gain that is the inverse of the feedback,
    # to the right delay input.
    original_delayed = Delay(wet_path, delay_time_l, mul=1 - delay_feed)

    # Change the right delay input (now that the left delay exists).
    right.setInput(original_delayed + left * delay_feed)


    def playit():
        "Assign a sound to the player and start playback."
        which = random.randint(1, 4)
        path = wet_path % which
        #sf.path = path
        signal.play()


    # Call the function "playit" every second.
    pat = Pattern(playit, 1).play()

    return left, right


def chorus(delay_left, delay_right):
    # Sets values for 8 LFO'ed delay lines (you can add more if you want!).
    # LFO frequencies.
    freqs = [0.254, 0.465, 0.657, 0.879, 1.23, 1.342, 1.654, 1.879]
    # Center delays in seconds.
    cdelay = [0.0087, 0.0102, 0.0111, 0.01254, 0.0134, 0.01501, 0.01707, 0.0178]
    # Modulation depths in seconds.
    adelay = [0.001, 0.0012, 0.0013, 0.0014, 0.0015, 0.0016, 0.002, 0.0023]

    # Create 8 sinusoidal LFOs with center delays "cdelay" and depths "adelay".
    lfos = Sine(freqs, mul=adelay, add=cdelay)

    # Create 8 modulated delay lines with a little feedback and send the signals
    # to the output. Streams 1, 3, 5, 7 to the left and streams 2, 4, 6, 8 to the
    # right (default behaviour of the out() method).
    left_chorus = Delay(delay_left, lfos, feedback=0.3, mul=0.3)
    right_chorus = Delay(delay_right, lfos, feedback=0.4, mul=0.3)

    return left_chorus, right_chorus





























































if __name__ == "__main__":
    main()