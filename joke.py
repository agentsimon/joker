#! /usr/bin/python2.7
import sys
import os
print(str(sys.path))
import pyttsx3
import csv
import RPi.GPIO as GPIO
import time


# setup everything
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)
count = 0
prev_input = 0
csvFileArray = []
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

#Read the CSV file
file_name = '/home/pi/Documents/Jokeproject/jokes.csv'
jokes_list = open(file_name, 'r')
csvFileArray = []
for row in csv.reader(jokes_list, delimiter = '.'):
  csvFileArray.append(row)
total_row = len(csvFileArray)


try:
    while True:
        input = GPIO.input(24)
        if ((not prev_input) and input):
            joke = csvFileArray[randint(0, total_row)]
            print(joke)
            converter = pyttsx3.init()
            # Sets speed percent  
    # Can be more than 100 
            converter.setProperty('rate', 120) 
    # Set volume 0-1 
            converter.setProperty('volume', 1) 
            converter.say(joke)
            converter.runAndWait()
        prev_input =input
        time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()

