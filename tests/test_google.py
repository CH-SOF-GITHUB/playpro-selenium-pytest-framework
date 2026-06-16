"""
sample test google using Fixtures Test Functions
"""
from utils.Logger import Logger
from selenium.webdriver.remote.webdriver import WebDriver

def test_google_search(driver:WebDriver):
    # Open Google
    driver.get('https://www.google.com')
    # Wait for the results to load and display the title
    driver.implicitly_wait(5)  # Wait for 5 seconds
    Logger.set_message(driver.title)
