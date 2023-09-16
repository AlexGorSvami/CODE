print('------------------------1-------------------')
import csv 
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index1_page_1.html'

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow([
                'Наименование', 'Цена', 'Бренд', 'Форм-фактор', 'Объём буф.памяти', 'Цена'])
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
