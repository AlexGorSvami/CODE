import requests
from bs4 import BeautifulSoup
import json

print('---------------------------1-------------------------------')
# url = 'http://parsinger.ru/html/mouse/3/3_11.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')

# result_json = {
#     'name': soup.find('p', id='p_header').text,
#     'price': soup.find('span', id='price').text}

# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)

print('------------------2-------------------------')
# url = 'http://parsinger.ru/html/index3_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')

# name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
# description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
# price = [x.text for x in soup.find_all('p', class_='price')]

# res_json = []

# for list_item, price_item, name in zip(description, price, name):
#     res_json.append({
#         'name': name,
#         'brand': [x.split(':')[1] for x in list_item][0],
#         'type': [x.split(':')[1] for x in list_item][1],
#         'connect': [x.split(':')[1] for x in list_item][2],
#         'game': [x.split(':')[1] for x in list_item][3],
#         'price': price_item
#     })


# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(res_json, file, indent=4, ensure_ascii=False)
print('----------------------------3-----------------------')
response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
description = soup.find('ul', id='description').find_all('li')
li_id = [x['id'] for x in description]
print(li_id)

for li in description:
    print(li['id'])

