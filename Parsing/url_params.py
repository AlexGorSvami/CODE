import requests

param = {'key1':'value1', 'key2':'value2'}
r = requests.get('https://httpbin.org/get', params=param)
print(r.url)