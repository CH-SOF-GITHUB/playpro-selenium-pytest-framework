"""
class Locator - Login Module: define and locate web elements using locators
"""
from selenium.webdriver.common.by import By

class Locator(object):
    # user_profile_icon locator
    profile_icon = (By.XPATH, "/html/body/header/div/div[2]/a[3]")
    # email field
    email_field = (By.XPATH, "/html/body/div[1]/main/div[1]/form/div[1]/input")
    # password field
    pwd_field = (By.XPATH, "/html/body/div[1]/main/div[1]/form/div[2]/input")
    # login button
    login_btn = (By.XPATH, "/html/body/div[1]/main/div[1]/form/div[3]/button")
