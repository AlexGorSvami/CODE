# import requests
# import json
# from bs4 import BeautifulSoup
# result_json=[]

# for i in range(1,5):
#     url=f'https://parsinger.ru/html/index3_page_{i}.html'
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#     description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
#     price = [x.text for x in soup.find_all('p', class_='price')]
#     for  list_item, price_item, name in zip(description, price, name):
#         result_json.append({
#             'name': name,
#             'brand': [x.split(':')[1] for x in list_item][0],
#             'type': [x.split(':')[1] for x in list_item][1],
#             'connect': [x.split(':')[1] for x in list_item][2],
#             'game': [x.split(':')[1] for x in list_item][3],
#             'price': price_item
#         })

# with open('res1.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
# print('Success')





# import requests
# from bs4 import BeautifulSoup
# import json

# url = 'https://parsinger.ru/html/index1_page_1.html'
# start_url = 'https://parsinger.ru/html/'

# def get_soup(url: str, headers: list = None) -> BeautifulSoup:
#     response = requests.get(url=url, headers=headers)
#     response.encoding = 'utf-8'
#     return BeautifulSoup(markup=response.text, features='html.parser')
        
# def to_json(file_name: str, mode: str, object_: list, encoding: str = 'utf-8', indent: int = 4) -> None:
#     with open(file=file_name, mode=mode, encoding=encoding) as f:
#         json.dump(obj=object_, fp=f, indent=indent, ensure_ascii=False)

# # находим страницу с hdd
# soup = get_soup(url=url)
# hdd_suffix = soup.find(name='div', id='hdd').parent.get('href')
# print(hdd_suffix)
# # страница с hdd
# soup_hdd = get_soup(url=start_url+hdd_suffix)
# # пагинация у hdd
# pagination_hdd = [a.get('href') for a in soup_hdd.find(name='div', class_='pagen').findChildren(name='a')]
# result_json = []
# for page in pagination_hdd:
#     soup_page = get_soup(url=start_url+page)
#     # собираем списки параметров по товарам
#     items = soup_page.find_all(name='div', class_='item')
#     for item in items:
#         item_dict = {}
#         # наименование
#         item_dict[item.find(name='a', class_='name_item')['class'][0]] = item.find(name='a', class_='name_item').text.strip()
#         # описание
#         for i, li in enumerate([li.text.split(':')[1].strip() for li in item.find(name='div', class_='description').find_all(name='li')]):
#             if i == 0:
#                 item_dict['brand'] = li
#             elif i == 1:
#                 item_dict['type'] = li
#             elif i == 2:
#                 item_dict['volume'] = li
#             elif i == 3:
#                 item_dict['buffer_volume'] = li
#         # стоимость
#         item_dict[item.find(name='p', class_='price')['class'][0]] = item.find(name='p', class_='price').text
#         result_json.append(item_dict)
# # записываем в json
# to_json(file_name='res.json', mode='w', object_=result_json)

# import requests
# from bs4 import BeautifulSoup
# import json


# def get_soup(url):
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     return BeautifulSoup(response.text, 'lxml')


# shema = 'https://parsinger.ru/html/'
# soup = get_soup('https://parsinger.ru/html/index1_page_1.html')
# mouse = soup.find('div', id='mouse')
# mouse_url = f"{shema}{mouse.find_parent()['href']}"
# pages = (f"{shema}{link['href']}" for link in get_soup(mouse_url).find('div', class_='pagen').find_all('a'))
# result_json = []
# for page in pages:
#     soup_page = get_soup(page)
#     name = [x.text.strip() for x in soup_page.find_all('a', class_='name_item')]
#     description = [x.text.strip().split('\n') for x in soup_page.find_all('div', class_='description')]
#     price = [x.text for x in soup_page.find_all('p', class_='price')]
#     for list_item, price_item, name in zip(description, price, name):
#         result_json.append({
#             'name': name,
#             'brand': [x.split(':')[1] for x in list_item][0],
#             'type': [x.split(':')[1] for x in list_item][1],
#             'connect': [x.split(':')[1] for x in list_item][2],
#             'game': [x.split(':')[1] for x in list_item][3],
#             'price': price_item

#         })
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)


# import requests
# from bs4 import BeautifulSoup
# import json

 
# url = 'https://parsinger.ru/html/index3_page_1.html'

# response = requests.get(url=url)
# response.encoding = 'utf-8'

