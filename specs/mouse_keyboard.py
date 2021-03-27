import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
driver.get("https://flipkart.com")
driver.maximize_window()
elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/button")
elem.click()

######## mouse move
ele = driver.find_element_by_xpath("//span[contains(text(),'Electronics')]")
#Create the object for Action Chains
actions = ActionChains(driver)
actions.move_to_element(ele)
# perform the operation on the element
actions.perform()

#### keyboard select all ctrl + a
action_chains = ActionChains(driver)
driver.get("https://www.google.com")
search = driver.find_element_by_name("q").send_keys("aaaaaaaaaaaaa")
action_chains.key_down(Keys.LEFT_CONTROL).send_keys("a").key_up(Keys.LEFT_CONTROL).perform()
