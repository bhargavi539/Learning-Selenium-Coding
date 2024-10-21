from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure


#@pytest.mark.positive
@allure.title("Positive Testcase - awesomeqa registration form verification. ")
@allure.description("Verify that the registration is successful after entering all the valid details "
                    "and navigates to the next page with account has been created message")
def test_awesomeqa_registration_positive():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    driver.maximize_window()
    time.sleep(3)
    firstname_textbox = driver.find_element(By.XPATH,"//input[@name='firstname']")
    firstname_textbox.send_keys("abc")

    lastname_textbox = driver.find_element(By.XPATH,"//input[@placeholder='Last Name']")
    lastname_textbox.send_keys("123")

    email_textbox = driver.find_element(By.XPATH,"//input[@type='email' and @id='input-email']")
    email_textbox.send_keys("qwerty@pabc.com")

    telephone_textbox = driver.find_element(By.XPATH,"//input[@type='tel' and @placeholder='Telephone']")
    telephone_textbox.send_keys("2123456")

    password_textbox = driver.find_element(By.XPATH,"//input[@type='password' and @id='input-password']")
    password_textbox.send_keys("123456")

    confm_pwd_textbox = driver.find_element(By.XPATH,"//input[contains(@placeholder,'Confirm')]")
    confm_pwd_textbox.send_keys("123456")

    subscribe_button = driver.find_element(By.XPATH,"//input[@name='newsletter' and @value='1']")
    subscribe_button.click()

    policy_checkbox = driver.find_element(By.XPATH,"//input[contains(@name,'agree') and @value='1']")
    policy_checkbox.click()

    continue_button = driver.find_element(By.XPATH,"//input[@value='Continue']")
    continue_button.click()

    time.sleep(5)

    success_msg = driver.find_element(By.XPATH,"//div[@id='content']/h1").text
    assert success_msg == "Your Account Has Been Created!"
    print("The title of the page is ",driver.title)

    driver.quit()