from selenium import webdriver
import allure
import pytest

@allure.title("Verify the title of the webpage")
def test_verify_title():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    assert driver.title == "Login - VWO"