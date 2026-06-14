from conftest import driver
from locators.login_locators import Locator
from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC


class Login(object):
    def __init__(self, driver):
        self.driver = driver
        self.email_field = Wait.wait(self.driver).until((EC.presence_of_element_located(Locator.email_field)))
        self.pwd_field = Wait.wait(self.driver).until((EC.presence_of_element_located(Locator.pwd_field)))
        self.login_btn = Wait.wait(self.driver).until((EC.presence_of_element_located(Locator.login_btn)))

    def type_email(self, email):
        self.email_field.send_keys(email)

    def type_password(self, password):
        self.pwd_field.send_keys(password)

    def click_login(self):
        self.login_btn.click()