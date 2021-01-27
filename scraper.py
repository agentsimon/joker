import requests
from bs4 import BeautifulSoup
import csv
# open a file for writing
jokes_data = csv.writer(open('jokes.csv', 'w', newline=''))
jokes_data.writerow(['Joke'])
url = 'https://athlonsports.com/dad-jokes'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
target = soup.find('h2',text='Best Dad Jokes')


for sib in target.find_next_siblings():
    if sib.name=="h2":
        break
    else:
        print(sib.text)
        
        jokes = sib.text
        jokes_data.writerow([jokes])



