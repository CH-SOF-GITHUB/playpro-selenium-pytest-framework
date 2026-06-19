"""
class Locator - Activity / Experience: define and locate web elements using locators
                Name: vr arena premium test qa
"""
from selenium.webdriver.common.by import By


class Locator(object):
    # locate Bank Carte Stripe
    carte_bank_4242 = (By.XPATH, "//div[@id='headlessui-disclosure-button-:r18:']//span[@class='md:w-5 w-4 md:h-5 h-4 border-2 border-black rounded-full']")
    # locate payment button
    payment_btn = (By.XPATH, "//button[normalize-space()='Payer maintenant']")
