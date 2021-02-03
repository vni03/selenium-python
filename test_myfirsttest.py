import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains

def test_1():
    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
    driver.get('file://C:/work/selenium-redirects/practice_page.html')
    action = ActionChains(driver)
    first_name = driver.find_element_by_id("firstname")
    first_name.send_keys("viktoria")
    last_name = driver.find_element_by_id("lastname")
    action.click(on_element = last_name)
    last_name.send_keys("nikolova")
    action.click(on_element = first_name)
    action.perform()


    time.sleep(3)

    result_firstname = first_name.get_attribute("value")
    expected_firstname = "Viktoria"
    result_lastname = last_name.get_attribute("value")
    expected_lastname = "Nikolova"

    assert expected_firstname == result_firstname
    assert expected_lastname == result_lastname

    driver.quit()

