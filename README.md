# **neblinita** - sonic fog machine
#### Video Demo:  <URL HERE>
#### Description:

As a lifelong musician, I have always been intrigued with audio effects such as delays, echos and distortion and how they're able to transform any 
sound into something new.  In particular, I'm quite fond of reverbs and their ability to transport the listener into an immersive space of sonic ambiance.  
For my final project in CS50P, I wanted to use my newly acquired skill of coding in Python to create something that I could use in my daily audio 
explorations; thus, **neblinita** was born.  

**neblinita** is an audio processing unit that adds texture and ambiance to an input audio signal. The basis of neblinita is two flavor of reverbs I 
created, **luz** and **sombra**, which are mixed together with the input signal to create a spacious, beautifully distorted atmosphere: 

**luz** creates harmonic content and a large atmosphere by sending a copy of the input signal through an initial delay which was designed to add echos at 
very short intervals allowing the sound to be drawn out but without the usual noticeable separation in echos found in a traditional delay.  This signal is then fed
into a more traditional delay featuring a large amount of feedback which is separated in lengthy intervals.  The combination of feeding the first delay into the
second delay creates a smooth signal that is then multiplied and repeated over time, creating modulation and adding variance to the signal over time.  This signal is 
then fed into a chorus which adds color by adding harmonic content to the signal.  Since the delayed signal feeding into the chorus is already being modulated with
each repeat, the chorus helps create a massive field of harmonic content since the delay signal is changing in frequency over time.  This new signal is then finally
fed into a large reverb.  A reverb is essentially a large amount of delays repeating very rapidly to give the impression of a sound echoing in a given space.  The 
larger the time of the reverb, the larger the space that is created.  Feeding an already long, heavily delayed signal into a reverb with a long time creates an
incredibly large and deep atmosphere.  The output of **luz** is therefore a very atmospheric, harmonic, psychedelic signal.

**sombra** creates a gritty, chaotic ambiance by heavy use of distortion.  A copy of the input signal is sent through a distortion, overdriving the sound
and creating a fuzzy, dirty output.  This is then sent into a delay similar to the first delay found  in **luz* which smoothens out the sound and adds
length without an audible separation in the sound.  Before the sound is output of this initial delay, the signal is blasted through another distortion, this time
being controlled by the user.  This gnarly signal is then ran through a more traditional delay, adding repeats and chaos to the gnar gnar.  This is finally
fed into a reverb to add a large amount of space and create a dirty, nasty signal giving the listener the impression of getting sent into ***The Void***.

The initial input, also known as the dry signal, is then send to a mixer along with the signal output by **luz** and **sombra**.  These signals are then mixed together
to create the final signal to be output.  A 'wet/dry' feature was implemented to allow the user to control the amount that the signals should be mixed.
When the signal is fully dry, all you hear is the original dry signal.  When the signal is fully wet, you only hear the outputs of **luz** and **sombra**. Setting
the wet/dry anywhere in between fully wet and fully dry will attenuate each output accordingly, allowing the user to mix the dry signal with the effects
of **neblinita** as they see fit. 

I used the Pyo library as the sound engine to create audio effects and to handle all of the audio routing.   
  

I made a simple GUI with the PySimpleGui library.



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
- David Malan and the CS50 team for being such amazing teachers
