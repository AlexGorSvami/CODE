import time
from selenium import webdriver

url = 'https://stepik.org/a/104774'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)