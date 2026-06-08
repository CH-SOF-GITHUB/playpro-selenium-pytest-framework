import os
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from utils.Logger import Logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='session')
def driver(request):
    Logger.set_message("Python Web Driver Started")
    # initialize webdriver with Chrome Options
    chrome_options = Options()
    headless = os.environ.get("headless", "false")
    if headless == "true":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
    # eliminate conflits permission linux
    chrome_options.add_argument("--no-sandbox")
    # prevents shared memory from becoming full
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    # set up web driver with chrome options
    _driver = webdriver.Chrome(options=chrome_options)
    """
    if headless == "true":
        _driver.set_window_size(1920, 1080)
    else:
        # maximize the web driver
        _driver.maximize_window()
    """
    Logger.set_message("window size: " + str(_driver.get_window_size()))

    # Close the driver if the test finished
    def driver_teardown():
        Logger.set_message("Python Web Driver Teardown")
        _driver.quit()

    request.addfinalizer(driver_teardown)
    # Hand off the driver to the test
    return _driver


"""
Pytest - Fixture of login : we needed before each another test
La fixture driver est maintenant à scope='session', donc le WebDriver est lancé une seule fois par session de test.

La fixture setup est autouse=True, donc elle s'exécute automatiquement avant chaque test pour ouvrir la page, accepter cookies, 
et faire le login.

La fonction pytest_sessionstart n'est plus utilisée, ce qui évite l'erreur de hook.
"""


@pytest.fixture(scope='function', autouse=True)
def login(driver):
    Logger.set_message("Python Web Driver & Pytest Session Start")
    # Open Play Pro V3 home page
    driver.get("https://demotenant.playpro.fr/connexion")
    # wait initialization
    wait = WebDriverWait(driver, 25)
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
    Logger.set_message("Login Successful")
