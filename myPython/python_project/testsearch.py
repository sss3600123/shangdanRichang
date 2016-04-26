#coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SearchTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		
	def testSearch(self):
		driver = self.driver
		driver.get('https://www.baidu.com')
		ele = driver.find_element_by_id('kw')
		ele.send_keys('php开发')
		ele.send_keys(Keys.RETURN)
		assert "No result found" not in driver.page_source
	
	def tearDown(self):
		time.sleep(5)
		self.driver.close()
		
		

if __name__ == '__main__':
	unittest.main()