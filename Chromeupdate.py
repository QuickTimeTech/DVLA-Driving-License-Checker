import chromedriver_autoinstaller

# This will automatically download and install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

# Now you can use ChromeDriver with Selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")
print(driver.title)
driver.quit()
