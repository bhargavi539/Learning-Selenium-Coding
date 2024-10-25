from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure

@pytest.mark.positive
@allure.title("Positive Testcase - awesomeqa.com First use of Xpath Selector ")
@allure.description("Using the Xpath selector to find the element")
def test_xpath_selector():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    driver.maximize_window()
    time.sleep(3)
    firstname_textbox = driver.find_element(By.XPATH,"//input[@name='firstname']")
    firstname_textbox.send_keys("Lakshmi")
    time.sleep(5)
    driver.quit()