# Actions for handling keyboard and mouse events
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@allure.title("Handling mouse actions")
@allure.description("Move to previous page and next page"
                    " using mouse actions")
def test_actions():
    driver =  webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")


