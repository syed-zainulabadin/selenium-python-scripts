from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pandas as pd
from datetime import datetime

directory = 'C:/Users/Test-Scripts/Reports/AMP-Report/'

data = []

urls = [
    "https://www.example.com/blog/how-it-works"
]

browser = webdriver.Firefox()
browser.maximize_window()


def get_amp_url(url):
    try:
        browser.get(url)
        time.sleep(3)
        print(url)
        amp_element = browser.find_element(By.XPATH, "//link[@rel='amphtml']")
        amp_url = amp_element.get_attribute("href")

        return amp_url

    except NoSuchElementException:
        print("AMP not found")
        return None


for url in urls:
    amp_url = get_amp_url(url)
    if amp_url is not None:
        row = {'URL': url, 'AMP URL': amp_url}
        data.append(row)
        print('AMP Added')
    else:
        row = {'URL': url, 'AMP URL': "AMP not added"}
        data.append(row)

browser.quit()

df = pd.DataFrame(data)

file_name = 'AMP-Report-' + datetime.now().strftime("%y-%m-%d_%H-%M") + '.xlsx'
file_path = os.path.join(directory, file_name)

df.to_excel(file_path, index=False)
print("Data saved to file:", file_name)
