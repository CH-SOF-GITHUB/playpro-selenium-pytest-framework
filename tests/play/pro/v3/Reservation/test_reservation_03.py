"""
Test Case ID: TC01
Objective: User should access his orders by Profile
Design pattern: Page Object Model
Framework: Selenium + Pytest
"""

from time import sleep
from utils.Logger import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.user_profile_page import UserProfile


def test_check_my_orders_in_profile(login: WebDriver, request):
    # make an instance of login page class(s) and call method(s)
    user_profile_page = UserProfile(driver=login)
    # click on user profile icon
    user_profile_page.click_user_profile_icon()
    # click on my orders link
    user_profile_page.click_my_reservations_link()
    # Wait for some time to allow to load page
    sleep(7)
    # assertion
    is_booking = False
    if login.current_url == "https://demotenant.playpro.fr/profile?tab=reservations":
        is_booking = True
    assert is_booking is True
    # display the success/fail message of test
    Logger.set_message(request.node.name + " OK")