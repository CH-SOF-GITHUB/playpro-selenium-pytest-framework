"""
TC01: Go to panier using properties Pytest
               and using {record_property, record_testsuite_property}
               fixtures
"""
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.waits import Wait
from utils.Logger import Logger
from selenium.webdriver.chrome.webdriver import WebDriver


def test_go_to_empty_cart(login: WebDriver, request, record_property, record_testsuite_property):
    # save global properties for test suite
    record_testsuite_property("Project", "Play-Pro-V3")
    record_testsuite_property("Environment", "QA")
    record_testsuite_property("Test Suite", "Cart Suite Test")
    # save private properties of test
    record_property("Test", "Cart Empty Navigation")
    record_property("Priority", "High")
    record_property("Browser", "Chrome")
    record_property("Type", "Functional")
    # locate panier web element
    panier_icon = Wait.wait(login).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div[2]/a[2]")))
    login.execute_script("arguments[0].scrollIntoView();", panier_icon)
    login.execute_script("arguments[0].click();", panier_icon)
    # wait for 25 s to allow to load page
    sleep(25)
    # assertion of url page
    assert (login.current_url == "https://demotenant.playpro.fr/Panier") is True
    Logger.set_message(request.node.name + " OK")
