from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure

@allure.title("web table")
@allure.description("Find the preceding element of a specific element eg:- Helen Bennett")
def test_web_table():
    driver =  webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")

    table = driver.find_element(By.XPATH,"//table[@class='tsc_table_s13']/tbody")
    rows_in_a_table = table.find_elements(By.TAG_NAME,"tr") # --> //table[@class='tsc_table_s13']/tbody/tr

    for row in rows_in_a_table:
        columns = row.find_elements(By.TAG_NAME,"td")
        for cell in columns:
            print(cell.text)