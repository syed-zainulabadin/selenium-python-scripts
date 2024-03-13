from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import pandas as pd
from datetime import datetime

directory = 'C:/User/Test-Scripts/Reports/Canonical-Report/'

data = []

urls = [
    "https://www.example.com",
    "---"
]

browser = webdriver.Firefox()
browser.maximize_window()


def get_canonical_url(url):
    try:
        browser.get(url)
        time.sleep(3)
        print(url)
        canonical_element = browser.find_element(By.XPATH, "//link[@rel='canonical']")
        canonical_url = canonical_element.get_attribute("href")

        return canonical_url

    except NoSuchElementException:
        print("Canonical not found")
        return None


for url in urls:
    canonical_url = get_canonical_url(url)
    if canonical_url is not None:
        row = {'URL': url, 'Canonical': canonical_url}
        data.append(row)
        print('Canonical Added')
    else:
        row = {'URL': url, 'Canonical': "Canonical missing"}
        data.append(row)

browser.quit()

df = pd.DataFrame(data)

file_name = 'Canonical-Report-' + datetime.now().strftime("%y-%m-%d_%H-%M") + '.xlsx'
file_path = os.path.join(directory, file_name)

df.to_excel(file_path, index=False)
print("Data saved to file:", file_name)