# soup = BeautifulSoup(response.text, 'lxml')

# shema = 'http://parsinger.ru/html/'
# # получение ссылок на страницы
# Pages = [shema + link['href'] for link in soup.find('div', class_='pagen').find_all('a') ] 

# result_json = [] 
# #
# for Page in Pages:
#     print('====Processing:{0} ===='.format( Page) )

#     response_page  =  requests.get(url =  Page)
#     response_page.encoding = 'utf-8'
    
#     soup_page = BeautifulSoup(response_page.text, 'lxml')
#     # получение HTML-кодов карточек с товарами

#     Items = soup_page.find_all(name = 'div', class_ = "item" )
#     # проход по карточкам товаров
#     for Item in Items:

#         dict_item = {}
#         # добыча данных о товаре, запись в словарь и добавление в массив

#         Name = Item.find(name = 'a', class_ = "name_item" ).text

#         dict_item.update( { "Имя" :  Name })

#         description = Item.find('div', class_ = 'description').find_all('li')

#         for X in  description:

#             dict_item.update( { X.text.split(": ")[0] :  X.text.split(": ")[1]})

#         dict_item.update( { "Цена" : Item.find('p', class_ = 'price').text  })
        
 

#         result_json.append(dict_item)


 
# # запись массива в файл JSON       
# with open('res.json', 'w', encoding='utf-8') as file:
    
#     json.dump(result_json, file, indent=4, ensure_ascii=False)

print('----------------------------------2----------------------------------------')
# import json
# import requests
# from bs4 import BeautifulSoup

# result_json = []


# for i in range(1,6):
#     for j in range(1,5):
#         url = f'https://parsinger.ru/html/index{i}_page_{j}.html'
#         response = requests.get(url=url)
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#         description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
#         price = [x.text for x in soup.find_all('p', class_='price')]
#         for  list_item, price_item, name in zip(description, price, name):
#             result_json.append({
#                 'name': name,
#                 'brand': [x.split(':')[1] for x in list_item][0],
#                 'type': [x.split(':')[1] for x in list_item][1],
#                 'connect': [x.split(':')[1] for x in list_item][2],
#                 'game': [x.split(':')[1] for x in list_item][3],
#                 'price': price_item
#             })
# with open('res2.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
# print('Success')




# import requests
# from bs4 import BeautifulSoup
# import json

# url = 'https://parsinger.ru/html/index1_page_1.html'
# start_url = 'https://parsinger.ru/html/'

# def get_soup(url: str, headers: list = None) -> BeautifulSoup:
#     response = requests.get(url=url, headers=headers)
#     response.encoding = 'utf-8'
#     return BeautifulSoup(markup=response.text, features='html.parser')
        
# def to_json(file_name: str, mode: str, object_: list, encoding: str = 'utf-8', indent: int = 4) -> None:
#     with open(file=file_name, mode=mode, encoding=encoding) as f:
#         json.dump(obj=object_, fp=f, indent=indent, ensure_ascii=False)

# result_json = []
# # странички категорий
# soup = get_soup(url=url)
# categories_url = [a.get('href') for a in soup.find(name='div', class_='nav_menu').find_all(name='a')]
# for category_url in categories_url:
#     soup_category = get_soup(url=start_url+category_url)
#     # пагинация
#     pagination_pages = [a.get('href') for a in soup_category.find(name='div', class_='pagen').findChildren(name='a')]
#     for pagination_page in pagination_pages:
#         soup_page = get_soup(url=start_url+pagination_page)
#         # блок с товарами
#         items = soup_page.find_all(name='div', class_='item')
#         for item in items:
#             item_dict = {}
#             # наименование
#             item_dict['Наименование'] = item.find(name='a', class_='name_item').text.strip()
#             # описание
#             for li in item.find(name='div', class_='description').find_all(name='li'):
#                 item_dict[li.text.split(':')[0].strip()] = li.text.split(':')[1].strip()
#             # стоимость
#             item_dict['Стоимость'] = item.find(name='p', class_='price').text
#             result_json.append(item_dict)
# # записываем в json
# to_json(file_name='res_2.json', mode='w', object_=result_json)


print('-------------------------------3---------------------------------------')
import json
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/html/mouse/3/3_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
count_pages = [a.get('href')  for a in soup.find(name='div', class_='haeders').find_all(name='a', id='a_back')]
print(count_pages)
