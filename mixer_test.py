from pyo import *
import time
import random

def main():
    # initiate server
    s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for headphones
    s.amp = 0.2
    # set the input device
    s.setInputDevice(1) # zoom
    # set the output device
    s.setOutputDevice(2) # headphones: when zoom is used 2 - headphones, 4 - speakers

    # boot server
    s.boot()
    # get buffer time
    buftime = s.getBufferSize() / s.getSamplingRate()
    # dry signal
    dry = Input()
    # create copy of input for fog reverb
    wet_path1 = dry
    # create copy of input for light reverb
    wet_path2 = dry

    ### signal chain for fog reverb ###
    distortion_out = distortion(wet_path1)
    left_distdelay, right_distdelay = distdelay(distortion_out, buftime)
    left_dirtdelay, right_dirtdelay = dirtdelay(left_distdelay, right_distdelay, buftime)
    left_gv, right_gv = grimeverb(left_dirtdelay, right_dirtdelay)
    left_grimeverb = (left_gv * .65)
    right_grimeverb = (right_gv * .65)


    ### signal chain for light reverb ###
    delay1_left, delay1_right = delay1(wet_path2, buftime)
    delay2_left, delay2_right = delay2(delay1_left, delay1_right, buftime)
    chorus_left, chorus_right = chorus(delay2_left, delay2_right)
    wet_left, wet_right = reverb(chorus_left, chorus_right)
    left_lightverb = (wet_left * .6)
    right_lightverb = (wet_right * .6)

    ### mixer ###
    master = Mixer(chnls=5, mul=.6)
    master.addInput(0, dry)
    master.addInput(1, left_grimeverb)
    master.addInput(2, right_grimeverb)
    master.addInput(3, left_lightverb)
    master.addInput(4, right_lightverb)
    master.setAmp(0, 0, .25) # dry  - .25 50% wet
    master.setAmp(1, 0, .5) # left_grimeverb - .5 50% wet
    master.setAmp(2, 0, .5) # right_grimeverb - .5 50% wet
    master.setAmp(3, 0, .6) # left_lightverb - .6 50% wet
    master.setAmp(4, 0, .6) # right_lightverb - .6 50% wet
    master.out()


    #master.out()
    
    # run a gui to keep the program running until exit command
    s.start()
    s.gui(timer = False, title="neblina")

    # If your final output uses less channels than the number of audio streams in an object, don’t 
    # forget to mix it down (call its mix() method) before applying effects on the sum of the signals.


def distortion(wet_path1):
    # Distortion parameters
    BP_CENTER_FREQ = 400  # Bandpass filter center frequency.
    BP_Q = 3  # Bandpass Q (center_freq / Q = bandwidth).
    BOOST = 25  # Pre-boost (linear gain).
    LP_CUTOFF_FREQ = 3000  # Lowpass filter cutoff frequency.
    BALANCE = 0.9  # Balance dry - wet.

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

    # Bandpass filter and boost gain applied on input signal.
    bp = ButBP(wet_path1, freq=BP_CENTER_FREQ, q=BP_Q)
    boost = Sig(bp, mul=BOOST)

    # Apply the transfert function.
    sig = Lookup(table, boost)

    # Lowpass filter on the distorted signal.
    lp = ButLP(sig, freq=LP_CUTOFF_FREQ, mul=0.6)

    # Balance between dry and wet signals.
    mixed = Interp(wet_path1, lp, interp=BALANCE)

    return mixed


def distdelay(distortion_out, buftime):
    # Delay parameters
    delay_time_l = Sig(0.08)  # Delay time for the left channel delay.
    delay_feed = Sig(0.3)  # Feedback value for both delays.

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
    left = Delay(distortion_out + right * delay_feed, delay=delay_time_l)

    # One issue with recursive cross-delay is if we set the feedback to
    # 0, the right delay never gets any signal. To resolve this, we add a
    # non-recursive delay, with a gain that is the inverse of the feedback,
    # to the right delay input.
    original_delayed = Delay(distortion_out, delay_time_l, mul=1 - delay_feed)

    # Change the right delay input (now that the left delay exists).
    right.setInput(original_delayed + left * delay_feed)

    return left, right

    
def dirtdelay(left_distdelay, right_distdelay, buftime):
    delay_time_l = Sig(0.3)  # Delay time for the left channel delay.
    delay_feed = Sig(0.8)  # Feedback value for both delays.

    # buffer compensation
    delay_time_r = Sig(delay_time_l, add=-buftime)

    # Initialize the right delay with zeros as input because the left delay
    # does not exist yet.
    right = Delay(Sig(0), delay=delay_time_r)

    # Initialize the left delay with the original mono source and the right
    # delay signal (multiplied by the feedback value) as input.
    left = Delay(left_distdelay + right_distdelay + right * delay_feed, delay=delay_time_l)

    # non-recursive delay fed to right output
    original_delayed = Delay(left_distdelay + right_distdelay, delay_time_l, mul=1 - delay_feed)

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

    lout = (left * .1)
    rout = (right * .1)

    return lout, rout


