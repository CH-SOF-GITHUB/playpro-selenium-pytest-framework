"""
class Locator - Profile Module: define and locate web elements using locators
"""
from selenium.webdriver.common.by import By


class Locator(object):
    # User menu
    user_profile_icon = (By.XPATH, "/html/body/header/div/div[2]/div/button/div")
    # Link my reservations in sub-menu
    my_reservations_link = (By.LINK_TEXT, "Mes réservations")