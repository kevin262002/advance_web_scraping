import requests
from bs4 import BeautifulSoup

r = requests.get('https://timesofindia.indiatimes.com/home/headlines')

soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('div', id= 'c_headlines_wdt_1')

a = s.find('ul',class_='clearfix')

print(a.prettify())

