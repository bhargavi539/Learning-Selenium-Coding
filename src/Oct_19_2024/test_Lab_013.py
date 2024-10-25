from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure

@pytest.mark.negative
@allure.title("Negative Testcase - Verify error message for invalid username and password ")
@allure.description("Verify that the page shows error message when invalid username and password are entered")
def test_verify_error_msg_login_app_vwo():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    time.sleep(3)

    email_textbox = driver.find_element(By.ID,"login-username")
    email_textbox.send_keys("abc@123.com")

    password_textbox = driver.find_element(By.ID,"login-password")
    password_textbox.send_keys("123456")

    signin_button = driver.find_element(By.ID,"js-login-btn")
    signin_button.click()

    time.sleep(5)

    signup_error_msg = driver.find_element(By.CLASS_NAME,"notification-box-description").text
    assert signup_error_msg == "Your email, password, IP address or location did not match"

    driver.quit()