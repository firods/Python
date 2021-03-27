import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

########################### Google chrome ################################

driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
#driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
driver.get("http://www.google.co.in")
driver.maximize_window()

##Take screen-shot
driver.save_screenshot("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\data\\Google.png")

assert "Google" in driver.title

## Compare element is present or not
assert(driver.find_element_by_name("q").is_enabled()==True)

driver.quit()
# gmail login to logout using functions
# use data driven for gmail
# add assertions in gmail flow & screen-shot
# execute script on multiple browsers - take input from user
# redbus take date from user


#compare two screen-shot
#specific element screen-shot
#specific element text compare
