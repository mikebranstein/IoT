# blinks 3 LED at the same time, in parallel
import RPi.GPIO as GPIO
import time
    
def blinkThree(redLedPin, blueLedPin, greenLedPin):
    GPIO.output(redLedPin, GPIO.HIGH)
    GPIO.output(blueLedPin, GPIO.HIGH)
    GPIO.output(greenLedPin, GPIO.HIGH)

    time.sleep(1)

    GPIO.output(redLedPin, GPIO.LOW)
    GPIO.output(blueLedPin, GPIO.LOW)
    GPIO.output(greenLedPin, GPIO.LOW)

    time.sleep(1)
  
# tell GPIO to use the Pi's board numbering for pins
GPIO.setmode(GPIO.BOARD)

redLedPin = 22
blueLedPin = 18
greenLedPin = 16

# set data direction of LED pin to output
GPIO.setup(redLedPin, GPIO.OUT)
GPIO.setup(blueLedPin, GPIO.OUT)
GPIO.setup(greenLedPin, GPIO.OUT)

# loop until keyboard interrupt

try:
    while True:
        blinkThree(redLedPin, blueLedPin, greenLedPin)
except KeyboardInterrupt:
    pass

GPIO.cleanup()