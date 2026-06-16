from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.user_profile_locators import Locator


class UserProfile(object):
    def __init__(self, driver):
        self.driver = driver

    def click_user_profile_icon(self):
        user_profile_icon = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.user_profile_icon))
        user_profile_icon.click()

    def click_my_reservations_link(self):
        my_reservations_link = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.my_reservations_link))
        my_reservations_link.click()
