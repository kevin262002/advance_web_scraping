import requests
from bs4 import BeautifulSoup

r = requests.get(' https://www.producthunt.com/')

soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('div', id= '__next')

a = s.find(class_='px-mobile-1 px-tablet-1 pt-mobile-0 pt-desktop-6 pt-tablet-6 pt-widescreen-6 pb-mobile-7 pb-desktop-6 pb-tablet-6 pb-widescreen-6')

print(a.prettify())

