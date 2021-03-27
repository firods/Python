import time
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(4)
driver.execute_script("window.alert();")
driver.switch_to.alert.accept()
