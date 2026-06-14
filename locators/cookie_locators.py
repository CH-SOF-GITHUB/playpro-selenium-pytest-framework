"""
class Locator - Cookie Module: define and locate web elements using locators
"""
from selenium.webdriver.common.by import By

class Locator(object):
    # accepter button
    accept_btn = (By.XPATH, "/html/body/div[3]/div/div/div[4]/div/button[1]")