"""
Test Case ID: TC01
Objective: User should access and discover reservation page
Design pattern: Page Object Model
Framework: Selenium + Pytest
"""
from time import sleep
from utils.Logger import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.reservation_page import Reservation


def test_reservation(login: WebDriver, request):
    # make an instance of login page class(s) and call method(s)
    reservation_page = Reservation(driver=login)
    # Click on Book Link and redirect to reservation page
    reservation_page.click_booking_nav_link()
    # Wait for some time to allow to load page
    sleep(8)
    # assertion
    is_booking = False
    if login.current_url == "https://demotenant.playpro.fr/discover/reservation":
        is_booking = True
    assert is_booking is True
    # display the success/fail message of test
    Logger.set_message(request.node.name + " OK")
