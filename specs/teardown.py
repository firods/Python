import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import json
import time
import unittest
driver = webdriver.Chrome(executable_path=r"C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
#with open('D:\\python\\Python Project\\Data\\Gmail.json') as f:data = json.load(f)
class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        time.sleep(5)
        driver.maximize_window()
        driver.get("https://www.gmail.com")
        time.sleep(5)
        print('setUpClass')

    def setUp(self):
            print ("*"+driver.title)
            assert "Gmail" in driver.title
            #Send UserName details through JSON
            driver.find_element_by_xpath("//input[contains(@type,'email')]").clear()
            driver.find_element_by_xpath("//input[contains(@type,'email')]").send_keys("shrikantfirodiya4@gmail.com")
            #Click on next button
            elem = driver.find_element_by_xpath("//span[contains(text(),'Next')]")
            elem.click()

            time.sleep(5)
            driver.find_element_by_xpath("//input[contains(@type,'password')]").click()
            #Send user password details through JSON
            driver.find_element_by_xpath("//input[contains(@type,'password')]").send_keys("Admin@9850")
            # NextButton
            driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()
            time.sleep(40)
            print ('setUp')

    def test_test1(self): # test-case names run alphabetically
        assert(driver.find_element_by_xpath("//a[contains(@aria-label,'Pratik Ghodsad')]").is_enabled()==False)
        driver.find_element_by_xpath("//a[contains(@aria-label,'Pratik Ghodsad')]").click()
        time.sleep(10)
        print('test1')

    def test_test2(self):
        driver.find_element_by_xpath("//a[contains(text(),'Sign out')]").click()
        time.sleep(10)
        print('test2')

        @classmethod
        def tearDownClass(cls):
            print('tearDownClass')


        def tearDown(self):
            print('tearDown')


if __name__ == '__main__':
        unittest.main(testRunner=HTMLTestRunner(output='C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\specs'))
