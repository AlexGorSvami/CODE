from pprint import pprint
from selenium import webdriver

print('-----------------------1------------------------')
# url = 'https://parsinger.ru/methods/3/index.html'

# res = []
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     cookies = browser.get_cookies()
#     for i in cookies:
#         res.append(int(i['value']))

# print(sum(res))

print('--------------------------------2------------------------')
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/3/index.html')
#     cookies = browser.get_cookies()
#     res = [int(i['value']) for i in cookies if int(i['name'].replace('_','',1).split('_')[1]) % 2 == 0]

# print(sum(res))

print('-------------------------------3-------------------------')
from selenium import webdriver
from selenium.webdriver.common.by import By

res = 0
for i in range(1,43):
    with webdriver.Chrome() as browser:
        browser.get(f'https://parsinger.ru/methods/5/{i}.html')
        cookies = browser.get_cookies()
        for i in cookies:
            if i['expiry'] > res:
                res = i['expiry']
                print(browser.find_element(By.ID, 'result').text)





        
