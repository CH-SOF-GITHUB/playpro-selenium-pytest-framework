from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def driver(request):
    # initialize webdriver with Firefox
    _driver = webdriver.Chrome()

    # Close the driver if the test finished
    def driver_teardown():
        _driver.quit()

    request.addfinalizer(driver_teardown)
    # Hand off the driver to the test
    _driver.maximize_window()
    return _driver
