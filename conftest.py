import os

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

from utils.Logger import Logger


@pytest.fixture(scope='function')
def driver(request):
    Logger.set_message("Python Web Driver Started")
    # initialize webdriver with Chrome Options
    chrome_options = Options()
    headless = os.environ.get("headless", "false")
    if headless == "true":
        chrome_options.add_argument("--headless=new")
    # eliminate conflits permission linux
    chrome_options.add_argument("--no-sandbox")
    # prevents shared memory from becoming full
    chrome_options.add_argument("--disable-dev-shm-usage")
    # set up web driver with chrome options
    _driver = webdriver.Chrome(options=chrome_options)
    # maximize the web driver
    _driver.maximize_window()

    # Close the driver if the test finished
    def driver_teardown():
        Logger.set_message("Python Web Driver Teardown")
        _driver.quit()

    request.addfinalizer(driver_teardown)
    # Hand off the driver to the test
    return _driver
