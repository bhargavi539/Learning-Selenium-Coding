from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure


@pytest.mark.negative
@allure.title("Positive Testcase - App.vwo.com Singup Button Verification. ")
@allure.description("Verify that FREE Trail button is clicked, Navigated to the signup page")
def test_start_a_trail_vwo_negative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    time.sleep(3)
    #LINK_TEXT -> Exact Match
    #start_trail_anchor_tag =driver.find_element(By.LINK_TEXT,"Start a free trial")
    #start_trail_anchor_tag.click()

    #PARTIAL_LINK_TEXT -> contains
    start_trail_anchor_tag =driver.find_element(By.PARTIAL_LINK_TEXT,"Start a free trial")
    start_trail_anchor_tag.click()
    time.sleep(3)

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
