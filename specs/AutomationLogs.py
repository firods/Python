import unittest
import logging
#https://docs.python.org/2/library/logging.html

def div(a,b):
    return a/b

logging.basicConfig(filename='C:\\Users\\Shrikant\\Desktop\\Auto\\Python\\specs\\test.log',level=logging.NOTSET,format='%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info('setUpClass')

    @classmethod
    def tearDownClass(cls):
        logging.warning('tearDownClass')

    def setUp(self):
        logging.info('setUp')

    def tearDown(self):
        logging.debug('tearDown')

    def test_test1(self): # test-case names run alphabetically
        self.assertEqual('123', '123')
        logging.error('test1')

    def test_test2(self):
        self.assertTrue(1)
        logging.info('test2')

    def test_test3(self):
        self.assertRaises(ZeroDivisionError, div, 1,0) #pass it raise divide by zero
        #self.assertRaises(ZeroDivisionError, div, 1,1) #fail not raise divide by zero
        logging.critical('test3')

if __name__ == '__main__':
    unittest.main()
