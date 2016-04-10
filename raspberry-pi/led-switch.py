import RPi.GPIO as GPIO
import time

# tell GPIO to use the Pi's board numbering for pins
GPIO.setmode(GPIO.BOARD)

redLedPin = 22
switchPin = 18

# set data direction of LED pin to output
GPIO.setup(redLedPin, GPIO.OUT)
GPIO.setup (switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    if GPIO.input(switchPin):
        GPIO.output(redLedPin, GPIO.LOW)
        print('Button not pressed.')
    else:
        GPIO.output(redLedPin, GPIO.HIGH)
        print('Button pressed.')
    time.sleep(0.2)
    return

#loop until keyboard interrupt
try:
    while True:
        loop()
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()