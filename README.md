# DVLA-Driving-License-Checker
Automated DVLA Driving License Checker using Selenium in Python. This Python script allows you to check the status of your driving license on the DVLA website. Before running the script, make sure to follow the instructions below:

Prerequisites
Python and Selenium: Ensure you have Python installed on your system. You’ll also need the Selenium library, which you can install using:
#####
``` pip install selenium ```
#####
Chrome WebDriver: Download the appropriate Chrome WebDriver for your system from [here](https://developer.chrome.com/docs/chromedriver/downloads). Make sure to place the WebDriver executable in the same directory as your script.
Configuration
Open the dvla_checker.py file in a text editor.
Locate the following lines in the script:
Python

### -------------------------------------------------------
### ########### Change to your information! ##############
### -------------------------------------------------------
### licence_number = "ENTER YOUR LICENCE NUMBER"
### national_insurance = "ENTER YOUR NATIONAL INSURANCE NUMBER"
### postcode = "ENTER YOUR POSTCODE"
### -------------------------------------------------------

Replace the placeholders (ENTER YOUR LICENCE NUMBER, ENTER YOUR NATIONAL INSURANCE NUMBER, and ENTER YOUR POSTCODE) with your actual information.
Running the Script
Open a terminal or command prompt.
Navigate to the directory where Simple.py is located.
Run the script using the command:
#####
```python Simple.py ```

Expected Output
If your details are correct, the script will display the status of your driving license.
If there’s an issue (e.g., incorrect details), it will print an error message.
Troubleshooting
If you encounter any errors, double-check your information (licence number, national insurance, and postcode).
Ensure that the Chrome WebDriver is in the same directory as the script.
