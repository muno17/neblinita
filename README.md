# neblina - audio fog machine
#### Video Demo:  <URL HERE>
#### Description:
Using pyo library as a sound engine to create an audio effect processor.
Using PyQt6 library to create the GUI.
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

- trying to eliminate audio dropouts
- implementing a way to stream live sound from an external (ob-6) source - DONE
- customizing the effects and managing gain - DONE
- chaining all the effect together - DONE
- implementing a wet/dry feature - DONE
- creating a GUI DONE
    - dropdowns for interactive I/O
    - knobs for aggregate functions DONE

____________________________

IN PROGRESS

- create a GUI for control and aggregate function knobs 
    - audio I/O - QComboBox for dropdown menu
        - run pa_list_devices() to get a list for inputs and outputs
        - for inputs: regex (r"^(\d*):\s IN, name: (+*),.*$") - gets inputs
        - for outputs: regex (r"^(\d*):\s IN, name: (+*),.*$") - gets outputs
    - create aggregate GUI widgets to control:
        - haze (distortion) knob DONE
            - add distortion to distdelay DONE
        - space knobs (reverb and delay time) UNABLE TO COMPLETE
        - melt (reverb decay) UNABLE TO COMPLETE
        - fractals (harmonic content - chorus / delay frequency)
        - wet/dry knob DONE
            - dry: dry = 1, everything else = 0
            - wet: dry = 0, grimeverbs = .8, lightverbs = 1



______________________________

DONE

- customize distortion parameter DONE
- customize delay1 parameter DONE
- customize delay2 parameter DONE
- customize chorus parameter DONE
- customize reverb parameter DONE
- chain everything together, test different signal paths DONE
- audio routing
    - implement audio output DONE
    - create master mix DONE
        - multiplied output  by .5 to prevent clipping


______________________________

Testing

- don't allow a feedback loop to be created by the computer
    - input of microphone and output of built in speaker not allowed

______________________________
Acknowledgments

- pyo 1.0.4 documentation by AJAX SOUND STUDIO (http://ajaxsoundstudio.com/pyodoc/index.html#)
- PyQt v6.4.1 documentation by River Bank Computing (https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- pythonguis.com PyQt6 tutorials (https://www.pythonguis.com/pyqt6/)