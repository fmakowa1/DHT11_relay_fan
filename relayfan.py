"""
------HOMEWORK IOT APPLICATION DESIGN---------- 
This code checks temperature from DHT11 sensor and then turns on the fan once its above
the threshold.
********* (Created by Fula-11) ***********

-------*REFERENCES*-------------
https://www.instructables.com/Automated-cooling-fan-for-Pi/
https://iotdesignpro.com/projects/how-to-send-sensor-data-to-ibm-watson-cloud-platform-using-raspberry-pi
https://github.com/adafruit/Adafruit_Python_DHT


"""


#import libraries
import RPi.GPIO as GPIO
import time
from time import sleep
import Adafruit_DHT
#import paho.mqtt.client as mqtt #to be used when sending data to IBM bluemix cloud

#Define variables and GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FAN_PIN = 23
GPIO.setup(FAN_PIN, GPIO.OUT)
TEMP_THRESHOLD = 23
gpio=17
sensor=Adafruit_DHT.DHT11
try:
    while True:
        temp - Adafruit_DHT.read_retry(sensor, gpio)
        sleep(5)
        print(temp)
        
        if temp > TEMP_THRESHOLD:
            GPIO.output(FAN_PIN, GPIO.HIGH)
            print("FAN ON...")

        else:
            GPIO.output(FAN_PIN, GPIO.LOW)
            print("FAN OFF...")
except KeyboardInterrupt:
        GPIO.cleanup()
        print("Switching Fan OFF...\nCleaning GPIO...\n*** \n***")
print( "Done!")
