"""
sample test google using Fixtures Test Functions
"""


def test_open_home_page(driver):
    # Open Play Pro V3 home page
    driver.get("https://demotenant.playpro.fr/")
    expected_title = "DEMO TENANT"
    actual_title = driver.title
    # pytest assert
    assert expected_title == actual_title, "Title did not match"
