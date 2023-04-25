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
postcode = os.getenv("POSTCODE")

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


try:
    wait.until(EC.presence_of_element_located((By.ID, "SocialHousing")))
    print("Successfully logged in!")
    print("\a")  # Make beep sound
except:
    print("Login failed")



# Wait for the "Eligible properties" element to load (or timeout after 10 seconds)
wait.until(EC.presence_of_element_located((By.XPATH, "//a[@title='Eligible properties']")))

# Find the "Eligible properties" element
eligible_properties_element = driver.find_element(By.XPATH, "//a[@title='Eligible properties']")


# Extract the number of eligible properties
eligible_properties_count = int(eligible_properties_element.find_element(By.CSS_SELECTOR, ".number").text)
print("Number of eligible properties:", eligible_properties_count)

# Click on the "Eligible properties" element
eligible_properties_element.click()

# Find and fill in the input box with the id ChangeSearchLocationAttemptedLocationName
location_input = driver.find_element(By.ID, "ChangeSearchLocationAttemptedLocationName")
location_input.send_keys(postcode)

# Select the option value 1 (1 mile) in the dropdown box with the id SearchRadius
search_radius_dropdown = driver.find_element(By.ID, "SearchRadius")
search_radius_options = search_radius_dropdown.find_elements(By.TAG_NAME, "option")
search_radius_options[1].click()  # Option value 1 corresponds to the second option (1 mile)

# Find and click on the button with the id SearchLocationDistanceButton
search_location_distance_button = driver.find_element(By.ID, "SearchLocationDistanceButton")
search_location_distance_button.click()
...


# Wait for the list to load
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "advert-address-container")))

# Check if the overlay pops up
overlay_present = EC.presence_of_element_located((By.ID, "ChangeSearchLocationNoLocationModalBody"))
try:
    wait.until(overlay_present, timeout=5)

    # If the overlay appears, click the Close button
    close_button = driver.find_element(By.XPATH, "//button[@data-dismiss='modal' and contains(@class, 'btn btn-default')]")
    close_button.click()

    # Select the next option up (2 miles) in the dropdown box with the id SearchRadius
    search_radius_options[2].click()

    # Click on the button with the id SearchLocationDistanceButton again
    search_location_distance_button.click()

    # Wait for the list to be updated
    wait.until(EC.staleness_of(driver.find_element(By.CLASS_NAME, "advert-address-container")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "advert-address-container")))



    # Find all address elements
    address_elements = driver.find_elements(By.CLASS_NAME, "advert-address-container")

    # Check if the overlay pops up again
    try:
        wait.until(overlay_present, timeout=5)
        if overlay_present:
            print("No local homes found")
            for index, address_element in enumerate(address_elements):
                address_text = address_element.text.strip()
                print(f"Address {index + 1}: {address_text}")
        print("No local homes found")
        for index, address_element in enumerate(address_elements):
            address_text = address_element.text.strip()
            print(f"Address {index + 1}: {address_text}")
    except:
        print("Local homes within two miles found")
        for index, address_element in enumerate(address_elements):
            address_text = address_element.text.strip()
            print(f"Address {index + 1}: {address_text}")
        pass
except:
    print("Local homes within one mile found")
    pass

# Wait for the dropdown with the menu id Arrange to load
wait.until(EC.presence_of_element_located((By.ID, "Arrange")))

# Select option 0 (Closest first) in the dropdown with the id Arrange
arrange_dropdown = driver.find_element(By.ID, "Arrange")
arrange_options = arrange_dropdown.find_elements(By.TAG_NAME, "option")
arrange_options[0].click()  # Option value 0 corresponds to the first option (Closest first)

# Wait for at least one address element to load (or timeout after 10 seconds)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "advert-address-container")))


# Loop through the address elements and print the address text for each one

    


# Wait for the "SocialHousing" element to load (or timeout after 10 seconds)


# Close the browser

input("Press Enter to exit and close the browser...")
driver.quit()
