#Explicit wait with fluent wait

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)


@pytest.mark.negative
@allure.title("App.vwo.com - Explicit wait fluent")
@allure.description("Verify that if email/pass is wrong, we will get a message-explicit fluent")
def test_login_vwo_explicit_wait_fluent():
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
    #time.sleep(4)

    #We use explicit wait
    ignore_list = [ElementNotVisibleException,ElementNotSelectableException]
    WebDriverWait(driver=driver,timeout=5,poll_frequency=1,ignored_exceptions=ignore_list).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"notification-box-description")))

    signin_error_msg = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(signin_error_msg.text)

    assert signin_error_msg.text == "Your email, password, IP address or location did not match"