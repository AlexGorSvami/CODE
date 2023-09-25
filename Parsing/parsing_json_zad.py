import requests

print('-----------------------------------1----------------------------------')
response = requests.get(url='http://parsinger.ru/downloads/get_json/res.json').json()
res = {}
for item in response:
    res.setdefault(item["categories"],[]).append(int(item["count"]))
res = {key:sum(value) for key, value in res.items()}
print(res)

print('----------------------------2----------------------------')
response = requests.get(url='http://parsinger.ru/downloads/get_json/res.json').json()
res = {}
for item in response:
    res.setdefault(item["categories"],[]).append(int(item["count"])*int(item["price"].split()[0]))
res = {key:sum(value) for key, value in res.items()}
print(res)
