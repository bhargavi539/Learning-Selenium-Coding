# Actions for handling keyboard and mouse events
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@allure.title("Actions")
@allure.description("Handling keyboard and mouse events by using Actions")
def test_actions():
    driver =  webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")
    actions = ActionChains(driver)
    (actions.key_down(Keys.SHIFT)
     .send_keys_to_element(first_name,"oswold")
     .key_up(Keys.SHIFT).perform())

    time.sleep(5)
    driver.quit()

