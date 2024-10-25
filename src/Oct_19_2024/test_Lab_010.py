from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time
import allure


@pytest.mark.negative
@allure.title("Positive Testcase - App.vwo.com Find all the buttons by Tag name. ")
@allure.description("Find all the buttons using tag name and print their text")
def test_find_buttons_in_the_login_page():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    time.sleep(3)

    button_elements = driver.find_elements(By.TAG_NAME,"button")
    print(len(button_elements))
    print(type(button_elements))

    for button in button_elements:
        print(button.text)

    all_links = driver.find_elements(By.TAG_NAME,"a")
    print(len(all_links))

    for link in all_links:
        print(link.text)