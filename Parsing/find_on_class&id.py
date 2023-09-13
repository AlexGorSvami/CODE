from bs4 import BeautifulSoup
import requests 
url = 'http://parsinger.ru/html/headphones/5/5_32.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('p', class_='article').text
div1 = soup.find('p', id='p_header').text
div3 = soup.find('span', {'name':'count'}).text
print(div)
print(div1)
print(div3)
