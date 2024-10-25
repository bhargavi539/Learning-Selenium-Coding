from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)


@pytest.mark.regression
@allure.title("Alerts")
@allure.description("Verify alerts in the webpage")
def test_verify_alerts():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    alert_element = driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    alert_element.click()

    WebDriverWait(driver=driver,timeout=5).until(expected_conditions.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    result_in_text = driver.find_element(By.ID,"result").text
    assert result_in_text == "You successfully clicked an alert"


@pytest.mark.regression
@allure.title("Verify Confirm alert button")
@allure.description("Verify confirm alert in the webpage")
def test_verify_confirm():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    confirm_element = driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    confirm_element.click()

    WebDriverWait(driver=driver,timeout=5).until(expected_conditions.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()
    result_in_text = driver.find_element(By.ID,"result").text
    assert result_in_text == "You clicked: Cancel"


@pytest.mark.regression
@allure.title("Verify Prompt alert button")
@allure.description("Verify prompt button in the webpage")
def test_verify_confirm():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    prompt_element = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    prompt_element.click()

    WebDriverWait(driver=driver,timeout=5).until(expected_conditions.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Guest999")
    alert.accept()
    result_in_text = driver.find_element(By.ID,"result").text
    assert result_in_text == "You entered: Guest999"