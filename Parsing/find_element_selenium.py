# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# browser = webdriver.Chrome()
# browser.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = browser.find_element(By.ID, "sale_button").click()

# time.sleep(10)

print('-----------------------2-------------')
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# try:
#     browser = webdriver.Chrome()
#     browser.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = browser.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)
# finally:
#     browser.quit()

print('--------------------------3---------------------')
# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = browser.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)

print('--------------------------------4-----------------------------')
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.CLASS_NAME, 'text')
    link1 = browser.find_element(By.XPATH, "//div[@class='text'] /p[2]")
    all_link2 = browser.find_elements(By.XPATH, "//div[@class='text'] /p[2]")
    print(link.text)
    print(link1.text)
    print([i.text for i in all_link2])
    

