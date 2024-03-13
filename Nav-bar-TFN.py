import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from datetime import datetime

browser = webdriver.Firefox()
browser.maximize_window()

directory = 'C:/Users/Test-Scripts/Reports/NavBar-TFN/'

data = []


def url_function(URL):
    try:
        browser.get(URL)
        print(browser.current_url)
        time.sleep(3)

        navbar = browser.find_element(By.ID, "navbar-tfn")

        if navbar.is_displayed():
            navbar_status = 'Navbar-TFN Added'
        else:
            navbar_status = 'Not Added'

        row = {'URL': browser.current_url, 'NavBar-TFN': navbar_status}
        data.append(row)
        print('Navbar-TFN Added.')

    except NoSuchElementException:

        navbar_status = 'Not Added'
        row = {'URL': browser.current_url, 'NavBar-TFN': navbar_status}
        data.append(row)
        print('Navbar-TFN Not Added.')


urls = [
    "https://www.example.com",
    "---"
]

for url in urls:
    url_function(url)

browser.quit()

df = pd.DataFrame(data)
file_name = 'NavBar-TFN-Report-' + datetime.now().strftime("%y-%m-%d_%H-%M") + '.xlsx'
file_path = os.path.join(directory, file_name)
df.to_excel(file_path, index=False)
print("Data saved to file:", file_name)
