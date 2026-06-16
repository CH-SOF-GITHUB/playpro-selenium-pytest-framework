from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.activities_locators import Locator

"""
Experience POM page: Vr Arena Premium Test QA
"""


class EXPVrArenaPremiumTestQA(object):
    def __init__(self, driver):
        self.driver = driver

    """
    Select of Number of Persons Methods
    """

    def click_nb_pers_selection(self):
        nb_pers_selection = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.nb_pers_selection))
        nb_pers_selection.click()

    def click_one_person_option(self):
        one_person_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.one_person_option))
        one_person_option.click()

    def click_two_person_option(self):
        two_person_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.two_person_option))
        two_person_option.click()

    def click_three_person_option(self):
        three_person_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.three_person_option))
        three_person_option.click()

    def click_four_person_option(self):
        four_person_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.four_person_option))
        four_person_option.click()

    def click_five_person_option(self):
        five_person_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.five_person_option))
        five_person_option.click()

    def click_six_person_option(self):
        six_person_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.six_person_option))
        six_person_option.click()

    def click_seven_person_option(self):
        seven_person_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.seven_person_option))
        seven_person_option.click()

    def click_eight_person_option(self):
        eight_person_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.eight_person_option))
        eight_person_option.click()

    """
    Choices of Formule Methods
    """

    def click_duration_price_selection(self):
        duration_price_selection = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.duration_price_selection))
        duration_price_selection.click()

    def click_one_h_05_min_option(self):
        one_h_05_min_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.one_h_05_min_option))
        one_h_05_min_option.click()

    def click_two_h_10_min_option(self):
        two_h_10_min_option = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.two_h_10_min_option))
        two_h_10_min_option.click()

    """
    Continue Button Methods
    """

    def click_continue_btn_step_1(self):
        continue_btn_step_1 = Wait.wait(self.driver).until(EC.element_to_be_clickable(Locator.continue_btn_step_1))
        continue_btn_step_1.click()

    """
    STEP 2: <div><span>"VR Arena Premium Test QA"<div><span> Methods
    """

    def check_name_exp_step_2(self):
        div_vr_arena_premium_test_qa = Wait.wait(self.driver).until(EC.visibility_of_element_located(Locator.div_vr_arena_premium_test_qa))
        return div_vr_arena_premium_test_qa.text