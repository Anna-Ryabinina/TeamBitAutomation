import unittest
import time
from selene.api import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.test_data import *


class BaseTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(DRIVER_PATH)
        browser.set_driver(self.driver)

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
