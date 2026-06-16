"""
sample test google using Fixtures Test Functions
"""
import logging
from selenium.webdriver.remote.webdriver import WebDriver

# define logging instance to log tests
logger = logging.getLogger(__name__)


def test_open_home_page(driver: WebDriver):
    # Open Play Pro V3 home page
    driver.get("https://demotenant.playpro.fr/")
    expected_title = "DEMO TENANT"
    actual_title = driver.title
    logger.info(actual_title)
    # pytest assert
    assert expected_title == actual_title, "Title play pro v3 page does not match"
