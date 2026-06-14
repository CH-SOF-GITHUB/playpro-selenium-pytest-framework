# from conftest import driver
from locators.cookie_locators import Locator
from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC


class Cookie(object):
    def __init__(self, driver):
        self.driver = driver
        self.cookie_btn = Wait.wait(self.driver).until((EC.element_to_be_clickable(Locator.accept_btn)))

    def close_cookie(self):
        self.cookie_btn.click()