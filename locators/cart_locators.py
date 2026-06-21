"""
class Locator - Activity / Experience: define and locate web elements using locators
                Name: vr arena premium test qa
"""
from selenium.webdriver.common.by import By


class Locator(object):
    # locate Bank Carte Stripe
    carte_bank_4242 = (By.XPATH, "/html/body/div[1]/section/div[2]/div/div/div[1]/div/div[1]/div[1]/div")
    # locate payment button
    payment_btn = (By.XPATH, "//button[normalize-space()='Payer maintenant']")
