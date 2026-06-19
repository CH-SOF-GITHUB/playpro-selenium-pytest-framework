"""
class Locator - Reservation Module: define and locate web elements using locators
"""
from selenium.webdriver.common.by import By

class Locator(object):
    # booking home page button
    booking_link = (By.XPATH, "//a[contains(@href,'reservation')]")
    # booking navbar button
    booking_nav_link = (By.XPATH, "//a[contains(.,'Réserver en Ligne')]")
    # Example of Activity "Padel Court Test Tarifs Spécifiques" book button
    activity_book_btn = (By.XPATH, "/html/body/div[1]/div/section[1]/section[1]/div[2]/div[11]/div/div[2]/div/div[2]/div")
    # Message of success after reservation is passed
    success_reservation_msg = (By.XPATH, "//p[@class='font-poppins font-semibold text-black md:text-xl text-sm py-6 text-center leading-4']")