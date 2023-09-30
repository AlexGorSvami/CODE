import time
from selenium import webdriver

print('----------------------------------1----------------------------------')
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     browser.execute_script('window.scrollBy(0, 10000)')
#     time.sleep(5)

print('----------------------------------2----------------------------------')
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     for i in range(10):
#         browser.execute_script('window.scrollBy(0, 5000)')
#         time.sleep(2)

print('----------------------------------3----------------------------------')
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     height = browser.execute_script('return document.body.scrollHeight')
#     time.sleep(2)
#     print(height)

print('----------------------------------4----------------------------------')
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     height = browser.execute_script('return window.innerHeight')
#     print(height)

print('---------------------------------5----------------------------------')
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)


