from bs4 import BeautifulSoup
import requests


print('----------------------Part1----------------------------')
# url = 'http://parsinger.ru/html/index1_page_3.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# pagen = soup.find('div', class_='pagen').find_all('a')
# pagen = [link['href'] for link in pagen]
# list_link = []
# shema = 'https://parsinger.ru/html/'
# pagen = [f'{shema}{link["href"]}' for link in soup.find('div', class_='pagen').find_all('a')]
# # for link in pagen:
# #     list_link.append(shema+link)

# print(pagen)

print('---------------------------Part2----------------------------')
link = []
for i in range(1,101):
    link.append(f'https://www.wildberries.ru/catalog/elektronika/smart-chasy?sort=popular&page={i}')

url = 'https://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'https://parsinger.ru/html/'
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]
print(pagen)


