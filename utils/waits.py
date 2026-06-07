from selenium.webdriver.support.wait import WebDriverWait


class Wait:

    @staticmethod
    def wait(driver, timeout=25):
        return WebDriverWait(driver, timeout)
