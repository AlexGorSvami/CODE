import requests

url_usd = 'https://cbr.ru/cursonweek/?DT=&val_id=R01235&_=1692528097005'
url_eur = 'https://cbr.ru/cursonweek/?DT=&val_id=R01239&_=1692528097006'
url_cny = 'https://cbr.ru/cursonweek/?DT=&val_id=R01375&_=1692528097007'

urls_list = [url_usd, url_eur, url_cny]
ex_list = ['USD', 'EUR', 'CNY']

for i, j in zip(urls_list, ex_list):
    response = requests.get(i).json()[-1]
    print(f"Курс {j} на {response['data'][:-9]} к рублю - {response['curs']}")

print('----------------------------------------------')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.207.132.170 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
data = {
    "GivenName": "Monero",
    "GetName": "Dash",
    "Sum": 100,
    "Direction": 0
}

url = 'https://bitality.cc/Home/GetSum?'
response = requests.get(url=url, headers=headers, params=data).json()
print(response)


