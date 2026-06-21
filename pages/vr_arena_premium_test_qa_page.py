from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.vr_arena_premium_test_qa_locators import Locator

"""
Experience POM page: Vr Arena Premium Test QA
"""


class EXPVrArenaPremiumTestQA(object):
    def __init__(self, driver):
        self.driver = driver

    """
    STEP 1: Click how is the Number of Persons
    """

    def click_nb_pers_selection(self):
        nb_pers_button = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.nb_pers_button))
        nb_pers_button.click()

    """
    STEP 1: Choice of Formule Methods
    """

    def click_one_h_05_min_option(self):
        one_h_05_min_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.one_h_05_min_option))
        self.driver.execute_script("arguments[0].scrollIntoView();", one_h_05_min_option)
        self.driver.execute_script("arguments[0].click();", one_h_05_min_option)

    def click_two_h_10_min_option(self):
        two_h_10_min_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.two_h_10_min_option))
        two_h_10_min_option.click()

    """
    STEP 1: Continue Button
    """

    def click_continue_btn_step_1(self):
        continue_btn_step_1 = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.continue_btn_step_1))
        self.driver.execute_script("arguments[0].scrollIntoView();", continue_btn_step_1)
        self.driver.execute_script("arguments[0].click();", continue_btn_step_1)

    """
    STEP 2: Check Slots and Click on Confirm Btn For Example: Confirmer ma réservation- 71.1€ Soit 35.55€/pers
    """

    def click_confirm_reservation_step_2(self):
        my_reservation_confirm = Wait.wait(self.driver).until(EC.visibility_of_element_located(Locator.my_reservation_confirm))
        my_reservation_confirm.click()

    """
    STEP 3: Check Options
    """
    def click_continue_no_option_btn(self):
        continue_no_option_btn = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.continue_no_option_btn))
        self.driver.execute_script("arguments[0].scrollIntoView();", continue_no_option_btn)
        self.driver.execute_script("arguments[0].click();", continue_no_option_btn)

    """
    STEP 4: Check all steps and click to finish the reservation
    """
    def click_finish_btn_step_4(self):
        finish_btn_step_4 = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.finish_btn_step_4))
        self.driver.execute_script("arguments[0].scrollIntoView();", finish_btn_step_4)
        self.driver.execute_script("arguments[0].click();", finish_btn_step_4)