"""
class Locator - Profile Module: define and locate web elements using locators
"""
from selenium.webdriver.common.by import By


class Locator(object):
    # user icon profile locator
    user_profile_icon = (By.XPATH, "/html/body/header/div/div[2]/div/button/div")
    my_reservations_link = (By.LINK_TEXT, "Mes réservations")