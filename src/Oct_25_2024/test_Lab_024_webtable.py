from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure

@allure.title("web table")
def test_web_table():
    driver =  webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

    row_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    rows = len(row_elements)

    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[3]/td")
    cols = len(col_elements)

    print("No. of rows: ",rows)
    print("No. of columns: ",cols)

    #Create dynamic path for the table to retrieve data
    """
        first_part = "//table[@id='customers']/tbody/tr["
        second_part = "]/td["
        third_part = "]"
        i = 2-->7
        j = 2-->3
    """
    first_part = "//table[@id='customers']/tbody/tr["
    second_part = "]/td["
    third_part = "]"
    for i in range(2,rows+1):
        for j in range(1,cols+1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            table_data = driver.find_element(By.XPATH,dynamic_path)
            print(table_data.text, end="  ")

        print("\n")