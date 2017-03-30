'''
Created on 17-Mar-2017

@author: prince.mahi
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lib2to3.tests.support import driver
from selenium.webdriver import ActionChains



if __name__ == '__main__':
    
    driver = webdriver.Firefox()
    driver.get("https://www.abhibus.com")
    driver.find_element_by_xpath(".//*[@id='myModalLay']/div/div[1]/div[2]/span").click()
    driver.find_element_by_xpath(".//*[@id='source']").send_keys("Bangalore")
    driver.find_element_by_xpath(".//*[@id='destination']").send_keys("Hubli")
    driver.find_element_by_xpath(".//*[@id='datepicker1']").click()
    driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[4]/td[6]/a").click()
    driver.find_element_by_xpath(".//*[@id='roundTrip']/a").click()
    #driver.find_element_by_xpath(".//*[@id='roundTrip']/a").click()
    #driver.close()
    
   