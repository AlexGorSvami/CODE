print('-----------------alert---------------------')
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'alert').click()
    time.sleep(2)
    alert = browser.switch_to.alert
    print(alert.text)
    time.sleep(1)
    alert.accept()

print('----------------------prompt---------------------')
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'prompt').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.send_keys('Ky-ky')
    prompt.accept()
    time.sleep(3)
    print(browser.find_element(By.ID, 'result').text)

print('----------------------confirm---------------------')
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'confirm').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.accept() #Замените на .dismiss() чтобы нажать на кнопку "Отмена"
    time.sleep(.5)

