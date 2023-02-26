# neblina - audio fog machine
#### Video Demo:  <URL HERE>
#### Description:
Using pyo library as a sound engine to create an audio effect processor.
Using PyQt6 library to create the GUI.
____________________________

neblina creates two different flavors of reverbs:

'light reverb' - creates harmonic content and a large atmosphere

'fog reverb' - creates a distorted atmosphere

The two reverbs are mixed with the input signal to create a spacious, beautifully distorted atmosphere.

light reverb
- delay1 for smoothness
- delay2 for ambiance and fractals
- chorus for extra color
- reverb for space

fog reverb
- distortion for grit
- dist_delay to make distortion sound longer
- dirt_delay to have the distorted signal repeat
- grimeverb to create a distorted space
____________________________

Challenges


- implementing a way to stream live sound from an external (ob-6) source - DONE
- chaining all the effect together - DONE
- implementing a wet/dry feature
- creating a GUI
    - dropdowns for interactive I/O
    - knobs for aggregate functions
    - signal output visualizer and control
    - info bubbles for each widget giving brief explanation
____________________________

IN PROGRESS

- create a GUI for control and aggregate function knobs
    - knobs or faders? - QDial, QSlider
    - display signal level - QProgressBar
        - be able to control
        - displays decibel level, similar to ableton
    - audio I/O - QComboBox for dropdown menu
        - run pa_list_devices() to get a list for inputs and outputs
        - for inputs: regex (r"^(\d*):\s IN, name: (+*),.*$") - gets inputs
        - for outputs: regex (r"^(\d*):\s IN, name: (+*),.*$") - gets outputs


- create aggregate GUI widgets to control:
    - fog (distortion, noise) knob
        - add noise to distorted signal
    - space knob (reverb and delay time)
    - disintegrate (reverb decay)
    - fractals (harmonic content - chorus / delay frequency)
    - wet/dry knob
        - dry: dry = 1, everything else = 0
        - wet: dry = 0, grimeverbs = .8, lightverbs = 1
        - use Balance(input, input2, freq) ???
        OR
        - control dry, wet_path1, wet_path2 signals


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
Acknowledgments

- pyo 1.0.4 documentation by AJAX SOUND STUDIO (http://ajaxsoundstudio.com/pyodoc/index.html#)
- PyQt v6.4.1 documentation by River Bank Computing (https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- pythonguis.com PyQt6 tutorials (https://www.pythonguis.com/pyqt6/)