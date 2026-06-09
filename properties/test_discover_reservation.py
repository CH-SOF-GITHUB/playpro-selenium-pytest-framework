"""
TC01: Go to reservation page using properties Pytest
               and using {record_property, record_testsuite_property} fixtures
"""
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.waits import Wait
from utils.Logger import Logger


def test_reservation(driver, request, record_property, record_testsuite_property):
    # save global properties for test suite
    record_testsuite_property("Project", "Play-Pro-V3")
    record_testsuite_property("Environment", "QA")
    record_testsuite_property("Test Suite", "Cart Suite Test")
    # save private properties of test
    record_property("Test", "Cart Empty Navigation")
    record_property("Priority", "High")
    record_property("Browser", "Chrome")
    record_property("Type", "Functional")
    record_property("URL", driver.current_url)
    reserver_link = Wait.wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/section[1]/div[3]/div[2]/a")))
    reserver_link.click()
    # wait for 10s to allow to load page
    sleep(10)
    # assertion
    assert (driver.current_url == "https://demotenant.playpro.fr/discover/reservation") is True
    Logger.set_message(request.node.name + " OK")