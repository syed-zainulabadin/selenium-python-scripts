import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from datetime import datetime

browser = webdriver.Firefox()
browser.maximize_window()

directory = 'C:/Users/Test-Scripts/Reports/Flex-Chat/'

data = []


def url_function(URL):
    try:
        browser.get("https://www.google.com/" + URL)
        print(browser.current_url)
        time.sleep(7)

        chatbox = browser.find_element(By.CSS_SELECTOR, '#flxChatIcon')

        if chatbox.is_displayed():
            chat_status = 'Implemented'
        else:
            chat_status = 'Not implemented'

        row = {'Provider': URL.capitalize(), 'URL': browser.current_url, 'Flex Chat': chat_status}
        data.append(row)
        print('Flex Chat implemented.')

    except NoSuchElementException:

        chat_status = 'Not implemented'
        row = {'Provider': URL.capitalize(), 'URL': browser.current_url, 'Flex Chat': chat_status}
        data.append(row)
        print('Flex Chat not implemented.')


urls = ["", "abc", "xyz", "--"]

for url in urls:
    url_function(url)

browser.quit()

df = pd.DataFrame(data)
file_name = 'Flex-Chat-Report' + datetime.now().strftime("%y-%m-%d_%H%M") + '.xlsx'
file_path = os.path.join(directory, file_name)
df.to_excel(file_path, index=False)
print("Data saved to file:", file_name)
