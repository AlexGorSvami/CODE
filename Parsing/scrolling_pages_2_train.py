from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

# res = []
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/2/index.html')
#     for i in range(1,51):
#         browser.find_element(By.ID, f'{i}').click()
#         value = browser.find_element(By.ID, f'result{i}').text
#         if value:
#             res.append(int(value))

# print(sum(res))
print('--------------------------2---------------------------')
# res = []
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/3/')
#     for i in range(1,501):
#         browser.find_element(By.ID, f'{i}').click()
#         value = browser.find_element(By.ID, f'result{i}').text
#         if value:
#             res.append(i)

# print(sum(res))

print('----------------------------------3--------------------------------')
res = []
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_1/')
    for tag in browser.find_elements(By.TAG_NAME, 'input'):
        
        
    