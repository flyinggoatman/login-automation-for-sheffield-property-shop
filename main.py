import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Load values from the .env file
load_dotenv()
login_reference = os.getenv("LOGIN_REFERENCE")
dob_day = os.getenv("DOB_DAY")
dob_month = os.getenv("DOB_MONTH")
dob_year = os.getenv("DOB_YEAR")
password = os.getenv("PASSWORD")

# Initialize Chrome driver and navigate to login page

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_service = Service(executable_path="chromedriver")
chrome_service.log_path = "NUL"
chrome_service.start()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://www.sheffieldpropertyshop.org.uk/HouseholdLogin")

# Find and fill in login reference box
login_reference_box = driver.find_element(By.ID, 'LoginReferenceField')
login_reference_box.send_keys(login_reference)

# Click login button and wait for page to load
login_button = driver.find_element(By.ID, "LoginFormSubmitButton")
login_button.click()

# Wait for date of birth fields to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "FirstPasswordField_Day")))

# Enter date of birth
dob_day_box = driver.find_element(By.ID, "FirstPasswordField_Day")
dob_month_box = driver.find_element(By.ID, "FirstPasswordField_Month")
dob_year_box = driver.find_element(By.ID, "FirstPasswordField_Year")
dob_day_box.send_keys(dob_day)
dob_month_box.send_keys(dob_month)
dob_year_box.send_keys(dob_year)

# Enter password
password_box = driver.find_element(By.ID, "SecondPasswordField")
password_box.send_keys(password)

# Click login button and wait for page to load
login_button = driver.find_element(By.ID, "LoginFormSubmitButton")
login_button.click()

# Wait for the "SocialHousing" element to load (or timeout after 10 seconds)
try:
    wait.until(EC.presence_of_element_located((By.ID, "SocialHousing")))
    print("Successfully logged in!")
    print("\a")  # Make beep sound
except:
    print("Login failed")

# Close the browser

input("Press Enter to exit and close the browser...")
driver.quit()
