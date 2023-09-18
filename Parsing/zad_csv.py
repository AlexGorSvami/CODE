print('------------------------1-------------------')
# import csv 
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/html/index4_page_1.html'

# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f, delimiter=';')
#     writer.writerow([
#                  'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена'])
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# shema = 'https://parsinger.ru/html/'
# pagen = [f'{shema}{link["href"]}' for link in soup.find('div', class_='pagen').find_all('a')]
# for link in pagen:
#     soup = BeautifulSoup(requests.get(url=link).text, 'lxml')
#     name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#     description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
#     price = [x.text.split()[0] for x in soup.find_all('p', class_='price')]

#     for item, price, desc in zip(name, price, description):
#         flatten = item, *[x.split(':')[1].strip() for x in desc if x], price
#         f = open('res.csv', 'a', encoding='utf-8-sig', newline='')
#         writer = csv.writer(f, delimiter=';')
#         writer.writerow(flatten)
#     f.close()
# print('Успешно сохранено!')

# from bs4 import BeautifulSoup
# import requests
# import csv

# # открываем файл и записываем туда заголовки таблицы
# with open('494res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Бренд', 'Форм-фактор', 
#         'Емкость', 'Объём буф. памяти', 'Цена'])

# # открываем сайт и составляем список для пагинации
# url = 'https://parsinger.ru/html/index4_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

# # идём по каждой ссылке в списке пагинации и составляем список всех товаров
# items_all = []
# schema = 'https://parsinger.ru/html/'

# for page in pagen:
#     response = requests.get(url=schema + page)
#     response.encoding = 'utf-8'
#     page_soup = BeautifulSoup(response.text, 'lxml')
#     items_all += page_soup.find_all(class_ = 'item')
    
# # проходим по списку товаров и переписываем оттуда в файл все значения атрибутов
# for item in items_all:
#     name = item.find(class_ = 'name_item').text.strip()
    
#     div_description = item.find(class_ = 'description').text.strip().split('\n')
#     brand = div_description[0][div_description[0].find('Бренд:') + 6:].strip()
#     form_factor = div_description[1][div_description[1].find('Форм-фактор:') + 12:].strip()
#     capacity = div_description[2][div_description[2].find('Ёмкость:') + 8:].strip()
#     volume = div_description[3][div_description[3].find('памяти:') + 7:].strip()
    
#     price = item.find(class_ = 'price').text.strip()
    
#     # записываем в файл построчно
#     with open('494res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow([
#             name, brand, form_factor, capacity,
#             volume, price])

print('-------------------------------------2----------------------------------------------')
import csv 
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index4_page_1.html'

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
for i in range(1,6):
    url = f'https://parsinger.ru/html/index{i}_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    shema = 'https://parsinger.ru/html/'
    pagen = [f'{shema}{link["href"]}' for link in soup.find('div', class_='pagen').find_all('a')]
    for link in pagen:
        soup = BeautifulSoup(requests.get(url=link).text, 'lxml')
        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        price = [x.text.split()[0] for x in soup.find_all('p', class_='price')]

        for item, price, desc in zip(name, price, description):
            flatten = item, *[x.split(':')[1].strip() for x in desc if x], price
            f = open('res.csv', 'a', encoding='utf-8-sig', newline='')
            writer = csv.writer(f, delimiter=';')
            writer.writerow(flatten)
        f.close()
print('Успешно сохранено!')
        