import csv 
import requests
from bs4 import BeautifulSoup

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса', 
    'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',  'Ссылка на карточку с товаром'    
    ])

for i in range(1,33):
    url = 'https://parsinger.ru/html/watch/1/1_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    