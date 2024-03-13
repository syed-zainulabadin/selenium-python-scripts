from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://validator.schema.org/")


def url_function(URL):
    time.sleep(2)
    browser.find_element(By.ID, 'new-test-url-input').send_keys(URL)
    time.sleep(2)

    button = browser.find_element(By.ID, 'new-test-submit-button')
    button.click()
    time.sleep(10)

    check = browser.find_element(By.ID, 'results-cell').get_attribute("K4efff-fmcmS")
    print(check)

    # browser.find_element(By.ID, 'new-test').click()
    # browser.find_element(By.ID, 'new-test-url-input').send_keys(URL).clear()


url_function("https://www.google.com")

browser.quit()
