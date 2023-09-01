import requests

response = requests.get(url='https://jsonplaceholder.typicode.com/todos/')
print(response)

response = requests.get(url='https://jsonplaceholder.typicode.com/todos/')
print(response.text)