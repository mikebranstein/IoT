# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!
 
import RPi.GPIO as GPIO, time, os      
 
DEBUG = 1
GPIO.setmode(GPIO.BOARD)
 
def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading
 
#loop until keyboard interrupt
try:
    while True:
        # Read RC timing using pin #12
        print(RCtime(12))
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()