#task1
#print('First commit!')

import requests
from bs4 import BeautifulSoup


url = "https://www.gismeteo.ru/weather-sankt-peterburg-4079/now/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

city = soup.find_all('span', class_='wob_t q8U8x')

print(page.status_code)

