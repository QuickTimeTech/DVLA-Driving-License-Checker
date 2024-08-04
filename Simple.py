# DVLA Driving License Checker.
# Checks the Status of your Driving License on the DVLA website.
# Made By Liam Baker.

# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# -------------------------------------------------------
############## Change to your information! ##############
# -------------------------------------------------------
licence_number = "ENTER YOUR LICENCE NUMBER"
national_insurance = "ENTER YOUR NATIONAL INSURANCE NUMBER"
postcode = "ENTER YOUR POSTCODE"
# -------------------------------------------------------

# Initialize the WebDriver (choose the appropriate driver)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Use --headless for better experience
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the DVLA webpage
driver.get("https://www.viewdrivingrecord.service.gov.uk/driving-record/licence-number")

# Find the form elements
ln = driver.find_element(By.NAME, "wizard_view_driving_licence_enter_details[driving_licence_number]")
ni = driver.find_element(By.NAME, "wizard_view_driving_licence_enter_details[national_insurance_number]")
pc = driver.find_element(By.NAME, "wizard_view_driving_licence_enter_details[post_code]")
cb = driver.find_element(By.CLASS_NAME, "govuk-checkboxes__input")
button = driver.find_element(By.NAME, "button")

# Fill in the form
ln.send_keys(licence_number)
ni.send_keys(national_insurance)
pc.send_keys(postcode)
cb.click()
button.click()

# Get the status of the driving license
try:
    lr = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/div/dl[2]/div[1]/dd")
    print(lr.text)  # Print the result
except:
    print("Element not found, Check your details are correct!")

# Close the WebDriver
driver.quit()
