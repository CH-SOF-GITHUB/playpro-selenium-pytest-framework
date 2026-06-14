"""
class Locator - Reservation Module: define and locate web elements using locators
"""
from selenium.webdriver.common.by import By

class Locator(object):
    # booking home page button
    booking_link = (By.LINK_TEXT, "Réserver")