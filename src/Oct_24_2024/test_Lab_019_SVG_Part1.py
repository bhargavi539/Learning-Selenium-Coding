# //*[name()='svg'] --> is the method used in XPATH selector to find svg elements
#it works only in XPATH

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.mark.regression
@allure.title("svg")
@allure.description("Verify svg search button in the webpage")
def test_verify_alerts():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    search_box = driver.find_element(By.NAME,"q")
    search_box.send_keys("macmini")

    list_of_svg_elements = driver.find_elements(By.XPATH,"//*[name()='svg']")
    list_of_svg_elements[0].click()
