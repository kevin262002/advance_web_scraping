import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.amazon.in/deals?ref_=nav_cs_gb&deals-widget=%257B%2522version%2522%253A1%252C%2522viewIndex%2522%253A0%252C%2522presetId%2522%253A%2522065C798DA38A41B2A8D866C6A023C6F8%2522%252C%2522sorting%2522%253A%2522FEATURED%2522%257D')

soup = BeautifulSoup(r.content,'html.parser')

a = soup.find('div',class_='DealGridItem-module__dealItemContent_1vFddcq1F8pUxM8dd9FW32')

print(a)

