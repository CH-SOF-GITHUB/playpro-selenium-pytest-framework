"""
Test Case ID: TC01
Objective: User should access activity (Experience) and Execute the first STEP (Person Number & Duration/Price)
Name of Experience: VR Arena Premium Test QA
URL of Web Site: https://demotenant.playpro.fr/discover/reservation/vr-arena-premium-test-qa
Design pattern: Page Object Model
Framework: Selenium + Pytest
"""
import random
from time import sleep
from utils.Logger import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.vr_arena_premium_test_qa_page import EXPVrArenaPremiumTestQA
from pages.panier_page import Panier
from pages.reservation_page import Reservation
from utils.waits import Wait
from selenium.webdriver.common.by import By


def test_booking_vr_arena_premium_test_qa(login: WebDriver, request):
    # make an instance of pom class(s) and call method(s)
    reservation_page = Reservation(driver=login)
    this_activity_page = EXPVrArenaPremiumTestQA(driver=login)
    panier_page = Panier(driver=login)
    sleep(7)
    # DEBUG
    print("\nURL = " + login.current_url)
    print("\nPage Chargée !")
    # Click on Book Link and redirect to reservation page
    reservation_page.click_booking_link()
    # wait for 7s
    sleep(7)
    # Click on Activity (Expérience) : AVRArena Premium Test QA
    reservation_page.click_activity_book_btn()
    # Wait for some time to allow to load page
    sleep(10)
    # click on number of person
    this_activity_page.click_nb_pers_selection()
    # Wait for some time
    sleep(2)
    # select 1h 05 min option
    this_activity_page.click_one_h_05_min_option()
    # Wait for some time
    sleep(2)
    # Click on continue button step 1
    this_activity_page.click_continue_btn_step_1()
    # wait 7s to allow to load page
    sleep(7)
    # Define a table to stock the slots
    available_slots = []
    # Locate all Slots to click on it after
    Wait.wait(login).until(lambda d: len(d.find_elements(By.XPATH, "//button[@type='button']//div[@class='flex justify-center items-center']")) > 0)
    slots = login.find_elements(By.XPATH, "//button[@type='button']//div[@class='flex justify-center items-center']")
    for slot in slots:
        if "Complet" not in slot.text:
            available_slots.append(slot)
    # display text of table slots
    for slot in available_slots:
        Logger.set_message("slot: \n" + slot.text)
    # Define the slot to be clicked
    selected_slot = random.choice(available_slots)
    # Use JavaScript to click force on selected slot
    login.execute_script("arguments[0].scrollIntoView();", selected_slot)
    login.execute_script("arguments[0].click();", selected_slot)
    # wait for 3 s
    sleep(3)
    # Click on confirm reservation button
    this_activity_page.click_confirm_reservation_step_2()
    # Wait for 7 s  to allow to page
    sleep(7)
    # Click on Continue without option button
    this_activity_page.click_continue_no_option_btn()
    # wait for 7 s
    sleep(7)
    # Click on finish reservation button
    this_activity_page.click_finish_btn_step_4()
    # wait for 7 s
    sleep(7)
    # assertion
    expected_url = "https://demotenant.playpro.fr/Panier"
    actual_url = login.current_url
    in_cart = False
    if expected_url in actual_url:
        in_cart = True
    assert in_cart is True
    # Click on STRIPE Carte 4242
    panier_page.click_on_cb_stripe_4242()
    # Click on Payment button
    panier_page.click_on_payment_btn()
    # Wait for time 10 s to allow to load page
    sleep(10)
    # assertion
    actual_msg = reservation_page.check_success_reservation_msg()
    assert "Merci pour votre réservation ! 🎉" == actual_msg
    # print a success message if test is passed
    Logger.set_message(request.node.name + " OK")