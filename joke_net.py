import requests
import json


def jokes(f):
    
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt

f = r"https://official-joke-api.appspot.com/random_joke"
a = jokes(f)


input = GPIO.input(24)
    if ((not prev_input) and input):
		joke_getter
		converter = pyttsx3.init()
        # Sets speed percent  
    # Can be more than 100 
	# converter.setProperty('rate', 120) 
    # Set volume 0-1 
		converter.setProperty('volume', 1) 
		converter.say(joke)
		converter.runAndWait()
		prev_input =input
    	time.sleep(0.05)