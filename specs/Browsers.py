import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

########################### Google chrome ################################
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
#driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
driver.get("http://www.google.co.in")
driver.maximize_window()

########################### FIREFOX ################################
#capabilities = webdriver.DesiredCapabilities().FIREFOX
#binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
#driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities, executable_path="C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\geckodriver.exe")
#driver.get("http://www.google.com")

################# internet explorer ################################
#driver = webdriver.Ie("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\IEDriverServer.exe")
#driver.get("http://www.google.co.in")
#driver.maximize_window()
#time.sleep(5)
#elem = driver.find_element_by_id("lst-ib")
#elem.send_keys("find by name")

time.sleep(1)
print("Done")
#driver.close()
