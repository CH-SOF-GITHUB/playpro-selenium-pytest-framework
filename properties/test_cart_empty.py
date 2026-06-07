"""
TC01: Go to panier using properties Pytest
               and using record_property fixture
"""
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

# define status of test
status = "failed"

def test_go_to_cart(driver, record_property, record_testsuite_property):
    # assign that status variable is global
    global status
    # save global properties for test suite
    record_testsuite_property("Project","Play-Pro-V3")
    record_testsuite_property("Environment", "QA")
    record_testsuite_property("Test Suite", "Cart Suite Test")
    # save private properties of test
    record_property("Test", "Cart Empty Navigation")
    record_property("Priority", "High")
    record_property("Browser", "Chrome")
    record_property("Type", "Functional")
    # Go to home page
    driver.get("https://demotenant.playpro.fr/")
    # save a private property of test
    record_property("URL", driver.current_url)
    # wait initialization
    wait = WebDriverWait(driver, 15)
    # define Actions class
    actions = ActionChains(driver)
    # close the cookie
    cookie_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/div/button[1]")))
    actions.move_to_element(cookie_btn)
    actions.click(cookie_btn)
    actions.perform()
    # locate panier web element
    panier_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='relative']")))
    actions.move_to_element(panier_icon)
    actions.click(panier_icon)
    actions.perform()
    # wait for 8s to allow to load page
    sleep(8)
    # assertion of url page
    assert (driver.current_url == "https://demotenant.playpro.fr/Panier") is True
    # set status of test
    status = "success"
    # save private properties of test
    record_property("Status", status)