import RPi.GPIO as GPIO
import time

# tell GPIO to use the Pi's board numbering for pins
GPIO.setmode(GPIO.BOARD)

redLedPin = 22
switchPin = 18
ledOn = False
prevSwitchPressed = False

# set data direction of LED pin to output
GPIO.setup(redLedPin, GPIO.OUT)
GPIO.setup (switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def loop():
    curSwitchPressed = GPIO.input(switchPin)

    # do nothing if switch state has not changed    
    if curSwitchPressed == prevSwitchPressed:
        return
        
    prevSwitchPressed = curSwitchPressed
    
    if curSwitchPressed:
        if ledOn:
            GPIO.output(redLedPin, GPIO.LOW)
            ledOn = False
        else:
            GPIO.output(redLedPin, GPIO.HIGH)
            ledOn = True
    
    return

#loop until keyboard interrupt
try:
    while True:
        loop()
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()