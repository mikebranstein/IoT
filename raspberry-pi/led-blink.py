import RPi.GPIO as GPIO
import time

def blink(ledPin):
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(1)
    return
    
# tell GPIO to use the Pi's board numbering for pins
GPIO.setmode(GPIO.BOARD)

redLedPin = 22

# set data direction of LED pin to output
GPIO.setup(redLedPin, GPIO.OUT)

blink(redLedPin)

GPIO.cleanup()