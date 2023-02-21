from pyo import *
import random

s = Server(nchnls=1) # nchnles defaults to 2 channel output, changed to 1 for ob-6
# set the input device
s.setInputDevice(1) # zoom
# set the output device
s.setOutputDevice(2) # headphones: 2 when zoom is used, 0 when not

s.boot()
interface = Input().play().out()

# Compute the duration, in seconds, of one buffer size.
buftime = s.getBufferSize() / s.getSamplingRate()

# Delay parameters
delay_time_l = Sig(0.125)  # Delay time for the left channel delay.
delay_time_l.ctrl()
delay_feed = Sig(0.75)  # Feedback value for both delays.
delay_feed.ctrl()

# Because the right delay gets its input sound from the left delay, while
# it is computed before (to send its output sound to the left delay), it
# will be one buffer size late. To compensate this additional delay on the
# right, we substract one buffer size from the real delay time.
delay_time_r = Sig(delay_time_l, add=-buftime)


# Send the original sound to both speakers.
interface_out = interface.mix(2).out()

# Initialize the right delay with zeros as input because the left delay
# does not exist yet.
right = Delay(Sig(0), delay=delay_time_r).out(1)

# Initialize the left delay with the original mono source and the right
# delay signal (multiplied by the feedback value) as input.
left = Delay(interface + right * delay_feed, delay=delay_time_l).out()

# One issue with recursive cross-delay is if we set the feedback to
# 0, the right delay never gets any signal. To resolve this, we add a
# non-recursive delay, with a gain that is the inverse of the feedback,
# to the right delay input.
original_delayed = Delay(interface, delay_time_l, mul=1 - delay_feed)

# Change the right delay input (now that the left delay exists).
right.setInput(original_delayed + left * delay_feed)


def playit():
    "Assign a sound to the player and start playback."
    which = random.randint(1, 4)
    path = interface % which
    #sf.path = path
    interface.play()


# Call the function "playit" every second.
pat = Pattern(playit, 1).play()


s.gui(locals())