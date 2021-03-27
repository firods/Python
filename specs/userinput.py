from selenium import webdriver

name = input("enter browser name")
print(name)
if name=="chrome":
    print("1")
    driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
elif name == "firefox":
    print("2")
    driver = webdriver.Firefox(executable_path="C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\geckodriver.exe")
else:
    print("3")

driver.get("https://www.google.com")
