import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
driver.get('file://C:/work/selenium-redirects/practice_page.html')

first_name = driver.find_element_by_id("firstname")
first_name.send_keys("viktoria")
last_name = driver.find_element_by_id("lastname")
last_name.send_keys("nikolova")
time.sleep(3)



