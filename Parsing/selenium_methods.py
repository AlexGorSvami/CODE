import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    for i in range(100):
        element = browser.find_element(By.ID, 'result')
        print(element.text)
        browser.refresh()