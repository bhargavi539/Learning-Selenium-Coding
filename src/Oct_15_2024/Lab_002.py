# Importing python script from Selenium IDE

from selenium import webdriver
import allure
import pytest

@allure.title("Verify the current title and current url of the webpage")
def test_verify_title():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.title == "CURA Healthcare Service"
    assert "CURA Healthcare Service" in driver.page_source