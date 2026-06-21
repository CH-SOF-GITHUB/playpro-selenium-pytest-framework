from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.cart_locators import Locator


class Panier(object):
    def __init__(self, driver):
        self.driver = driver

    def click_on_cb_stripe_4242(self):
        carte_bank_4242 = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.carte_bank_4242))
        carte_bank_4242.click()

    def click_on_payment_btn(self):
        payment_now_btn = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.payment_btn))
        self.driver.execute_script("arguments[0].scrollIntoView();", payment_now_btn)
        self.driver.execute_script("arguments[0].click();", payment_now_btn)