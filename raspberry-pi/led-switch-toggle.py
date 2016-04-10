import RPi.GPIO as GPIO
import time

# tell GPIO to use the Pi's board numbering for pins
GPIO.setmode(GPIO.BOARD)

redLedPin = 22
switchPin = 18
toggler = new SwitchToggler(switchPin, redLedPin)

# set data direction of LED pin to output

# simple class that toggles the output value of the outputPin (HIGH/LOW)
# by pressing the switch on switchInputPin
#
# to use, instantiate and call the toggle() method in your loop
class SwitchToggler:
    prevSwitchPressed = False
    outputPinOn = False
    def __init__(self, switchInputPin, outputPin):
        self.switchInputPin = switchInputPin
        self.outputPin = outputPin
        GPIO.setup (switchInputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(outputPin, GPIO.OUT)
    
    def toggle():
        curSwitchPressed = not GPIO.input(self.switchInputPin)
        
        # do nothing if switch state has not changed    
        if curSwitchPressed == prevSwitchPressed:
            return
            
        self.prevSwitchPressed = curSwitchPressed
        
        if curSwitchPressed:
            if self.outputPinOn:
                GPIO.output(self.outputPin, GPIO.LOW)
                self.outputPinOn = False
            else:
                GPIO.output(self.outputPin, GPIO.HIGH)
                self.outputPinOn = True
                
        return
       
    

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