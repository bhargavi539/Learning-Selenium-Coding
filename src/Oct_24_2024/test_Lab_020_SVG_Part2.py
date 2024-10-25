# //*[name()='svg'] --> is the method used in XPATH selector to find svg elements
#it works only in XPATH
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)


@pytest.mark.regression
@allure.title("svg complex")
@allure.description("Verify svg in the webpage")
def test_verify_alerts():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in list_of_states:
        print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)