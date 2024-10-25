import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest
import allure

@pytest.mark.regression
@allure.title("selenium exceptions")
@allure.description("practise exceptions webpage")
def test_verify_alerts():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    try:
        button = driver.find_element(By.ID,"id_does_not_exist")
    except NoSuchElementException as nsee:
        print("Element is not found in the webpage: ",nsee.msg)

    finally:
        print("Test execution is completed")