import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

########################### Google chrome ################################

#driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
#driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
#driver.get("http://www.google.co.in")
#driver.maximize_window()

with open('C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\data\\data.json') as f:
    data = json.load(f)
    #print(data["credentials"])
    #print(data["credentials"][0]["both_valid"])
    #print(data["credentials"][0]["both_valid"]["uname"])
    print(data["credentials"][0]["uname_valid"]["uname"]) #cccc

    login(data["credentials"][0]["both_valid"]["uname"],data["credentials"][0]["both_valid"]["pwd"],"expected message")
    login(data["credentials"][0]["uname_valid"]["uname"],data["credentials"][0]["uname_valid"]["pwd"],"expected message")
    #login(data["credentials"][0]["pwd_valid"]["uname"],data["credentials"][0]["pwd_valid"]["pwd"],"expected message")

#print(data)


#driver.quit()
