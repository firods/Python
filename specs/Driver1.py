import unittest
import Driver

name = input("enter browser name")
print(name)

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('setUp') # execute before every test-case
        Driver.Initialize(name)
        # login

    def tearDown(self): # execute after every test-case
        print('tearDown')
        Driver.CloseDriver()
        #logout

    def test_test1(self): # test-case names run alphabetically
        Driver.driver.get("https://www.google.com")
        print('test1')
        #assertion for email

    def test_test2(self):
        Driver.driver.get("https://www.facebook.com")
        print('test2')
        # send email
        #verify email in inbox

    def test_test3(self):
        Driver.driver.get("https://www.flipkart.com")
        #self.assertRaises(ZeroDivisionError, div, 1,1) #fail not raise divide by zero
        print('test3')

if __name__ == '__main__':
    unittest.main()
