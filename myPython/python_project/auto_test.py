#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
kw = driver.find_element_by_id('kw')
kw.send_keys('php开发')
kw.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source	#断言语句
# driver.find_element_by_id('su').click()
time.sleep(5)
driver.close()
