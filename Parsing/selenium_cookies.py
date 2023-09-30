print('---------------------1print cookies-------------------')

# from pprint import pprint
# from selenium import webdriver

# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     cookies = webdriver.get_cookies()

#     pprint(cookies)

print('-------------------------2print_cookies_name-------------------')
# from selenium import webdriver

# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     cookies = webdriver.get_cookies()
#     for cookie in cookies:
#         print(cookie["name"])
#     print(webdriver.get_cookie('_yasc')['expiry'])

print('-----------------------3add_cookies------------------------')
import time
from pprint import pprint
from selenium import webdriver

cookie_dict = {
    'name': 'any_name_cookie',
    'value': 'any_value_cookie',
    'expiry': 2_000_000_000,
    'path': '/',
    'domain': 'parsinger.ru',
    'secure': True,
    'httpOnly': True,
    'sameSite': 'Strict',
}

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/4/index.html')
    webdriver.add_cookie(cookie_dict)
    pprint(webdriver.get_cookies())
    time.sleep(7)

