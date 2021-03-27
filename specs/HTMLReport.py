import unittest
from pyunitreport import HTMLTestRunner
#https://github.com/HttpRunner/PyUnitReport

def div(a,b):
    return a/b

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_test1(self): # test-case names run alphabetically
        self.assertEqual('1222223', '123')
        print('test1')

    def test_test2(self):
        self.assertTrue(1)
        print('test2')

    def test_test3(self):
        self.assertRaises(ZeroDivisionError, div, 1,0) #pass it raise divide by zero
        #self.assertRaises(ZeroDivisionError, div, 1,1) #fail not raise divide by zero
        print('test3')

if __name__ == '__main__':
        unittest.main(testRunner=HTMLTestRunner(output='C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\specs'))
