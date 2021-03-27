import time
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
driver.get("http://www.google.co.in")
driver.maximize_window()

##################################################################
assert "Google" in driver.title
text = driver.title
print("-------------"+text)
############################## find by name ##########################
elem = driver.find_element_by_name("q")
elem.send_keys("find by name")
time.sleep(1)
elem.clear()
############################## find by xpath ##############################
elem = driver.find_element_by_xpath("//input[@id='lst-ib']")
elem.send_keys("find by xpath")
time.sleep(1)
elem.clear()
############################# find by classname #######################
elem = driver.find_element_by_class_name("gsfi")
elem.send_keys("find by classname")
time.sleep(1)
elem.clear()
############################# find by link text ######################
driver.find_element_by_link_text("Gmail")
gmailtext = driver.find_element_by_link_text("Gmail").text
print("Gmail text = "+gmailtext)
driver.find_element_by_link_text("Gmail").click()
time.sleep(1)
driver.back()
############################# find by partial link text ######################
driver.find_element_by_link_text("Gmail")
gmailtext = driver.find_element_by_partial_link_text("Gmail").text
print("Gmail partial text = "+gmailtext)
driver.find_element_by_partial_link_text("Gmail").click()
time.sleep(1)
driver.back()
############################ find by css selector ###########################
elem = driver.find_element_by_css_selector("#lst-ib") #lst-ib
elem.send_keys("find by css selector")
time.sleep(1)
elem.clear()
