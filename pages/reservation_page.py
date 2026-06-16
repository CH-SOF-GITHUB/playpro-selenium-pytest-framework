# from conftest import driver
from locators.booking_locators import Locator
from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC


class Reservation(object):
    def __init__(self, driver):
        self.driver = driver

    def click_booking_link(self):
        booking_link = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.booking_link))
        booking_link.click()

    def click_booking_nav_link(self):
        booking_nav_link = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.booking_nav_link))
        booking_nav_link.click()

    def click_activity_book_btn(self):
        # scroll down 500 pixels
        # self.driver.execute_script("window.scrollBy(0,500);")
        activity_book_btn = Wait.wait(self.driver).until(EC.visibility_of_element_located(Locator.activity_book_btn))
        self.driver.execute_script("arguments[0].scrollIntoView();", activity_book_btn)
        self.driver.execute_script("arguments[0].click();", activity_book_btn)
