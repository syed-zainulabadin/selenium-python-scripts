from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://www.example.com")
print(browser.current_url)
ZIP = browser.find_element(By.ID, 'ZipSearch')
ZIP.send_keys("10001")

BTN = browser.find_element(By.CLASS_NAME, 'zip-btn')
BTN.click()
time.sleep(4)

browser.execute_script("window.scrollTo(0, 780)")
time.sleep(4)

attr_value = browser.find_element(By.CLASS_NAME, 'providerBox').get_attribute('provider')
print(attr_value)
time.sleep(3)

rows = browser.find_elements(By.CLASS_NAME, 'providerBox')

for value in rows:
  print(value.get_attribute("provider"))


browser.quit()


