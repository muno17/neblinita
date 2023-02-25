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
- compress the master signal
- implementing a wet/dry feature
- creating a GUI
- creating lfos
    - lfo to module shapes of other lfos 
____________________________

TO DO
- create lfos to modulate times in delays,reverbs and chorus
- implement a wet/dry feature
- create aggregate functions
    - input volume control
    - fog (distortion, noise) knob
    - space knob (reverb and delay time)
    - disintegration (reverb decay)
    - haze (harmonic content - chorus / delay frequency)
    - master lfo control
    - wet/dry knob
- create a GUI for control and aggregate function knobs
    - knobs or faders?
    - display signal level
    - audio I/O
    - info bubbles
- implement audio output
    - if one audio output, sum to mono
    - if two audio outputs, output in stereo
    - mix wet and dry signals 
    - create master mix DONE


DONE
- customize distortion parameter DONE
- customize delay1 parameter DONE
- customize delay2 parameter DONE
- customize chorus parameter DONE
- customize reverb parameter DONE
- chain everything together, test different signal paths DONE