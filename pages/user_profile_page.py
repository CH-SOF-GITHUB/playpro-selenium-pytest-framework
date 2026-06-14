from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.user_profile_locators import Locator


class UserProfile(object):
    def __init__(self, driver):
        self.driver = driver
        self.user_profile_icon = Wait.wait(driver).until((EC.element_to_be_clickable(Locator.user_profile_icon)))
        self.my_reservations_link = Wait.wait(driver).until((EC.element_to_be_clickable(Locator.my_reservations_link)))

    def click_user_profile_icon(self):
        self.driver.execute_script("arguments[0].click();", self.user_profile_icon.click())

    def click_my_reservations_link(self):
        self.driver.execute_script("arguments[0].click();", self.my_reservations_link)
