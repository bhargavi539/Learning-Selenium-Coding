from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure

@allure.title("Selecting the options from the radio or check box")
def test_homework_task():
    driver =  webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    gender = driver.find_element(By.CSS_SELECTOR,"input#sex-1")
    gender.click()

    profession_checkbox = driver.find_element(By.XPATH,"//input[@id='profession-1']")
    profession_checkbox.click()

    year_of_exp = driver.find_element(By.ID,"exp-2")
    year_of_exp.click()

    time.sleep(3)
