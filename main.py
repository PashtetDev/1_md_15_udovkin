#task1
#print('First commit!')

import requests
from bs4 import BeautifulSoup


url = "https://www.gismeteo.ru/weather-sankt-peterburg-4079/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

city = soup.find('h1').text

print(city)