

import sys
import os
print(str(sys.path))
import pyttsx3
import csv
import RPi.GPIO as GPIO
import time


# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
GPIO_PIN = 24
GPIO.setmode(GPIO.BCM)
csvFileArray = []

GPIO.setup(GPIO_PIN, GPIO.IN)

file_name = '/home/pi/Documents/Joke project/jokes.csv'
jokes_list = open(file_name, 'r')

for row in csv.reader(jokes_list, delimiter = '.'):
  csvFileArray.append(row)
total_row = len(csvFileArray)
#Function executed on signal detection
def active(null):
        #value = randint(0, random_tot)
        joke = csvFileArray[randint(0, total_row)]
        print(joke)
        converter = pyttsx3.init()
        # Sets speed percent  
# Can be more than 100 
        converter.setProperty('rate', 120) 
# Set volume 0-1 
        converter.setProperty('volume', 0.7) 
        converter.say(joke)
        converter.runAndWait()

#On detecting signal (falling edge), active function will be activated.
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=active, bouncetime=100) 
  
# main program loop
try:
        while True:
                
                time.sleep(1)
  
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
