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

____________________

I used the Pyo library to handle all of the audio routing:

**Within the project folder is a program I created named 'audio_io.py'. Running this program before starting the main program is essential to assure that your audio will** 
**be routed correctly and to ensure that audio feedback loops won't be created (trust me you do not want this to happen for the sake of your ears).** audio_io.py will output 
information pertaining to the audio inputs and outputs of your computer.  In particular, we want to pay special attention to the 'default input' and 'default output' at the 
bottom.  You will want these to match the desired devices listed in the 'AUDIO devices' section above.  For example, I want to input signal into my computer through my
Zoom H4N Pro recorder and be able to listen through my headphones that I have plugged into my computer.  When I run audio_io.py, my 'AUDIO devices' and default i/o
are listed as:

>0: OUT, name: H4, host api index: 0, default sr: 48000 Hz, latency: 0.004354 s

>1: IN, name: H4, host api index: 0, default sr: 44100 Hz, latency: 0.005896 s

>2: OUT, name: External Headphones, host api index: 0, default sr: 44100 Hz, latency: 0.006213 s

>3: IN, name: MacBook Pro Microphone, host api index: 0, default sr: 48000 Hz, latency: 0.033687 s

>4: OUT, name: MacBook Pro Speakers, host api index: 0, default sr: 44100 Hz, latency: 0.009229 s

>5: IN, name: Microsoft Teams Audio, host api index: 0, default sr: 48000 Hz, latency: 0.010000 s

>5: OUT, name: Microsoft Teams Audio, host api index: 0, default sr: 48000 Hz, latency: 0.001333 s
>
> default input: 1

> default output: 2

In this example, the defaults are already set for where I would like to input and output the audio.  In the main Project.py file I would then go to line 22 and enter in the 
correct input and output numbers, 1 for the input and 2 for the output in this case:

 >   s.setInputDevice(1)

 >   s.setOutputDevice(2)

**'******'MAKE SURE THAT THE INPUT AND OUTPUT COMBINATION IS NEVER INPUT - INTERNAL MICROPHONE (3 in the example above) AND OUTPUT - INTERNAL SPEAKERS (4 in the example above).**
**THIS WILL CREATE AN AUDIO FEEDBACK LOOP SINCE THE BUILD IN MICROPHONE WILL PICK UP ANYTHING COMING OUT OF THE INTERNAL SPEAKERS, CREATING AN INFINITE LOOP OF EVER**
**EXPANDING PAIN TO YOUR EARS.  IF YOU DO THIS BY ACCIDENT THEN EXIT THE PROGRAM IMMEDIATELY TO AVOID EAR DAMAGE'******'**

______________________

I also used the Pyo library for the sound engine.  

I knew very little about digital signal processing (DSP) going into this project so I thoroughly read through all of the Pyo documentation to try and get a grasp on the subject, 
or least enough to be able to build this project.  The general concept is that pyo creates a 'server' where all the audio runs through.  Within this server, you run operations on
'pyo objects' which are essentially classes pertaining to each component of an audio system.  **neblina** was designed to take in an audio signal and then create two copies of that signal.  Each signal is then fed through the processes described in the first segment of this ReadMe.  

The pyo documentation lists effect types in two ways.  The first is in a 
simple function call, such as Disto() to apply distortion to an effect.  These functions seemed tempting to use because of their ease of use but they don't allow for much customization.  The second is by presenting broken down bare-bones functions of different effects. These templates (for example, http://ajaxsoundstudio.com/pyodoc/examples/07-effects/03-fuzz-disto.html for distortion) show you the basic building blocks that make up a certain type of effect.  From these templates you're then able to make your own modifications and add/remove functions as you see fit.  I took this latter approach for all of my effects since I wanted something fully customizable to my liking that would sound like the idea I had in my head when I first thought of making this project.  This of course took a lot of experimentation since I'm a DSP noob but, after a lot of trial and error, I finished customizing all of my effects exactly
how I wanted them to function.  After creating these effects, I chained them all together by creating return values (pyo objects) for each effect which I would then assign and then send through the next effect.  After running through each chain, the final reverb effect of both **luz** and **sombra** returns a pyo object containing the final output of each signal chain.

The pyo objects for **luz** and  **sombra** are then summed in a Mixer object along with the initial dry signal.  This again took a lot of experimentation to get the output levels
of each effect to a proper level so as to not output a signal so loud that it would cause audio dropouts and damage speakers/headphones.  The method I used was to attenuate each signal
with a float value between 0.0 and 1.0.  The output for the input signal combined with **luz** and **sombra** would then max out between  -15 to -5 db depending on the level of the 
initial signal.  This of course doesn't factor in devious individuals who are out to make speakers and eardrums explode by sending very loud input signal but in this case, and the way
the majority of virtual effects processors work, we assume the user is a rational well-intended person.  I also created a wet/dry function that calculates new attenuation levels based
on how wet or dry the user wants the signal to be.  This is all then output and the result is a glorious wave of distorted space and sound.

______________________

I created a simple GUI using the PySimpleGui library.

I initially attempted to create 





______________________________
Acknowledgments

- Pyo by AJAX SOUND STUDIO, documentation (http://ajaxsoundstudio.com/pyodoc/index.html#)
- PySimpleGui, documentation (https://www.pysimplegui.org/en/latest/call%20reference/)
- David Malan and the CS50 team for being such amazing teachers
- my ears for dealing with many unintended sounds while I was testing this project
