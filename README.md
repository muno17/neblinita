# neblina - audio fog machine
#### Video Demo:  <URL HERE>
#### Description:
Using Pyo library as a sound engine to create an audio effect processor.
Using PySimpleGUI library to create the GUI.
____________________________

neblina creates two different flavors of reverbs:

'luz reverb' - creates harmonic content and a large atmosphere

'sombra reverb' - creates a distorted atmosphere

The two reverbs are mixed with the input signal to create a spacious, beautifully distorted atmosphere.

luz reverb
- delay1 for smoothness
- delay2 for ambiance and fractals
- chorus for extra color
- reverb for space

sombra reverb
- distortion for grit
- dist_delay to add additional distortion and to drag out the distorted signal
- dirt_delay to have the distorted signal repeat
- grimeverb to create a distorted space
____________________________

Challenges

- trying to eliminate audio dropouts - UNABLE TO COMPLETE
- implementing a way to stream live sound from an external (ob-6) source - DONE
- customizing the effects and managing gain - DONE
- chaining all the effect together - DONE
- implementing a wet/dry feature - DONE
- creating a GUI DONE
    - knobs for aggregate functions DONE

____________________________

TASKS

- create a GUI for control and aggregate function knobs DONE
    - create aggregate GUI widgets to control: UNABLE TO COMPLETE
        - fog (distortion) knob DONE
            - add distortion to distdelay DONE
        - space knobs (reverb and delay time) UNABLE TO COMPLETE
        - melt (reverb decay) UNABLE TO COMPLETE
        - fractals (harmonic content - chorus / delay frequency) UNABLE TO COMPLETE
        - wet/dry knob DONE
            - dry: dry = 1, everything else = 0
            - wet: dry = 0, grimeverbs = .8, lightverbs = 1
- customize distortion parameter DONE
- customize delay1 parameter DONE
- customize delay2 parameter DONE
- customize chorus parameter DONE
- customize reverb parameter DONE
- chain everything together, test different signal paths DONE
- audio routing DONE
    - implement audio output DONE
    - create master mix DONE
        - multiplied output  by .5 to prevent clipping

______________________________

Testing

- don't allow a feedback loop to be created by the computer
    - input of microphone and output of built in speaker not allowed

______________________________
Acknowledgments

- Pyo by AJAX SOUND STUDIO, documentation (http://ajaxsoundstudio.com/pyodoc/index.html#)
- PySimpleGui, documentation (https://www.pysimplegui.org/en/latest/call%20reference/)
