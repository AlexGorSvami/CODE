from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find_all('p', class_='price')
answer = 0
for i in div:
    price = int(i.text.split()[0])
    answer += price
print(answer)
