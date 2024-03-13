from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
import pandas as pd
from datetime import datetime

directory = 'C:/Users/Test-Scripts/Reports/Page-Speed/'

urls = [
    "https://www.google.com",
    "---"
]

try:
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.delete_all_cookies()
    browser.get("https://pagespeed.web.dev/")

    results = []


    def url_function(url):
        try:
            browser.find_element(By.CLASS_NAME, 'VfPpkd-fmcmS-wGMbrd').clear()
            time.sleep(2)
            browser.find_element(By.CLASS_NAME, 'VfPpkd-fmcmS-wGMbrd').send_keys(url)
            time.sleep(2)

            print(url)
            button = browser.find_element(By.CLASS_NAME,
                                          'VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.c659ib')
            button.send_keys(Keys.ENTER)
            time.sleep(45)

            mobile_performance = browser.find_element(By.XPATH,
                                                      '//*[@id="yDmH0d"]/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[2]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[1]/div[2]')
            text_value1 = mobile_performance.text
            variable_1 = text_value1
            time.sleep(2)

            mobile_fcp = browser.find_element(By.XPATH, '// *[ @ id = "first-contentful-paint"] / div / div[2]')
            text_value2 = mobile_fcp.text
            variable_2 = text_value2
            time.sleep(2)

            mobile_lcp = browser.find_element(By.XPATH, '//*[@id="largest-contentful-paint"]/div/div[2]')
            text_value3 = mobile_lcp.text
            variable_3 = text_value3
            time.sleep(2)

            mobile_layout_shift = browser.find_element(By.XPATH, '//*[@id="cumulative-layout-shift"]/div/div[2]')
            text_value4 = mobile_layout_shift.text
            variable_4 = text_value4
            time.sleep(2)

            desktop = browser.find_element(By.ID, "desktop_tab")
            desktop.send_keys(Keys.ENTER)
            time.sleep(2)

            desktop_performance = browser.find_element(By.XPATH,
                                                       '//*[@id="yDmH0d"]/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[3]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[1]/div[2]')
            text_value5 = desktop_performance.text
            variable_5 = text_value5
            time.sleep(5)

            desktop_fcp = browser.find_element(By.XPATH,
                                               '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[3]/span/div/div[2]/div[2]/div/div/article/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]')
            text_value6 = desktop_fcp.text
            variable_6 = text_value6
            time.sleep(2)

            desktop_lp = browser.find_element(By.XPATH,
                                              '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[3]/span/div/div[2]/div[2]/div/div/article/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]')
            text_value7 = desktop_lp.text
            variable_7 = text_value7
            time.sleep(2)

            desktop_layout_shift = browser.find_element(By.XPATH,
                                                        '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[3]/span/div/div[2]/div[2]/div/div/article/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[4]/div/div[2]')
            text_value8 = desktop_layout_shift.text
            variable_8 = text_value8
            time.sleep(2)

            browser.find_element(By.CLASS_NAME, 'gSBk9c').click()
            time.sleep(5)

            result = {"URL": url,
                      "Mobile Performance": variable_1,
                      "Mobile FCP": variable_2,
                      "Mobile LCP": variable_3,
                      "Mobile CLS": variable_4,
                      "Desktop Performance": variable_5,
                      "Desktop FCP": variable_6,
                      "Desktop LCP": variable_7,
                      "Desktop CLS": variable_8
                      }
            results.append(result)

        except NoSuchElementException:
            print(f"Element not found for URL: {url}")


    for url in urls:
        try:
            url_function(url)
        except NoSuchElementException:
            print(f"Element not found for URL: {url}")
            continue

    df = pd.DataFrame(results)
    file_name = 'Page-Speed-Report-' + datetime.now().strftime("%y-%m-%d_%H-%M-%S") + '.xlsx'
    file_path = os.path.join(directory, file_name)
    df.to_excel(file_path, index=False)
    print("Data saved to file:", file_name)

except NoSuchElementException:
    print("Element not found. Please verify selectors.")

browser.quit()
