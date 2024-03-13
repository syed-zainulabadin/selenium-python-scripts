import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

directory = 'C:/Users/Test-Scripts/Reports/Meta-Report/'

data = []

urls = [
    "https://www.gogle.com",
    "---"
]

browser = webdriver.Firefox()
browser.maximize_window()

try:
    for url in urls:
        browser.get(url)
        print(url)
        time.sleep(1)
        title = browser.title
        time.sleep(2)
        try:
            meta_description = browser.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content")
        except:
            meta_description = "No meta description found"

        data.append({'URL': url, 'Meta Title': title, 'Meta Description': meta_description})

except Exception as e:
    print(f"Error: {e}")

finally:
    browser.quit()

df = pd.DataFrame(data)

file_name = 'Meta-Report-' + datetime.now().strftime("%y-%m-%d_%H-%M") + '.xlsx'
file_path = os.path.join(directory, file_name)
df.to_excel(file_path, index=False)
print("Data saved to file:", file_name)
