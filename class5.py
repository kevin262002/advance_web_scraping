import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.facebook.com/')

soup = BeautifulSoup(r.content,'html.parser')

#s = soup.find('div', id= 'facebook')

#a = s.find(class_='_8esj _95k9 _8esf _8opv _8f3m _8ilg _8icx _8op_ _95ka')

print(soup)

