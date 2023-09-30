import time
from selenium import webdriver
from selenium.webdriver.common.by import By

result = []
url = 'https://parsinger.ru/scroll/4/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    for i in browser.find_elements(By.CLASS_NAME, 'btn'):
        browser.execute_script("return arguments[0].scrollIntoView(true);", i)
        i.click()
        num = browser.find_element(By.ID, 'result')
        result.append(int(num.text))

print(sum(result))