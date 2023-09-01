import requests
import time

url = 'http://httpbin.org/get'
proxies = {
    'http': 'http://200.12.55.90:80',
    'https': 'http://200.12.55.90:80'
    }
start = time.perf_counter()
try:
    requests.get(url=url, proxies=proxies, timeout=1)
except Exception as _ex:
    print(time.perf_counter() - start)
