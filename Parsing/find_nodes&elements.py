from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('div', 'item')
div1 = soup.find('div', 'item').find_all('li')
print(div)
print(div1)

for txt in div1:
    print(txt.text)

