from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://parsinger.ru/blank/modal/2/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    for i in browser.find_elements(By.CLASS_NAME, 'buttons'):
        i.click()
        i.switch_to.alert.accept()
        if browser.find_element(By.ID, 'result'):
            print(browser.find_element(By.ID, 'result').text)

    
        

