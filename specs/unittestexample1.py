import unittest
from selenium import webdriver

def div(a,b):
    return a/b
age = 25

name = None
driver = None

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("You are %d years old" % age)
        print('setUpClass') #execute only once in start
        name = input("enter browser name")
        print(name)
        driver  = None
        if name=="chrome":
            print("1")
            driver = webdriver.Chrome("C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\chromedriver.exe")
        elif name == "firefox":
            print("2")
            driver = webdriver.Firefox(executable_path="C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\drivers\\geckodriver.exe")
        else:
            print("3")

    @classmethod
    def tearDownClass(self):
        print('tearDownClass') # execute only once in end
        #browser close

    def setUp(self):
        driver.get("https://www.google.com")
        print('setUp') # execute before every test-case
        # login

    def tearDown(self): # execute after every test-case
        print('tearDown')
        #logout

    def test_test1(self): # test-case names run alphabetically
        self.assertEqual('123', '123')
        print('test1')
        #assertion for email

    def test_test2(self):
        self.assertTrue(1)
        print('test2')
        driver.get("https://www.facebook.com")
        # send email
        #verify email in inbox

    def test_test3(self):
        self.assertRaises(ZeroDivisionError, div, 1,0) #pass it raise divide by zero
        #self.assertRaises(ZeroDivisionError, div, 1,1) #fail not raise divide by zero
        print('test3')

if __name__ == '__main__':
    unittest.main()
