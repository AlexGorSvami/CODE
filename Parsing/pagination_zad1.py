from bs4 import BeautifulSoup
import requests

# print('-----------------------------1----------------------------')
# url = 'http://parsinger.ru/html/index3_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# shema = 'https://parsinger.ru/html/'
# pagen = [f'{shema}{link["href"]}' for link in soup.find('div', class_='pagen').find_all('a')]
# res = []
# for i in pagen:
#     response = requests.get(url=i)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     div1 = soup.find_all('a', class_='name_item')
#     res.append([name.text for name in div1])


# print('----------------------------2---------------------------')
# url = 'http://parsinger.ru/html/index3_page_4.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# shema = 'https://parsinger.ru/html/'
# pagen = [f'{shema}{link["href"]}' for link in soup.find('div', class_='pagen').find_all('a')]
# res = 0
# for i in pagen:
#     response = requests.get(url=i)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     mouses = [f'{shema}{tag["href"]}' for tag in soup.find_all('a', class_='name_item')]
#     for link in mouses:
#         response = requests.get(url=link)
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         res += int(soup.find('p', {'class':'article'}).text.split()[1])


print('-----------------------------------3--------------------------------')
url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'https://parsinger.ru/html/'
pagen = [f'{shema}{link["href"]}' for link in soup.find('div', class_='pagen').find_all('a')]
res = 0
index_lables = {1:'watch', 2:'mobile', 3:'mouse', 4:'hdd', 5:'headphones'}
for i in range(5):
    for j in range(32):
        url = f'{shema}{index_lables[i+1]}/{i+1}/{i+1}_{j+1}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        price = int(soup.find('span', id='price').text.split()[0])
        count = int(soup.find('span', id='in_stock').text.split()[2])
        res += price * count

print(res)
