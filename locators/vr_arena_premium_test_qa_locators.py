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
    # locate Continue button
    continue_btn_step_1 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[5]/div/button")
    # web elements locators
    #div_vr_arena_premium_test_qa = (By.XPATH, "//div[@role='button']//div[2]")
    # ma réservation- {price}€Confirmer locator
    #my_reservation_confirm = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/button[1]")
    # Suivant button locator
    #next_button_step_2 = (By.XPATH, "//button[normalize-space()='Suivant']")
    # Continue without option button locator
    #continue_no_option_btn = (By.XPATH, "//button[normalize-space()='Continuer sans option']")