"""
sample test login parametrized using Fixtures Test Functions


import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

chrome_driver = webdriver.Chrome()
firefox_driver = webdriver.Firefox()


@pytest.mark.parametrize('parallel_driver', [chrome_driver, firefox_driver])
def test_login_cross_browser(parallel_driver):
    # Open Play Pro V3 home page
    parallel_driver.get("https://demotenant.playpro.fr/connexion")
    # parallel_driver.maximize_window()
    # wait initialization
    wait = WebDriverWait(parallel_driver, 15)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    assert email_field.is_displayed() is True
    # close the web driver and finish the test
    parallel_driver.quit()
"""