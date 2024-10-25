import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.regression
@allure.title("stale element exception")
@allure.description("practice stale element exception webpage")
def test_stale_element_exception():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")

    try:
        WebDriverWait(driver=driver,timeout=10).until(EC.element_to_be_clickable((By.ID,"clickonit")))
    except TimeoutException as TOE:
        print(TOE.msg)
        print("Timeout exception occured. 10 seconds passed")

    finally:
        driver.quit()