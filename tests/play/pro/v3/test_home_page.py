"""
sample test google using Fixtures Test Functions
"""
import allure
from utils.Logger import Logger
from selenium.webdriver.remote.webdriver import WebDriver


@allure.title("Test home page")
@allure.description("This test attempts to access to home page and check this page")
@allure.tag("newUI", "Essentials", "Navigation")
@allure.label("Priority", "Medium")
@allure.label("tester", "Chaker Ben Said")
@allure.label("team", "QA")
@allure.label("browser", "chrome")
@allure.link("https://demotenant.playpro.fr/")
@allure.testcase("PLPRB-0001")
def test_open_home_page(driver: WebDriver):
    # Open Play Pro V3 home page
    driver.get("https://demotenant.playpro.fr/")
    expected_title = "DEMO TENANT"
    actual_title = driver.title
    Logger.set_message("Actual Title = " + actual_title)
    # pytest assert
    assert expected_title == actual_title, "Title play pro v3 page does not match"
