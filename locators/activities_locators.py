"""
class Locator - Activity / Experience: define and locate web elements using locators
                Name: vr arena premium test qa
"""
from selenium.webdriver.common.by import By


class Locator(object):
    # locate Persons Number Select field
    nb_pers_selection = (By.XPATH, "//span[normalize-space()='- Veuillez sélectionner -']")
    # locate options of persons number
    one_person_option = (By.XPATH, "//button[normalize-space()='1 personne']")
    two_person_option = (By.XPATH, "//button[normalize-space()='2 personne']")
    three_person_option = (By.XPATH, "//button[normalize-space()='3 personne']")
    four_person_option = (By.XPATH, "//button[normalize-space()='4 personne']")
    five_person_option = (By.XPATH, "//button[normalize-space()='5 personne']")
    six_person_option = (By.XPATH, "//button[normalize-space()='6 personne']")
    seven_person_option = (By.XPATH, "//button[normalize-space()='7 personne']")
    eight_person_option = (By.XPATH, "//button[normalize-space()='8 personne']")
    # locate Duration/price Select field
    duration_price_selection = (By.XPATH, "//span[normalize-space()='Sélectionner une formule']")
    # locate options of duration by price
    one_h_05_min_option = (By.XPATH, "//button[normalize-space()='1h 05 min']")
    two_h_10_min_option = (By.XPATH, "//button[normalize-space()='2h 10 min']")
    # locate Continue button
    continue_btn_step_1 = (By.XPATH, "//button[@class='relative w-full lg:w-1/3 h-[50px] rounded-md px-[15px] lg:text-lg lg:px-0 lg:py-1 py-[7px] gap-[10px] opacity-100 border bg-secondary']")
    # web elements locators
    div_vr_arena_premium_test_qa = (By.XPATH, "//div[@role='button']//div[2]")
