import datetime
import unittest
import time
from selene.api import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.test_data import *
import requests

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.execute_date = datetime.datetime.today().strftime('%c')
        print('Test started: ' + cls.execute_date)

    def setUp(self):
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome(DRIVER_PATH)
        #browser.set_driver(self.driver)
        #browser.driver().maximize_window()
        self.sess = requests.session()

    def tearDown(self):
        self.sess.close()
        browser.quit()
        #if self.driver is not None:
        #    self.driver.close()
        #    self.driver.quit()


if __name__ == '__main__':
    unittest.main()
