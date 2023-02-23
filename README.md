# neblina - Audio Effects Plugin
#### Video Demo:  <URL HERE>
#### Description:
Using pyo library as a sound engine to create an audio effect processor.

- harmonizer to add harmonic content
- noise for a bit of dirt
- distortion for real grit
- filter for "darkness"
- delay for ambiance and fractals
- chorus for extra color
- filter for more "darkness"
- reverb for ambiance and space

Challenges
- learning DSP
- implementing a way to stream live sound from an external (ob-6) source
- chaining all the effect together
- implementing a wet/dry feature
- creating a GUI
- creating lfos
    - lfo to module shapes of other lfos 

TO DO
- customize harmonizer parameter
- customize noise parameter
- customize distortion parameter
- customize filter1 parameter
- customize delay parameter
- customize chorus parameter
- customize filter2 parameter
- customize reverb parameter
- chain everything together, test different signal paths
- implement a wet/dry feature
- create aggregate functions
    - input volume control
    - fog (distortion, noise) knob
    - filter1 freq)
    - space knob (reverb and delay time)
    - disintegration (reverb decay)
    - haze (harmonic content - harmonizer, chorus / delay frequency)
    - filter2
    - master lfo control
    - wet/dry knob
- create a GUI for aggregate functions
- implement audio output
    - if one audio output, sum to mono
    - if two audio outputs, output in stereo
    - mix wet and dry signals
