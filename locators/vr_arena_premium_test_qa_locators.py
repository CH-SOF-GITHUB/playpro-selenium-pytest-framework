"""
class Locator - Activity / Experience: define and locate web elements using locators
                Name: vr arena premium test qa
"""
from selenium.webdriver.common.by import By


class Locator(object):
    # locate Persons Number (+ / -) button
    nb_pers_button = (By.XPATH, "(//button[contains(@class,'border rounded-[10px] w-[40px] p-2 #FFFFFF flex justify-center items-center cursor-pointer')])[1]")
    # locate options of duration by price
    one_h_05_min_option = (By.XPATH, "(//p[normalize-space()='1h 05 min'])[1]")
    two_h_10_min_option = (By.XPATH, "(//p[normalize-space()='2h 10 min'])[1]")
    # locate Continue button locator
    continue_btn_step_1 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[5]/div/button")
    # ma réservation- {price}€Confirmer button locator
    my_reservation_confirm = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[5]/div/button[1]")
    # Continue without option button locator
    continue_no_option_btn = (By.XPATH, "//button[normalize-space()='Continuer sans option']")
    # Finish button locator
    finish_btn_step_4 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[5]/div/button[1]")