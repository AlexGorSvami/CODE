import time 
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

print('------------------------1------------------------')
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     tag_p = browser.find_elements(By.TAG_NAME, 'input')
    
#     for input in tag_p:
#         input.send_keys(Keys.DOWN)
#         time.sleep(1)

print('-------------------------2-----------------------')

# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')

#     list_input = []
#     while True:
#         input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
#         for input in input_tags:
#             if input not in list_input:
#                 input.send_keys(Keys.DOWN)
#                 input.click()
#                 time.sleep(1)
#                 list_input.append(input)

print('-------------------------3------------------------')
# from selenium.webdriver.common.action_chains import ActionChains

# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/scroll/1/")
#     target = browser.find_elements(By.TAG_NAME, "input")[-1]
#     actions = ActionChains(browser)
#     actions.move_to_element(target)
#     time.sleep(5)
#     actions.click(target)
#     time.sleep(5)
#     actions.perform()
print('-------------------------4------------------------')
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    while True:
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()


