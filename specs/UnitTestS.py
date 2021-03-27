import unittest
from  selenium import webdriver
import json
from pyunitreport import HTMLTestRunner
import logging

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("F:\\Python\\selenium python\\chromedriver.exe")
logging.basicConfig(filename='F:\\Python\\selenium python\\assignments\\testunit.log',level=logging.NOTSET,format='%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
with open('F:\\Python\\selenium python\\assignments\\login.json') as f:
    data = json.load(f)

class unitTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #browser
        driver.get("https://accounts.google.com/")
        driver.maximize_window()
        logging.info('setUpClass')
        #readjson


    def setUp(self):
        #login
        username=data["credentials"][0]["login"]["uname"]
        password=data["credentials"][0]["login"]["pwd"]
        print(username)
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/form/div/div/input").submit()
        logging.info('setUp')

    def tearDown(self):
        #Logout
        driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td[1]/div/table/tbody/tr/td[4]/a/i").submit()
        logging.info('tearDown')

    @classmethod
    def tearDownClass(self):
        driver.close()
        logging.warning('tearDownClass')

    def test_emailassetion(self):
        print("email assert")
        logging.info('emailassertion')

    def test_sendEmail(self):
        driver.find_element_by_xpath("\\input[@class='T-I J-J5-Ji T-I-KE L3']").click()
        driver.find_element_by_xpath("\\textarea[@name='to']").send_keys("sayalikhadsare8@gmail.com")
        driver.find_element_by_xpath("\\input[@name='subjectbox']").send_keys("testemail")
        driver.find_element_by_xpath("//*[@id=':r8']").send_keys("Hi, this is test email")
        #driver.find_element_by_xpath("//*[@id=":pt"]").click()
        logging.info('sendemail')

if __name__ == '__main__':
        unittest.main(testRunner=HTMLTestRunner(output='F:\\Python\\selenium python\\assignments\\reports'))
