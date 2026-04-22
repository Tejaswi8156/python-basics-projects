from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

EMAIL = "tejaswi.2ndry@gmail.com"
PASSWORD = "Unused123@"
POST_TEXT = "Hello This is an automated Facebook post using Python Selenium."

# ---------- CHROME SETUP ----------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 40)

# ---------- LOGIN ----------
driver.get("https://www.facebook.com/login")
time.sleep(5)

wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(EMAIL)
driver.find_element(By.NAME, "pass").send_keys(PASSWORD + Keys.ENTER)

time.sleep(20)  # VERY IMPORTANT

# ---------- CLICK "WHAT'S ON YOUR MIND, SELENIUM?" ----------
mind_box = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//span[contains(text(),\"What's on your mind\")]"
    ))
)
mind_box.click()

time.sleep(5)

# ---------- WAIT FOR REAL TEXTBOX ----------
textbox = wait.until(
    EC.presence_of_element_located((
        By.XPATH,
        "//div[@role='textbox']"
    ))
)
textbox.send_keys(POST_TEXT)

time.sleep(3)

# ---------- CLICK POST ----------
post_button = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//div[@aria-label='Post']"
    ))
)
post_button.click()

time.sleep(5)

print("✅ Facebook post successfully uploaded")
driver.quit()
