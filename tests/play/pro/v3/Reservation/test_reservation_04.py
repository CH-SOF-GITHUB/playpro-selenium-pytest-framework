"""
Test Case ID: TC01
Objective: User should access activity (Experience) for reservation
Design pattern: Page Object Model
Framework: Selenium + Pytest
"""

from time import sleep

import pytest

from utils.Logger import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.reservation_page import Reservation


@pytest.mark.smoke
def test_open_activity_reservation(login: WebDriver, request):
    # make an instance of login page class(s) and call method(s)
    reservation_page = Reservation(driver=login)
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
    # assertion
    is_booking = False
    if login.current_url == "https://demotenant.playpro.fr/discover/reservation/vr-arena-premium-test-qa":
        is_booking = True
    assert is_booking is True
    # display the success/fail message of test
    Logger.set_message(request.node.name + " OK")
