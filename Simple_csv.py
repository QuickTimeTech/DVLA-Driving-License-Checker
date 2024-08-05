# DVLA Driving License Checker.
# Checks the Status of your Driving License on the DVLA website.
# Made By Liam Baker.

# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime

# -------------------------------------------------------
############## Change to your information! ##############
# -------------------------------------------------------
licence_number = "ENTER YOUR LICENCE NUMBER"
national_insurance = "ENTER YOUR NATIONAL INSURANCE NUMBER"
postcode = "ENTER YOUR POSTCODE"
# -------------------------------------------------------

# Define a function to append data to a CSV file
def append_to_csv(value):
    # Get the current date and time
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')

    # Create a DataFrame with the data
    data = {'Date': [current_date], 'Time': [current_time], 'Result': [value]}
    df = pd.DataFrame(data)

    # Append the DataFrame to the existing CSV file
    df.to_csv('output.csv', mode='a', index=False, header=False)

# Initialize the WebDriver (choose the appropriate driver)
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Use --headless=new for better experience
driver = webdriver.Chrome(options=chrome_options)

# Navigate to a webpage
driver.get("https://www.viewdrivingrecord.service.gov.uk/driving-record/licence-number")

# Find the elements in the form
ln = driver.find_element(By.NAME, "wizard_view_driving_licence_enter_details[driving_licence_number]")
ni = driver.find_element(By.NAME, "wizard_view_driving_licence_enter_details[national_insurance_number]")
pc = driver.find_element(By.NAME, "wizard_view_driving_licence_enter_details[post_code]")
cb = driver.find_element(By.CLASS_NAME, "govuk-checkboxes__input")
button = driver.find_element(By.NAME, "button")

# Perform actions on the elements (e.g., send keys and click)
try:
    ln.send_keys(licence_number)
    ni.send_keys(national_insurance)
    pc.send_keys(postcode)
    cb.click()
    button.click()
except TimeoutException:
    print("Element not found or not clickable within the specified timeout.")

# Load the new page and get the Status of the Driving license
try:
    # Find the element by XPATH
    lr = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/div/dl[2]/div[1]/dd")
    print(lr.text)
    # Log the Result to a CSV file
    append_to_csv(lr.text)
except:
    print("Element not found, Check your deails are correct!")
    # Log the Result to a CSV file
    append_to_csv("Element not found, Check your deails are correct!")

# Remember to close the WebDriver when done
driver.quit()
