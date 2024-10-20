from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure


@pytest.mark.negative
@allure.title("Negative Testcase - App.vwo.com - Wrong Email, Password -> Error Message.")
@allure.description("Verify that if email/pass is wrong, we will get a message")
def test_verify_login_vwo_negative():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    # Find the email,
    # Find the password,
    # Click on the Sign Button
    email_textbox = driver.find_element(By.ID,"login-username")
    email_textbox.send_keys("abc@asd.com")

    pwd_textbox = driver.find_element(By.NAME,"password")
    pwd_textbox.send_keys("abc123")

    signin_button = driver.find_element(By.ID,"js-login-btn")
    signin_button.click()

    # Verify that message is visible.
    time.sleep(4)
    signin_error_msg = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(signin_error_msg.text)

    assert signin_error_msg.text == "Your email, password, IP address or location did not match"