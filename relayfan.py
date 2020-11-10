"""
------HOMEWORK IOT APPLICATION DESIGN---------- 
This code checks temperature from DHT11 sensor and then turns on the fan once its above
the threshhold. 
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

#Define variables and GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FAN_PIN = 23 #gpio pin where the relay will be connected
GPIO.setup(FAN_PIN, GPIO.OUT)
TEMP_THRESHOLD = 26 #The highest tempreture thresh hold when the tempreture goes above this the relay is switched on
gpio=17 #gpio pin for temprature sensor
sensor=Adafruit_DHT.DHT11


try:
    while True:
        humidity, temp = Adafruit_DHT.read_retry(sensor, gpio) #Get temprature and humidity from sensor
        sleep(5) #in seconds
        print(temp)
        
        if temp > TEMP_THRESHOLD: #Checking if tempreture is greater than threshold
            GPIO.output(FAN_PIN, GPIO.HIGH) #Switch on the fan if true
            print("FAN ON...")
            
        else:
            GPIO.output(FAN_PIN, GPIO.LOW) #switch off the fan if false
            print("FAN OFF...")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Switching Fan OFF...\nCleaning GPIO... \n*** \n***")
    print("Done!")
