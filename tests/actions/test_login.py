from time import sleep

from selenium.webdriver import ActionChains
from utils.waits import Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_sample_login(driver):
    # Go to home page
    driver.get("https://demotenant.playpro.fr/")
    # Define actions class
    actions = ActionChains(driver)
    # close the cookie
    cookie_btn = Wait.wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/div/button[1]")))
    actions.move_to_element(cookie_btn)
    actions.click(cookie_btn)
    actions.perform()
    # Go the login page
    login_icon = Wait.wait(driver).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div[2]/a[3]")))
    actions.move_to_element(login_icon)
    actions.click(login_icon)
    actions.perform()
    # Locate Email and Password fields
    email_field = Wait.wait(driver).until(EC.visibility_of_element_located((By.NAME, "email")))
    actions.click(email_field).send_keys("demotenant3@yopmail.com").perform()
    pwd_field = Wait.wait(driver).until(EC.visibility_of_element_located((By.NAME, "password")))
    actions.click(pwd_field).send_keys("Admin1234!").perform()
    # Locate Login Btn and click on it
    login_btn = Wait.wait(driver).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    actions.move_to_element(login_btn)
    actions.click(login_btn)
    actions.perform()
    # sleep 7s
    sleep(7)
    # Assertion
    assert (driver.current_url == "https://demotenant.playpro.fr/") is True