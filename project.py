from pyo import *
import time
import random
import sys
import PySimpleGUI as sg


def main():

    ### create the gui window ###
    sg.theme('DarkGrey4')
    layout = [[sg.Text('neblina', font=('Monaco', 30), pad=(5,5)), sg.Text('  muno audio', font=('Monaco', 12))],
            [sg.Slider((0.00,1.00), key='-WET_DRY-', default_value=0, orientation='v', resolution=.01, tick_interval=.5, enable_events=True, disable_number_display=True, pad=(15,0), border_width=2, font='Monaco'),
            sg.Slider((0.00,1.00), key='-HAZE-', default_value=0, orientation='v', resolution=.01, tick_interval=.5, enable_events=True, disable_number_display=True, border_width=2, pad=(15,0), font='Monaco')],
            [sg.Text(text='   wet/dry', font='Monaco'), sg.Text(text='   haze', font='Monaco'),]]

    ### initiate pyo server ###
    s = Server(nchnls=1) # nchnls defaults to 2 channel output, changed to 1 for headphones
    s.amp = 0.2
    # set the input device
    s.setInputDevice(1)
    # set the output device
    s.setOutputDevice(2)

    # boot server and start
    s.boot().start()
    # get buffer time
    buftime = bufculator(s.getBufferSize(), s.getSamplingRate())
    # dry signal
    dry = Input()
    # create copy of input for fog reverb
    wet_path1 = dry
    # create copy of input for light reverb
    wet_path2 = dry

    # start gui window
    window = sg.Window('neblina', layout)

    ### signal chain for luz reverb ###
    delay1_left, delay1_right = delay1(wet_path2, buftime)
    delay2_left, delay2_right = delay2(delay1_left, delay1_right, buftime)
    chorus_left, chorus_right = chorus(delay2_left, delay2_right)
    wet_left, wet_right = reverb(chorus_left, chorus_right)
    left_lightverb = (wet_left * .6)
    right_lightverb = (wet_right * .6)
    
    ### start sombra signal path
    distortion_out = distortion(wet_path1)

    ### gui event loop ###
    while True:
        try:
            event, values = window.read()

            # signal path for sombra delay
            # -HAZE- controls distortion added to distdelay
            left_distdelay, right_distdelay = distdelay(distortion_out, buftime, values['-HAZE-'])
            left_dirtdelay, right_dirtdelay = dirtdelay(left_distdelay, right_distdelay, buftime)
            left_gv, right_gv = grimeverb(left_dirtdelay, right_dirtdelay)
            left_grimeverb = (left_gv * .5)
            right_grimeverb = (right_gv * .5)

            # -WET_DRY- controls wet/dry value
            mix = Mixer(chnls=5, mul=.55)
            mix.addInput(0, dry)
            mix.addInput(1, left_grimeverb)
            mix.addInput(2, right_grimeverb)
            mix.addInput(3, left_lightverb)
            mix.addInput(4, right_lightverb)
            mix.setAmp(0, 0, (1 - values['-WET_DRY-']))
            mix.setAmp(1, 0, values['-WET_DRY-'])
            mix.setAmp(2, 0, values['-WET_DRY-'])
            mix.setAmp(3, 0, values['-WET_DRY-'])
            mix.setAmp(4, 0, values['-WET_DRY-'])
            mix.out()

            if event is None:
                break
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == 'Show':
                sg.popup(f'The slider value = {values["-SLIDER-"]}')
        except TypeError:
            break

    s.stop()    
    window.close()
    

def bufculator(buftime, samplerate):
    return buftime / samplerate


def distortion(wet_path1):
    # Distortion parameters
    BP_CENTER_FREQ = 400  # Bandpass filter center frequency.
    BP_Q = 3  # Bandpass Q (center_freq / Q = bandwidth).
    BOOST = 25  # Pre-boost (linear gain).
    LP_CUTOFF_FREQ = 3000  # Lowpass filter cutoff frequency.
    BALANCE = 0.9  # Balance dry - wet.

    # transfert function
    table = ExpTable([(0, -0.25), (4096, 0), (8192, 0)], exp=30)
    high_table = ExpTable([(0, 1), (2000, 1), (4096, 0), (4598, 0), (8192, 0)], exp=5, inverse=False)
    high_table.reverse()
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


def distdelay(distortion_out, buftime, haze):
    delay_time_l = Sig(0.08)  # Delay time for the left channel delay.
    delay_feed = Sig(0.3)  # Feedback value for both delays.
    delay_time_r = Sig(delay_time_l, add=-buftime)
    right = Delay(Sig(0), delay=delay_time_r)
    left = Delay(distortion_out + right * delay_feed, delay=delay_time_l)
    original_delayed = Delay(distortion_out, delay_time_l, mul=1 - delay_feed)
    right.setInput(original_delayed + left * delay_feed)

    # apply distortion  to delayed signal
    dleft = Disto(left, drive=0.0, slope=.8)
    dright = Disto(left, drive=0.0, slope=.8)

    dleft.setDrive(haze) # distortion drive controlled by haze
    dright.setDrive(haze) # distortion drive controlled by haze

    return dleft, dright

    
