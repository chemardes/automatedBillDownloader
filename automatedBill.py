from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# setting chrome options
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
driver.find_element("xpath", "//input[@id='login-username']").send_keys("*************")
driver.find_element("xpath", "//input[@id='login-password']").send_keys("*************")
driver.find_element("xpath", "//button[@id='submitButton']").click()

# downloading electricity bill
driver.find_element("xpath", "//button[@id='last-bill-btn-link-2']").click()

# redirects user to next tab (contains the pdf file)
driver.switch_to.window(driver.window_handles[1])
driver.find_element("xpath", "//cr-icon-button[@id='download']").click()