def grimeverb(left_dirtdelay, right_dirtdelay):
    # The delay times are chosen to be as uncorrelated as possible.
    # Prime numbers are a good choice for delay lengths in samples.
    # left channel
    comb1 = Delay(left_dirtdelay, delay=[0.0997, 0.4277], feedback=0.50)
    comb2 = Delay(left_dirtdelay, delay=[0.7371, 0.0393], feedback=0.65)
    comb3 = Delay(left_dirtdelay, delay=[0.5411, 0.0409], feedback=0.5)
    comb4 = Delay(left_dirtdelay, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_left = left_dirtdelay + comb1 + comb2 + comb3 + comb4

    #right channel
    comb5 = Delay(right_dirtdelay, delay=[0.0997, 0.4277], feedback=0.50)
    comb6 = Delay(right_dirtdelay, delay=[0.7371, 0.0393], feedback=0.65)
    comb7 = Delay(right_dirtdelay, delay=[0.5411, 0.0409], feedback=0.5)
    comb8 = Delay(right_dirtdelay, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_right = right_dirtdelay + comb5 + comb6 + comb7 + comb8

    # The sum of the original signal and the comb filters
    # feeds two serial allpass filters.
    left_all1 = Allpass(combsum_left, delay=[0.005, 0.00507], feedback=0.75)
    left_all2 = Allpass(left_all1, delay=[0.0117, 0.0123], feedback=0.61)
    right_all1 = Allpass(combsum_right, delay=[0.005, 0.00507], feedback=0.75)
    right_all2 = Allpass(right_all1, delay=[0.0117, 0.0123], feedback=0.61)

    # Brightness control.
    left_lowp = Tone(left_all2, freq=3500, mul=0.25)
    right_lowp = Tone(right_all2, freq=3500, mul=0.25)

    return left_lowp, right_lowp


def delay1(wet_path, buftime):
    # Delay parameters
    delay_time_l = Sig(0.1)  # Delay time for the left channel delay.
    #delay_time_l.ctrl() # slider
    delay_feed = Sig(0.6)  # Feedback value for both delays.
    #delay_feed.ctrl() # slider

    # buffer compensation
    delay_time_r = Sig(delay_time_l, add=-buftime)

    # Initialize the right delay with zeros as input because the left delay
    # does not exist yet.
    right = Delay(Sig(0), delay=delay_time_r)

    # Initialize the left delay with the original mono source and the right
    # delay signal (multiplied by the feedback value) as input.
    left = Delay(wet_path + right * delay_feed, delay=delay_time_l)

    # non-recursive delay fed to right output
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


def delay2(delay1_left, delay1_right, buftime):
    # Delay parameters
    delay_time_l = Sig(0.4)  # Delay time for the left channel delay.
    #delay_time_l.ctrl() # slider
    delay_feed = Sig(0.8)  # Feedback value for both delays.
    #delay_feed.ctrl() # slider

    # buffer compensation
    delay_time_r = Sig(delay_time_l, add=-buftime)

    # Initialize the right delay with zeros as input because the left delay
    # does not exist yet.
    right = Delay(Sig(0), delay=delay_time_r)

    # Initialize the left delay with the original mono source and the right
    # delay signal (multiplied by the feedback value) as input.
    left = Delay(delay1_left + delay1_right + right * delay_feed, delay=delay_time_l)

    # non-recursive delay fed to right output
    original_delayed = Delay(delay1_left + delay1_right, delay_time_l, mul=1 - delay_feed)

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

    # Create 8 modulated delay lines with a little feedback
    left_chorus = Delay(delay_left, lfos, feedback=0.3, mul=0.3)
    right_chorus = Delay(delay_right, lfos, feedback=0.4, mul=0.3)

    return left_chorus, right_chorus


def  reverb(chorus_left, chorus_right):
    # The delay times are chosen to be as uncorrelated as possible.
    # Prime numbers are a good choice for delay lengths in samples.
    # left channel
    comb1 = Delay(chorus_left, delay=[0.0997, 0.4277], feedback=0.90)
    comb2 = Delay(chorus_left, delay=[0.7371, 0.0393], feedback=0.85)
    comb3 = Delay(chorus_left, delay=[0.5411, 0.0409], feedback=0.5)
    comb4 = Delay(chorus_left, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_left = chorus_left + comb1 + comb2 + comb3 + comb4

    #right channel
    comb5 = Delay(chorus_right, delay=[0.0997, 0.4277], feedback=0.90)
    comb6 = Delay(chorus_right, delay=[0.7371, 0.0393], feedback=0.85)
    comb7 = Delay(chorus_right, delay=[0.5411, 0.0409], feedback=0.5)
    comb8 = Delay(chorus_right, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_right = chorus_right + comb5 + comb6 + comb7 + comb8

    # The sum of the original signal and the comb filters
    # feeds two serial allpass filters.
    left_all1 = Allpass(combsum_left, delay=[0.005, 0.00507], feedback=0.75)
    left_all2 = Allpass(left_all1, delay=[0.0117, 0.0123], feedback=0.61)
    right_all1 = Allpass(combsum_right, delay=[0.005, 0.00507], feedback=0.75)
    right_all2 = Allpass(right_all1, delay=[0.0117, 0.0123], feedback=0.61)

    # Brightness control.
    left_lowp = Tone(left_all2, freq=3500, mul=0.25)
    right_lowp = Tone(right_all2, freq=3500, mul=0.25)

    return left_lowp, right_lowp



if __name__ == "__main__":
    main()