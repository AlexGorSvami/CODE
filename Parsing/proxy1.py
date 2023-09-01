from random import choice
import requests
import re

url = 'http://httpbin.org/ip'
proxies = []
amount_of_proxies = 10

with open('proxies/proxy.txt') as file:
    proxy_file = file.read().split('\n')
    while len(proxies) < amount_of_proxies and len(proxy_file) > 0:
        try:
            ip = proxy_file.pop(proxy_file.index(choice(proxy_file))).strip()
            if not re.fullmatch(r'([0-2]?\d{2}\.){3}([0-2]?\d{2})\:\d+', ip):
                continue
            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
            }
            response = requests.get(url=url, proxies=proxy, timeout=30)
            if response.status_code != 200:
                print(f'{ip}: response {response.status_code}. Bad connection')
            else:
                print(response.json(), 'Success connection')
                proxies.append(ip)
        except Exception as _ex:
            print(f'{ip}: {_ex}')

print(proxies)