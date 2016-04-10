import RPi.GPIO as GPIO
import time

# tell GPIO to use the Pi's board numbering for pins
GPIO.setmode(GPIO.BOARD)

redLedPin = 22
switchPin = 18

# set data direction of LED pin to output
GPIO.setup(redLedPin, GPIO.OUT)
GPIO.setup (switchPin, GPIO.IN)

def loop():
    if GPIO.input(switchPin):
        GPIO.output(redLedPin, GPIO.LOW)
    else:
        GPIO.output(redLedPin, GPIO.HIGH)
    return

#loop until keyboard interrupt
try:
    while True:
        loop()
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()