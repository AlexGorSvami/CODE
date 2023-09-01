import requests

url = 'http://parsinger.ru/task/1/'
count = 0
for i in range(331,501):
    response = requests.get(url=f'http://parsinger.ru/task/1/{i}.html')
    if response.status_code == 200:
        print(url+i.html)
        break
    print(response.status_code)
    count += 1
    print(count)

