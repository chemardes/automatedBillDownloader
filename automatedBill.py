from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# leaves browser open even after completion
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://energyonline.energia.ie/")
driver.maximize_window()

# waits for page to load
driver.implicitly_wait(5)

# handling cookie popups
driver.find_element("xpath", "//button[@id='onetrust-accept-btn-handler']").click()

# automatic login
driver.find_element("xpath", "//input[@id='login-username']").send_keys("marco04divaio@yahoo.com")
driver.find_element("xpath", "//input[@id='login-password']").send_keys("141577mcM%@%@@")
driver.find_element("xpath", "//button[@id='submitButton']").click()

# downloading electricity bill
driver.find_element("xpath", "//button[@id='last-bill-btn-link-2']").click();

