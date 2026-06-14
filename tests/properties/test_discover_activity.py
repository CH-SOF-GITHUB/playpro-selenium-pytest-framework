"""
TC01: User should go to One Activity and redirect to reservation page
      using record_property and record_testsuite_property fixtures
      We identify 'Padel Court Test Tarifs Spécifiques' as an activity
"""
from time import sleep
from utils.Logger import Logger
from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_discover_activity(login, request, record_property, record_testsuite_property):
    # save global properties for test suite
    record_testsuite_property("Project", "Play-Pro-V3")
    record_testsuite_property("Environment", "QA")
    record_testsuite_property("Test Suite", "Experience Suite Test")
    # save private properties of test
    record_property("Test", "Experience Navigation")
    record_property("Priority", "High")
    record_property("Browser", "Chrome")
    record_property("Type", "Functional")
    # Locate Book Link in home page and click on it
    book_link = Wait.wait(login).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/section[1]/div[3]/div[2]/a")))
    book_link.click()
    # Locate An Example Activity Card and click on it
    activity_book_btn = Wait.wait(login).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section[1]/section[1]/div[2]/div[6]/div/div[2]/div/div[2]/div")))
    login.execute_script("arguments[0].scrollIntoView();", activity_book_btn)
    sleep(3)
    login.execute_script("arguments[0].click();", activity_book_btn)
    Logger.set_message("Activity is clicked")
    # wait for time to load page
    sleep(7)
    # assertion
    assert (login.current_url == "https://demotenant.playpro.fr/discover/reservation/padel-court-test-tarifs-specifiques") is True
    assert "padel-court-test-tarifs-specifiques" in login.current_url
    Logger.set_message(request.node.name + " OK")