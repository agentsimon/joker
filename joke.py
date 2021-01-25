
import sys
import os
print(str(sys.path))
import pyttsx3
import pandas as pd
import RPi.GPIO as GPIO
import time


# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
GPIO.setmode(GPIO.BCM)

sensor = 17

#GPIO.setup(sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)
file_name = '/home/pi/Documents/Joke project/jokes.csv'
jokes_list = pd.read_csv(file_name, sep='delimiter', header=None)
#find number of rows to use as random number generator 
random_tot = (jokes_list.shape[0])-1
#Function executed on signal detection
# def active(null):
        # #value = randint(0, random_tot)
        # joke = jokes_list.loc[randint(0, random_tot)]
        # engine = pyttsx3.init()
        # engine.say(joke)
        # engine.runAndWait()

#On detecting signal (falling edge), active function will be activated.
#GPIO.add_event_detect(sensor, GPIO.FALLING, callback=active, bouncetime=100) 
  
# main program loop
try:
        while True:
                joke = jokes_list.loc[randint(0, random_tot)]
                engine = pyttsx3.init()
                engine.say(joke)
                print(joke)
                engine.runAndWait()
                time.sleep(1)
  
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
