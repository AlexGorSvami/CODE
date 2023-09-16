from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/table/1/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
nums = [float(i.text) for i in soup.find_all('td')]
print(sum(set(nums)))

print('-------------------------2--------------------')
url = 'https://parsinger.ru/table/2/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# nums = [float(i.text) for i in soup.find_all('td')]
# res = 0
# for i in range(0,len(nums),15):
#     res += nums[i]
# print(res)
td = [float(x.find('td').text) for x in soup.find_all('tr') if x.find('td')]
print(sum(td))
print('---------------------------------------3-----------------------------')
url = 'https://parsinger.ru/table/3/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
td = [float(i.text) for i in soup.find_all('b')]
print(sum(td))

print('----------------------------4-----------------------------')
url = 'https://parsinger.ru/table/4/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
res = [float(i.text) for i in soup.find_all('td', class_='green')]
print(sum(res))

print('----------------------------5------------------------------')
url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
res = [float(i.text) for i in soup.find_all('td', class_='orange')]
blue = [float(i.text) for i in soup.select('td:last-child')]
print(sum(map(lambda x: x[0]*x[1], zip(res, blue))))

print('------------------------6---------------------')
url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
keys = [i.text for i in soup.find_all('th')]
values = [round(sum(float(tag.text) for tag in soup.select(f'table tr td:nth-of-type({i})')),3) for i in range(1, len(keys)+1)]
res = dict(zip(keys, values))
print(res)
# values = [round(sum(values[i:i+15]),3) for i in range(0, len(values),15)]
# print(len(values))
# res = dict(zip(keys, values))
# print(res)

