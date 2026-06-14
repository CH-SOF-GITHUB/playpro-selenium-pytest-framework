# from conftest import driver
from locators.booking_locators import Locator
from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC


class Reservation(object):
    def __init__(self, driver):
        self.driver = driver
        self.book_link = Wait.wait(driver).until((EC.element_to_be_clickable(Locator.booking_link)))

    def click_booking_link(self):
        self.book_link.click()
