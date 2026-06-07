from selenium.webdriver.support.wait import WebDriverWait


class Wait:

    @staticmethod
    def wait(driver, timeout=15):
        return WebDriverWait(driver, timeout)
