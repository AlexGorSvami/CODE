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
# import csv 
# import requests
# from bs4 import BeautifulSoup

# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f, delimiter=';')

# for i in range(1,6):
#     url = f'https://parsinger.ru/html/index{i}_page_1.html'
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

#     items_all = []
#     schema = 'https://parsinger.ru/html/'

#     for page in pagen:
#         response = requests.get(url=schema + page)
#         response.encoding = 'utf-8'
#         page_soup = BeautifulSoup(response.text, 'lxml')
#         items_all += page_soup.find_all(class_ = 'item')
        
#     for item in items_all:
#         name = item.find(class_ = 'name_item').text.strip()   
#         div_description = item.find(class_ = 'description').text.strip().split('\n')
#         brand = div_description[0].split(':')[1].strip()
#         form_factor = div_description[1].split(':')[1].strip()
#         capacity = div_description[2].split(':')[1].strip()
#         volume = div_description[3].split(':')[1].strip()
#         price = item.find(class_ = 'price').text.strip(' ')
        
#         with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#             writer = csv.writer(file, delimiter=';')
#             writer.writerow([
#                 name, brand, form_factor, capacity,
#                 volume, price])


# print('Успешно сохранено!')
        

# import csv
# import requests
# from bs4 import BeautifulSoup

# with open('res.csv', 'w') as file:
#     "для очистки старого файла с именем 'res.csv', если имеется"
#     pass

# for i in range(1, 6):
#     for j in range(1, 5):
#         url = f'https://parsinger.ru/html/index{i}_page_{j}.html'

#         response = requests.get(url)
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')

#         name = [i.text for i in soup.find_all('a', class_='name_item')]
#         descr = [i.text.split('\n') for i in soup.find_all('div', class_='description')]
#         price = [i.text for i in soup.find_all('p', class_='price')]

#         for name, descr, price in zip(name, descr, price):
#             product = name, *[i.split(':')[1] for i in descr if i], price

#             with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#                 writer = csv.writer(file, delimiter=',')
#                 writer.writerow(product)



# from bs4 import BeautifulSoup
# import requests
# import csv

# # открываем сайт 
# url = 'https://parsinger.ru/html/index4_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')

# # составляем список ссылок навигационного меню
# nav_links = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]

# # составляем список ссылок для пагинации
# shema = 'https://parsinger.ru/html/'
# pagen = []
# for nav_link in nav_links:
#     url = shema + nav_link
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     pagen += [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

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
#     descr_1 = div_description[0][div_description[0].find(':') + 1:].strip()
#     descr_2 = div_description[1][div_description[1].find(':') + 1:].strip()
#     descr_3 = div_description[2][div_description[2].find(':') + 1:].strip()
#     descr_4 = div_description[3][div_description[3].find(':') + 1:].strip()
    
#     price = item.find(class_ = 'price').text.strip()
    
#     # записываем в файл построчно
#     with open('495res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow([
#             name, descr_1, descr_2, descr_3,
#             descr_4, price])


# import csv
# from bs4 import BeautifulSoup
# import requests



# with open('task3.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')



# for index in range(1, 6):
#     for page in range(1, 5):
#         url = f'https://parsinger.ru/html/index{index}_page_{page}.html'
#         response = requests.get(url=url)
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#         description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
#         price = [x.text for x in soup.find_all('p', class_='price')]

#         for item, descr, price in zip(name, description, price):
#             flatten = item, *[x.split(':')[1].strip() for x in descr if x], price

#             file = open('task3.csv', 'a', encoding='utf-8-sig', newline='')
#             writer = csv.writer(file, delimiter=';')
#             writer.writerow(flatten)
#     file.close()

print('--------------------------3-------------------------')
import csv
import requests
from bs4 import BeautifulSoup

def to_flatten(a_list: list, depth: int = -1) -> list:
    count = 0
    while True:
        result = []
        has_list = False
        for element in a_list:
            if type(element) is list:
                result.extend(element)
                has_list = True
            else:
                result.append(element)
        a_list = result
        count += 1
        if not has_list or (0 < depth == count):
            break
    return result

with open('res3.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса', 'Материал браслета', 'Размер', 
    'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',  'Ссылка на карточку с товаром'])

for i in range(1,5):
    for j in range(1,33):
        url = f'https://parsinger.ru/html/watch/{i}/1_{j}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        description = to_flatten(description)
        description = [i.split(':')[1].strip() for i in description if ':' in i]
        print(description)
        link = [link['href'] for link in soup.find_all('a', id='a_back')]
    #     for descr, lin  in  zip(description, link):
    #         flatten  = [*[list(str(x).split(':')) for x in descr if len(x)>0], lin]
    #         flatten.remove(flatten[-2])
    #         flatten = to_flatten(flatten)
    #         print(flatten)
    # #         file = open('res3.csv', 'a', encoding='utf-8-sig', newline='')
    #         writer = csv.writer(file, delimiter=';')
    #         writer.writerow(flatten)
    # file.close()

