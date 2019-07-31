import unittest
from common.desired_cap import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('----------setUp----------')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('___________tearDwon__________')
        sleep(10)
        self.driver.close_app()