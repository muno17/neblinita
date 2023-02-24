# neblina - audio fog machine
#### Video Demo:  <URL HERE>
#### Description:
Using pyo library as a sound engine to create an audio effect processor.

fog reverb
- distortion for grit
- dist_delay to make distortion sound longer
- dirt_delay to have the distorted signal repeat
- grimeverb to create a distorted atmosphere

light reverb
- delay1 for smoothness
- delay2 for ambiance and fractals
- chorus for extra color
- reverb for ambiance and space

Challenges
- learning DSP
- implementing a way to stream live sound from an external (ob-6) source - DONE
- chaining all the effect together - DONE
- implementing a wet/dry feature
- creating a GUI
- creating lfos
    - lfo to module shapes of other lfos 

TO DO
- customize noise parameter
- customize distortion parameter DONE
- customize delay1 parameter DONE
- customize delay2 parameter DONE
- customize chorus parameter DONE
- customize reverb parameter DONE
- chain everything together, test different signal paths DONE
- implement a wet/dry feature
- create aggregate functions
    - input volume control
    - fog (distortion, noise) knob
    - space knob (reverb and delay time)
    - disintegration (reverb decay)
    - haze (harmonic content - chorus / delay frequency)
    - master lfo control
    - wet/dry knob
- create a GUI for aggregate functions
- implement audio output
    - if one audio output, sum to mono
    - if two audio outputs, output in stereo
    - mix wet and dry signals 
    - create master mix
