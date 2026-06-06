"""
sample test sample login using Fixtures Test Functions
"""
from time import sleep
import logging
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_login_01(driver):
    # Open Play Pro V3 home page
    driver.get("https://demotenant.playpro.fr/connexion")
    driver.maximize_window()
    # wait initialization
    wait = WebDriverWait(driver, 15)
    # close the cookie
    cookie_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/div/button[1]")))
    cookie_btn.click()
    # locate email and password fields
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    email_field.send_keys("demotenant3@yopmail.com")
    pwd_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    pwd_field.send_keys("Admin1234!")
    # locate login button and click on
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    # wait 7s to allow to load page
    sleep(7)
    # py.test assertion
    expected_url = "https://demotenant.playpro.fr/"
    actual_url = driver.current_url
    # pytest assert
    assert expected_url == actual_url, "Title did not match"


@pytest.mark.smoke
def test_login_02(driver):
    # Open Play Pro V3 home page
    driver.get("https://demotenant.playpro.fr/connexion")
    driver.maximize_window()
    # wait initialization
    wait = WebDriverWait(driver, 15)
    # close the cookie
    cookie_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/div/button[1]")))
    cookie_btn.click()
    # locate email and password fields
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    email_field.send_keys("demotenant3@yopmail.com")
    # locate login button and click on
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    # detect and locate error message
    required_pwd_error_field = wait.until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div[1]/form/div[3]/span")))
    # assertion of error message
    assert required_pwd_error_field.is_displayed() is True
