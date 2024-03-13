import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

urls = [
    "https://www.example.com/abc",
    "---"
]


try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.delete_all_cookies()

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Selected Options"

    sheet['A1'] = "URL"
    sheet['B1'] = "Selected State"

    row = 2

    for url in urls:
        try:
            browser.get(url)

            try:
                select_element = browser.find_element(By.CLASS_NAME, 'form-control')
            except NoSuchElementException:
                print(f"Element not found on URL: {url}")
                continue

            select = Select(select_element)

            selected_option = select.first_selected_option
            selected_text = selected_option.text

            sheet[f'A{row}'] = url
            sheet[f'B{row}'] = selected_text
            row += 1

            time.sleep(2)
        except Exception as e:
            print(f"Error processing URL {url}: {e}")

    workbook.save("selected-state.xlsx")

except Exception as e:
    print(f"An error occurred: {e}")

browser.quit()
