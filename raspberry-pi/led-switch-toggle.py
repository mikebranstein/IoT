import RPi.GPIO as GPIO
import lib.switchtoggle as Toggle
import time

# tell GPIO to use the Pi's board numbering for pins
GPIO.setmode(GPIO.BOARD)

redLedPin = 22
switchPin = 18
toggler = Toggle.SwitchToggler(switchPin, redLedPin)

def loop():
    global toggler
    toggler.toggle()
    
    return

#loop until keyboard interrupt
try:
    while True:
        loop()
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()