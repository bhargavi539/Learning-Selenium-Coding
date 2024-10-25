import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import pytest
import allure

@pytest.mark.regression
@allure.title("stale element exception")
@allure.description("practice stale element exception webpage")
def test_stale_element_exception():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")
    time.sleep(5)

    try:
        text_box = driver.find_element(By.NAME,"q")
        driver.refresh()
        text_box.send_keys("QA Automation")
    except StaleElementReferenceException as sere:
        print(sere.msg)


    time.sleep(3)