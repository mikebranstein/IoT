# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!
 
import RPi.GPIO as GPIO, time, os, sys    
import datetime
import iothub_client
from iothub_client import *
  
GPIO.setmode(GPIO.BOARD)

timeout = 241000
minimumPollingTime = 9
receiveContext = 0

# transport protocol
Protocol = IoTHubTransportProvider.HTTP

# String containing Hostname, Device Id & Device Key in the format:
# "HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>"
connectionString = "[device connection string]"

msgTxt = "{\"deviceId\": \"RPi\",\"timestamp\": \"%s\",\"lightReading\": %d}"

def receive_message_callback(message, counter):
    print ("Received Message.")
    return IoTHubMessageDispositionResult.ACCEPTED


def send_confirmation_callback(message, result, userContext):
    print ("Confirmation[%d] received for message with result = %s" % (userContext, result))

def iothub_client_init():
    # prepare iothub client
    iotHubClient = IoTHubClient(connectionString, Protocol)
    if iotHubClient.protocol == IoTHubTransportProvider.HTTP:
        iotHubClient.set_option("timeout", timeout)
        iotHubClient.set_option("MinimumPollingTime", minimumPollingTime)
    iotHubClient.set_message_callback(receive_message_callback, receiveContext)
    return iotHubClient
 
 
def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
        if (reading >= 1000000):
            break
    return reading
 
#loop until keyboard interrupt
try:

    iotHubClient = iothub_client_init()
        
    while True:
        # Read RC timing using pin #12
        lightReading = RCtime(12)
        timestamp = datetime.datetime.now()

        msgTxtFormatted = msgTxt % (timestamp, lightReading)
        message = IoTHubMessage(msgTxtFormatted)

        iotHubClient.send_event_async(
            message, send_confirmation_callback, 0)
        print ("IoTHubClient.send_event_async accepted message for transmission to IoT Hub: %s" % msgTxtFormatted)
                
        time.sleep(30)
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()