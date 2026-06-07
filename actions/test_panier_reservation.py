"""
TC01: Go to panier and direct to reservation page
      Test Path: Panier > Reservation using Actions  class
"""
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import pytest

# define logging instance to log tests
logger = logging.getLogger(__name__)


@pytest.mark.dependency()
def test_panier_reservation(driver):
    # Go to home page
    driver.get("https://demotenant.playpro.fr/")
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
    logger.info("Actions Test passed")


@pytest.mark.dependency(depends=["test_panier_reservation"])
def test_discover_after_panier(driver):
    # Go to home page
    driver.get("https://demotenant.playpro.fr/")
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
    discover_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container-id']/div/div[2]/div/a")))
    actions.move_to_element(discover_btn)
    actions.click(discover_btn)
    actions.perform()
    # wait for 8s to allow to load page
    sleep(8)
    # assertion of url page
    assert (driver.current_url == "https://demotenant.playpro.fr/discover/reservation") is True
    logger.info("pytest dependency passed")
