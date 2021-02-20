import pandas as pd
import RPi.GPIO as GPIO
import urllib
import time

GPIO.setmode(GPIO.BCM)

sensor = 24

GPIO.setup(sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)
file_name = "jokes.csv"
jokes_list = pd.read_csv(file_name)
joke = []
  
#Function executed on signal detection
def active(null):
	try:
			url = "https://www.google.com"
			urllib.urlopen(url)
			status = "Connected"
			
	except:
			print("No internet connection.")
			file_name = '/home/pi/Documents/Jokeproject/jokes.csv'
			jokes_list = open(file_name, 'r')
			csvFileArray = []
			for row in csv.reader(jokes_list, delimiter = '.'):
				csvFileArray.append(row)
			total_row = len(csvFileArray)
			joke = csvFileArray[randint(0, total_row)]
	if status == "Connected":
		print("Connected to the Internet")
		data = requests.get(f)
		a = json.loads(data.text)
		part1 = (a["setup"],)
		part2 = (a["punchline"],)
		joke = part1 + part2
    
	else:
		print("No internet connection.")
		file_name = '/home/pi/Documents/Jokeproject/jokes.csv'
		jokes_list = open(file_name, 'r')
		csvFileArray = []
		for row in csv.reader(jokes_list, delimiter = '.'):
			csvFileArray.append(row)
		total_row = len(csvFileArray)
		joke = csvFileArray[randint(0, total_row)]

	converter = pyttsx3.init()
        # Sets speed percent  
    # Can be more than 100 
	# converter.setProperty('rate', 120) 
    # Set volume 0-1 
	converter.setProperty('volume', 1) 
	converter.say(joke)
	converter.runAndWait()

#On detecting signal (falling edge), active function will be activated.
GPIO.add_event_detect(sensor, GPIO.FALLING, callback=active, bouncetime=100) 


# main program loop
try:
        while True:
                time.sleep(0.05)
  
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
