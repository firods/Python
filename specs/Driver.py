from selenium import webdriver

driver = None

def Initialize(name):
    global driver
    if name=="chrome":
        print("1")
        driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
    elif name == "firefox":
        print("2")
        driver = webdriver.Firefox(executable_path="C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\geckodriver.exe")
    else:
        print("3")
    return driver

def CloseDriver():
    global driver
    driver.quit()
