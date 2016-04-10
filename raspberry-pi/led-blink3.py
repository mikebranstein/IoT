import RPi.GPIO as GPIO
import time

def blink(ledPin, onTime, offTime):
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(onTime)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(offTime)
    return
    
def blinkThree(redLedPin, blueLedPin, greenLedPin):
    blink(redLedPin, 1, 0)
    blink(blueLedPin, 1, 0)
    blink(greenLedPin, 1, 0)
  
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