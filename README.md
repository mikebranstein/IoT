# About
This is a code repository of all IoT code I've written from my various devices. 

# How to Use
Each IoT device has a dedicated folder in this repo. To get started, clone the repo on to your computer
or IoT device. Specfics on running the code on each device are included below.

To clone the repo:

    > git clone https://github.com/mikebranstein/IoT

## Raspberry Pi

Code in this repo is designed to run on a Raspberry Pi B. I haven't tested it on other models, but I don't see
why it wouldn't work. You may need to modify the pin outs. Each code sample has an accompanying 
[Fritzing](http://http://fritzing.org/) project. Code files are named code.py, and the Fritzing projects 
are named code.fzz.
 
To run the code, clone code, then navigate to the raspberry-pi directory and execute a python script. Be sure to 
wire your Raspberry Pi according to the Fritzing diagram first ;-)

    > git clone https://github.com/mikebranstein/IoT
    > cd IoT
    > cd raspberry-pi
    > python3 led-blink.py
