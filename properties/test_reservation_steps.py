"""
TC01: access to activity reservation page and follow all steps, finally our goal
      is to create a reservation
      for example: 'Padel Court Test Tarifs Spécifiques'
"""
from time import sleep
from utils.Logger import Logger
from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_reservation_steps(driver, request, record_property, record_testsuite_property):
    # save global properties for test suite
    record_testsuite_property("Project", "Play-Pro-V3")
    record_testsuite_property("Environment", "QA")
    record_testsuite_property("Test Suite", "Experience Suite Test")
    # save private properties of test
    record_property("Test", "Experience Navigation")
    record_property("Priority", "High")
    record_property("Browser", "Chrome")
    record_property("Type", "Functional")
    record_property("URL", driver.current_url)
    # Locate Book Link in home page and click on it
    book_link = Wait.wait(driver).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/section[1]/div[3]/div[2]/a")))
    book_link.click()
    # Locate Activity Card and click on it
    activity_book_btn = Wait.wait(driver).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section[1]/section[1]/div[2]/div[1]/div/div[2]/div/div[2]/div")))
    driver.execute_script("arguments[0].scrollIntoView();", activity_book_btn)
    sleep(3)
    driver.execute_script("arguments[0].click();", activity_book_btn)
    Logger.set_message("Activity is clicked")
    # wait for time to load page
    sleep(10)
    # Locate Continue btn and click on it
    continue_btn = Wait.wait(driver).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/button[1]")))
    continue_btn.click()
    # Locate Slot and click on it
    slot_07_30 = Wait.wait(driver).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div[2]/div[2]/button")))
    driver.execute_script("arguments[0].scrollIntoView();", slot_07_30)
    sleep(3)
    driver.execute_script("arguments[0].click();", slot_07_30)
    # Locate confirm my reservation btn and click on it
    confirm_btn = Wait.wait(driver).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/button[1]")))
    driver.execute_script("arguments[0].click();", confirm_btn)
    # Wait Time to load page payment
    sleep(10)
    # assertion
    assert (driver.current_url == "https://demotenant.playpro.fr/Panier") is True
    Logger.set_message(request.node.name + " OK")