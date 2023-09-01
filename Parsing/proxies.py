from fake_useragent import  UserAgent
import requests
from random  import choice

ua =  UserAgent()
# ua = fake_useragent.UserAgent()

url = 'http://httpbin.org/ip'

# for x in range(10):
#     fake_ua = {'user-agent': ua.random}
#     response = requests.get(url=url, headers=fake_ua)
#     print(response.text)

with open('proxies/proxy.txt') as f:
    proxy_file = f.read().split('\n')
    for _ in range(1000):
        try:
            ip = choice(proxy_file).strip()
            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}' 
            }
            response = requests.get(url=url,proxies=proxy,timeout=3)
            print(response.json(), 'Success connection')
        except Exception as _ex:
            continue

