import glob
import os
import re

from PyPDF2 import PdfReader
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# importing environment variables
load_dotenv()

# setting environment variables
file_path = os.getenv("FILE_PATH")
login_username = os.getenv("LOGIN_USERNAME")
login_password = os.getenv("LOGIN_PASSWORD")


def get_driver():
    # setting chrome options
    options = Options()
    # leaves browser open even after completion
    options.add_experimental_option("detach", True)
    options.add_experimental_option('prefs', {
        "plugins.always_open_pdf_externally": True,
        "download_default_directory": file_path,
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}]
        # prevents file from opening automatically
    })

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)
    return driver


def getting_latest_downloaded_folder(self):
    # function to get the latest downloaded pdf file in folder
    # passes the download folder path as a parameter

    # returns the file path of the pdf file
    file_list = glob.glob(self + "/*.pdf")
    latest_file = max(file_list, key=os.path.getmtime)
    return latest_file


def extracting_amount_due_from_pdf(path):
    reader = PdfReader(path)
    text = reader.pages[0].extract_text()

    # checks for the presence of keyword (specified by the RegEx)
    pattern = re.compile(r'(€[\d.,]+) Amount due')
    match = pattern.search(text)

    # returns amount due if keyword is found
    if match:
        amount = match.group(0)  # match.group(1) gives the 1st parenthesized value so (€0.75)
        return amount
    else:
        return "No matching amount found in text file."


def automate_download(driver):
    driver.get("https://energyonline.energia.ie/")
    # handling cookie popup
    driver.implicitly_wait(5)
    # waits for button to be clickable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(("xpath", "//button[@id='onetrust-accept-btn-handler']")))
    driver.find_element("xpath", "//button[@id='onetrust-accept-btn-handler']").click()

    # automatic login
    driver.find_element("xpath", "//input[@id='login-username']").send_keys(login_username)
    driver.find_element("xpath", "//input[@id='login-password']").send_keys(login_password)
    driver.find_element("xpath", "//button[@id='submitButton']").click()

    # downloading electricity bill
    driver.implicitly_wait(5)
    # waits for button to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//button[@id='last-bill-btn-link-2']")))
    driver.find_element("xpath", "//button[@id='last-bill-btn-link-2']").click()

    # redirects user to next tab (contains the pdf file)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    latest_download = getting_latest_downloaded_folder(file_path)
    return latest_download


def main():
    driver = get_driver()
    latest_download = automate_download(driver)
    amount_due = extracting_amount_due_from_pdf(latest_download)
    print(amount_due)
    driver.quit()


if __name__ == '__main__':
    main()
