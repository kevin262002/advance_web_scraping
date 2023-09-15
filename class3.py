import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.goodreads.com/quotes')

soup = BeautifulSoup(r.content,'html.parser')

a = soup.find(class_='quotes')

print(a.prettify())

