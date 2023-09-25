import  requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url=url).json()
for item in response:
    print(item["userId"],  item["title"])

print('--------------------2-------------------------')

url = 'http://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url=url).json()
for item in  response:
    print(item["description"]["brand"], item["description"]["model"])

