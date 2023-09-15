import requests
from bs4 import BeautifulSoup

r = requests.get('https://timesofindia.indiatimes.com/city/mumbai')

soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('div', id= 'app')

a = s.find(class_='row')

print(a.prettify())

