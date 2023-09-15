import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.instagram.com/')

soup = BeautifulSoup(r.content,'html.parser')

a = soup.find(class_='x1qjc9v5 x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x78zum5 x1q0g3np x1iyjqo2 x2lah0s xk390pu xl56j7k xg87l8a xkrivgy xat24cr x1gryazu x1ykew4q xexx8yu x4uap5 x1gan7if xkhd6sd x11njtxf xh8yej3 x1d2lwc3')

print(a.prettify())

