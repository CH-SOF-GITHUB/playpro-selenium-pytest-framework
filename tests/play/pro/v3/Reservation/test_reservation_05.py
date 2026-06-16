"""
Test Case ID: TC01
Objective: User should access activity (Experience) and Execute the first STEP (Person Number & Duration/Price)
Name of Experience: VR Arena Premium Test QA
URL of Web Site: https://demotenant.playpro.fr/discover/reservation/vr-arena-premium-test-qa
Design pattern: Page Object Model
Framework: Selenium + Pytest
"""
from time import sleep
from utils.Logger import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.vr_arena_premium_test_qa_page import EXPVrArenaPremiumTestQA
from pages.reservation_page import Reservation


def test_booking_vr_arena_premium_test_qa(login: WebDriver, request):
    # make an instance of login page class(s) and call method(s)
    reservation_page = Reservation(driver=login)
    activity_page = EXPVrArenaPremiumTestQA(driver=login)
    sleep(7)
    # DEBUG
    print("URL = " + login.current_url)
    print("Page Chargée !")
    # Click on Book Link and redirect to reservation page
    reservation_page.click_booking_link()
    # wait for 7s
    sleep(7)
    # Click on Activity (Expérience) : AVRArena Premium Test QA
    reservation_page.click_activity_book_btn()
    # Wait for some time to allow to load page
    sleep(10)
    # click on number of person selection
    activity_page.click_nb_pers_selection()
    # Wait for some time
    sleep(2)
    # select one person option
    activity_page.click_one_person_option()
    # Wait for some time
    sleep(2)
    # click on duration by price selection
    activity_page.click_duration_price_selection()
    # Wait for some time
    sleep(2)
    # select 1h 05 min option
    activity_page.click_one_h_05_min_option()
    # Wait for some time
    sleep(2)
    # click on continue button
    activity_page.click_continue_btn_step_1()
    # wait 7s to allow to load page
    sleep(7)
    # assertion
    expected_text = "VR Arena Premium Test QA"
    assert expected_text == activity_page.check_name_exp_step_2()
    # Display success message if Test is passed
    Logger.set_message(request.node.name + " OK")