"""
class Locator - Reservation Module: define and locate web elements using locators
"""
from selenium.webdriver.common.by import By

class Locator(object):
    # booking home page button
    booking_link = (By.XPATH, "//a[contains(@href,'reservation')]")
    # booking navbar button
    booking_nav_link = (By.XPATH, "//a[contains(.,'Réserver en Ligne')]")
    # Example of Activity book button
    activity_book_btn = (By.XPATH, "/html/body/div[1]/div/section[1]/section[1]/div[2]/div[3]/div/div[2]/div/div[2]/div")