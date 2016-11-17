'''
Created on Nov 17, 2016

@author: root
'''
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class Test(unittest.TestCase):


    def setUp(self):
        ff_binary = FirefoxBinary('/usr/bin/firefox')
        profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Firefox(firefox_binary=ff_binary, firefox_profile=profile)
        

    def tearDown(self):
        self.driver.quit()


    def testName(self):
        self.driver.get('http://www.mahsumakbas.net')
        print self.driver.title



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()