from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.maximize_window()

browser.get("https://www.example.com")
print(browser.current_url)
time.sleep(3)

meta = browser.find_element(By.XPATH, '/html/head/meta[4]').get_attribute('name')
print(meta)

content = browser.find_element(By.XPATH, '/html/head/meta[4]').get_attribute('content')
print(content)

assert meta == 'fo-verify'
assert content == '36297562-4c02-4140-84bc-c1516792f066'

browser.quit()
