# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coordinates_.crx')

# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     time.sleep(50)


# Запуск браузера в  скрытом режиме
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--disable-gpu')

# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     a = browser.find_element(By.TAG_NAME, 'a')
#     print(a.get_attribute('href'))

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coordinates_.crx')


# options_chrome.add_argument('--disable-gpu=chrome')

# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     time.sleep(5)
#     a = browser.find_element(By.TAG_NAME, 'a')
#     print(a.get_attribute('href'))


print('-----------------------Proxy и Selenium--------------------------')

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://pr-cy.ru/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(5)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)


from selenium import webdriver
from selenium.webdriver.common.by import By

proxy_list = ['138.199.48.1:8443',
'209.126.124.140:3128',
'35.236.207.242:33333',
'34.82.224.175:33333',
'163.172.31.44:80' ]

for PROXY in proxy_list:
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        url = 'https://pr-cy.ru/'

        with webdriver.Chrome(options=chrome_options) as browser:
            browser.get(url)
            print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

            browser.set_page_load_timeout(5)

            proxy_list.remove(PROXY)
    except Exception as _ex:
        print(f"Превышен timeout ожидания для - {PROXY}")
        continue
