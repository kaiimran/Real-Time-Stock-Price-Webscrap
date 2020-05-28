import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

starttime=time.time()

def priceTracker(url):
    page = urlopen(url)
    soup = bs4.BeautifulSoup(page,'html.parser')
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'lxml')
    #print(soup.prettify())
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

print('Real Time Stock Price (Updated every 15 seconds)')

while True:
    print('FTSE Bursa Malaysia KLCI: RM ' + str(priceTracker('https://finance.yahoo.com/quote/%5EKLSE?p=^KLSE&.tsrc=fin-srch')))
    print('NASDAQ Composite: USD ' + str(priceTracker('https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC&.tsrc=fin-srch')))
    time.sleep(15.0 - ((time.time() - starttime) % 15.0))
