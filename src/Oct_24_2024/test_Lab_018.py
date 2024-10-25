import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

allure.title("Verify Select box or Dropdown")
allure.description("Verify static select box or dropdown")
def test_verify_select_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    select_element = driver.find_element(By.ID,"dropdown")
    select_box = Select(select_element)
    select_box.select_by_visible_text("Option 2")
    time.sleep(3)
    select_box.select_by_index(1)
    time.sleep(2)