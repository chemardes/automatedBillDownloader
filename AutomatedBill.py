from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

import ReadPDF

file_path = r"C:\Users\LEGION\Downloads"

# setting chrome options
options = Options()
# leaves browser open even after completion
options.add_experimental_option("detach", True)
options.add_experimental_option('prefs', {
    "plugins.always_open_pdf_externally": True,
    "download_default_directory": file_path}) # change file path accordingly

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://energyonline.energia.ie/")
driver.maximize_window()

# handling cookie popup
cookie_popup = driver.find_element("xpath", "//button[@id='onetrust-accept-btn-handler']")
# waits for page to load
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(cookie_popup))
cookie_popup.click()

# automatic login
login_username = driver.find_element("xpath", "//input[@id='login-username']")
login_password = driver.find_element("xpath", "//input[@id='login-password']")
login = driver.find_element("xpath", "//button[@id='submitButton']")

login_username.send_keys("**********")
login_password.send_keys("**********")
login.click()

# downloading electricity bill
driver.implicitly_wait(5)
bill = driver.find_element("xpath", "//button[@id='last-bill-btn-link-2']")
bill.click()

# redirects user to next tab (contains the pdf file)
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])

latest_download = ReadPDF.getting_latest_downloaded_folder(file_path)
download_text = ReadPDF.extracting_text_from_pdf(latest_download)
