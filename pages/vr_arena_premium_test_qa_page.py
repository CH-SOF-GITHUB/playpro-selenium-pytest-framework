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
    STEP 2: <div><span>"VR Arena Premium Test QA"<div><span> Methods
    """

    def check_name_exp_step_2(self):
        div_vr_arena_premium_test_qa = Wait.wait(self.driver).until(
            EC.visibility_of_element_located(Locator.div_vr_arena_premium_test_qa))
        return div_vr_arena_premium_test_qa.text

    """
    STEP 2: Check Slots and Click on Confirm Btn
    """

    def click_confirm_btn_step_2(self):
        my_reservation_confirm = Wait.wait(self.driver).until(
            EC.visibility_of_element_located(Locator.my_reservation_confirm))
        my_reservation_confirm.click()

    def click_next_btn_step_2(self):
        # self.driver.execute_script("window.scrollBy(0,700);")
        next_button_step_2 = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.next_button_step_2))
        self.driver.execute_script("arguments[0].scrollIntoView();", next_button_step_2)
        self.driver.execute_script("arguments[0].click();", next_button_step_2)
        # next_button_step_2.click()

    def click_continue_no_option_btn(self):
        # self.driver.execute_script("window.scrollBy(0,1000);")
        continue_no_option_btn = Wait.wait(self.driver).until(
            EC.element_to_be_clickable(Locator.continue_no_option_btn))
        self.driver.execute_script("arguments[0].scrollIntoView();", continue_no_option_btn)
        self.driver.execute_script("arguments[0].click();", continue_no_option_btn)
        # continue_no_option_btn.click()
