from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure

@pytest.mark.positive
@allure.title("Print the titles of the items in the ebay website")
@allure.description("Verify that the titles of the items are retreived using CSS Selector")
def test_get_search_item_titles_prices():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    driver.maximize_window()
    time.sleep(3)
    search_box = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for anything']")
    #search_box= driver.find_element(By.CSS_SELECTOR,"#gh-ac"
    search_box.send_keys("macmini")
    search_box_button = driver.find_element(By.CSS_SELECTOR,"#gh-btn")
    search_box_button.click()

    list_of_items = driver.find_elements(By.CSS_SELECTOR,".s-item__title")
    list_of_elements = driver.find_elements(By.CSS_SELECTOR,".s-item__price")

    for title in list_of_items:
        print(title.text)

    time.sleep(3)
    print("Printing titles and the prices")

    for title in list_of_elements:
        print(title.text)

    time.sleep(3)

    driver.quit()