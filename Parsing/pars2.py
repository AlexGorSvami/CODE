from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/hdd/4/4_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
old = 0
new = 0
old_prices = soup.find('span', id='old_price')
new_price = soup.find('span', id='price')
old = int(old_prices.text.split()[0])
new = int(new_price.text.split()[0])
print(round((old-new)*100/old,2))