def dirtdelay(left_distdelay, right_distdelay, buftime):
    delay_time_l = Sig(0.3)  # Delay time for the left channel delay.
    delay_feed = Sig(0.8)  # Feedback value for both delays.
    delay_time_r = Sig(delay_time_l, add=-buftime)
    right = Delay(Sig(0), delay=delay_time_r)
    left = Delay(left_distdelay + right_distdelay + right * delay_feed, delay=delay_time_l)
    original_delayed = Delay(left_distdelay + right_distdelay, delay_time_l, mul=1 - delay_feed)
    right.setInput(original_delayed + left * delay_feed)

    lout = (left * .1)
    rout = (right * .1)

    return lout, rout


def grimeverb(left_dirtdelay, right_dirtdelay):
    # left channel
    comb1 = Delay(left_dirtdelay, delay=[0.0997, 0.4277], feedback=0.50)
    comb2 = Delay(left_dirtdelay, delay=[0.7371, 0.0393], feedback=0.65)
    comb3 = Delay(left_dirtdelay, delay=[0.5411, 0.0409], feedback=0.5)
    comb4 = Delay(left_dirtdelay, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_left = left_dirtdelay + comb1 + comb2 + comb3 + comb4

    # right channel
    comb5 = Delay(right_dirtdelay, delay=[0.0997, 0.4277], feedback=0.50)
    comb6 = Delay(right_dirtdelay, delay=[0.7371, 0.0393], feedback=0.65)
    comb7 = Delay(right_dirtdelay, delay=[0.5411, 0.0409], feedback=0.5)
    comb8 = Delay(right_dirtdelay, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_right = right_dirtdelay + comb5 + comb6 + comb7 + comb8

    # The sum of the original signal and the comb filters
    # feeds two serial allpass filters.
    left_all1 = Allpass(combsum_left, delay=[0.005, 0.00507], feedback=0.075)
    left_all2 = Allpass(left_all1, delay=[0.0117, 0.0123], feedback=0.61)
    right_all1 = Allpass(combsum_right, delay=[0.005, 0.00507], feedback=0.75)
    right_all2 = Allpass(right_all1, delay=[0.0117, 0.0123], feedback=0.61)

    # Brightness control.
    left_lowp = Tone(left_all2, freq=3500, mul=0.25)
    right_lowp = Tone(right_all2, freq=3500, mul=0.25)

    return left_lowp, right_lowp


def delay1(wet_path, buftime):
    delay_time_l = Sig(0.1)  # Delay time for the left channel delay.
    delay_feed = Sig(0.6)  # Feedback value for both delays.
    delay_time_r = Sig(delay_time_l, add=-buftime)
    right = Delay(Sig(0), delay=delay_time_r)
    left = Delay(wet_path + right * delay_feed, delay=delay_time_l)
    original_delayed = Delay(wet_path, delay_time_l, mul=1 - delay_feed)
    right.setInput(original_delayed + left * delay_feed)

    return left, right


def delay2(delay1_left, delay1_right, buftime):
    delay_time_l = Sig(0.4)  # Delay time for the left channel delay.
    delay_feed = Sig(0.8)  # Feedback value for both delays.
    delay_time_r = Sig(delay_time_l, add=-buftime)
    right = Delay(Sig(0), delay=delay_time_r)
    left = Delay(delay1_left + delay1_right + right * delay_feed, delay=delay_time_l)
    original_delayed = Delay(delay1_left + delay1_right, delay_time_l, mul=1 - delay_feed)
    right.setInput(original_delayed + left * delay_feed)

    return left, right


def chorus(delay_left, delay_right):
    freqs = [0.254, 0.465, 0.657, 0.879, 1.23, 1.342, 1.654, 1.879]
    cdelay = [0.0087, 0.0102, 0.0111, 0.01254, 0.0134, 0.01501, 0.01707, 0.0178]
    adelay = [0.001, 0.0012, 0.0013, 0.0014, 0.0015, 0.0016, 0.002, 0.0023]
    lfos = Sine(freqs, mul=adelay, add=cdelay)
    left_chorus = Delay(delay_left, lfos, feedback=0.3, mul=0.3)
    right_chorus = Delay(delay_right, lfos, feedback=0.4, mul=0.3)

    return left_chorus, right_chorus


def  reverb(chorus_left, chorus_right):
    # left channel
    comb1 = Delay(chorus_left, delay=[0.0997, 0.4277], feedback=0.90)
    comb2 = Delay(chorus_left, delay=[0.7371, 0.0393], feedback=0.85)
    comb3 = Delay(chorus_left, delay=[0.5411, 0.0409], feedback=0.5)
    comb4 = Delay(chorus_left, delay=[0.1137, 0.7155], feedback=0.73)

    combsum_left = chorus_left + comb1 + comb2 + comb3 + comb4

    # right channel
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