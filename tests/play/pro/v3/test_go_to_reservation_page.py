from time import sleep

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.waits import Wait
from utils.Logger import Logger
from selenium.webdriver.remote.webdriver import WebDriver

"""
TC01: User should access to reservation page simplify and easy.
      Expected URL: https://demotenant.playpro.fr/discover/reservation
"""


def test_go_to_discover_reservation(login: WebDriver, request):
    reserver_link = Wait.wait(login).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/section[1]/div[3]/div[2]/a")))
    reserver_link.click()
    # wait for 7s to allow to load page
    sleep(7)
    # assertion
    assert (login.current_url == "https://demotenant.playpro.fr/discover/reservation") is True
    Logger.set_message(request.node.name + " OK")
