import time
from selenium import webdriver

#n = input("enter number 1/2/3 = ")
#print("number = "+n)
#if n == "1":
#   print("1111111111111")
#else:
#   print("222222222")

######################## block red bus pop-up ##################
# accept input from user
enterdate = input("enter date in dd:mm:yyyy format ") #ex - 11:May:2019
user_day = enterdate.split(":")[0]
user_month = enterdate.split(":")[1]
user_year = enterdate.split(":")[2]

print("Day = "+user_day)
print("Month = "+user_month)
print("Year = "+user_year)

def selectday(date):
    #find table element
    ele_table = driver.find_element_by_xpath("//*[@id=\"rb-calendar_onward_cal\"]/table")

    #find all rows from table
    all_trs = ele_table.find_elements_by_tag_name("tr")
    #print("tr size = "+all_trs.size())

    for temp in all_trs:
        alltds = temp.find_elements_by_tag_name("td") #find all tds from each row
        for td in alltds:
            if td.text == date: #compare text with user input
               td.click()
               time.sleep(4)
               break

def selectmonth(month):
    month_yr = driver.find_element_by_xpath("//*[@id='rb-calendar_onward_cal']/table/tbody/tr[1]/td[2]").text
    act_month = month_yr.split(" ")[0]
    while(month!=act_month):
        driver.find_element_by_xpath("//*[@id='rb-calendar_onward_cal']/table/tbody/tr[1]/td[3]/button").click()
        month_yr = driver.find_element_by_xpath("//*[@id='rb-calendar_onward_cal']/table/tbody/tr[1]/td[2]").text
        act_month = month_yr.split(" ")[0]
        print(act_month)

def selectyear(year):
    month_yr = driver.find_element_by_xpath("//*[@id='rb-calendar_onward_cal']/table/tbody/tr[1]/td[2]").text
    act_year = month_yr.split(" ")[1]
    while(year!=act_year):
        driver.find_element_by_xpath("//*[@id='rb-calendar_onward_cal']/table/tbody/tr[1]/td[3]/button").click()
        month_yr = driver.find_element_by_xpath("//*[@id='rb-calendar_onward_cal']/table/tbody/tr[1]/td[2]").text
        act_year = month_yr.split(" ")[1]
        print(act_year)



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe')

driver.get("https://www.redbus.in/")
driver.maximize_window()
time.sleep(5)
#click calender icon
driver.find_element_by_xpath("//*[@id='search']/div/div[3]/span").click()
selectyear(user_year)
selectmonth(user_month)
selectday(user_day)

driver.quit()
print("Date selected successfully.")
