#Verify the current url, navigation to login and verify login functionality
# https://katalon-demo-cura.herokuapp.com/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_navigation_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    btn_appoint = driver.find_element(By.ID,"btn-make-appointment")
    btn_appoint.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    username = driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")

    btn_login = driver.find_element(By.ID,"btn-login")
    btn_login.click()

    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"