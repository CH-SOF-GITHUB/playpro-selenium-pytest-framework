"""
Test Case ID: TC01
Objective: the system should log in with valid credentials
Design pattern: Page Object Model
Framework: Selenium + Pytest
"""

from time import sleep
from utils.Logger import Logger
from pages.cookie_page import Cookie
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import Login


def test_login_tc_01(driver: WebDriver, request):
    # open login page
    driver.get("https://demotenant.playpro.fr/connexion")
    # make an instance of login page class(s) and call method(s)
    login = Login(driver=driver)
    cookie = Cookie(driver=driver)
    # as a first test, we should close the cookie
    cookie.close_cookie()
    # send email and password
    login.type_email("demotenant3@yopmail.com")
    login.type_password("Admin1234!")
    # click on login btn
    login.click_login()
    # assertion and check if system is logging
    sleep(7)
    current_page = driver.current_url
    assert current_page == "https://demotenant.playpro.fr/"
    # display the success/fail message of test
    Logger.set_message(request.node.name + " OK")